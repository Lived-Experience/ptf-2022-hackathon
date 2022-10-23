import random
import pygame
import viewer

WIDTH = 1280
HEIGHT = 800

starting="""Hello!  Welcome to the trans experience!
\n
Imagine yourself existing in the world as a trans person. Life isn't easy, but there are good things too. You'll encounter all kinds of transphobic microaggressions and friends/community members in this world and will have to decide how to interact with them. This game is meant to be fun an educational while showing the kinds of microaggressions that embolden and enable the more insidious violence. The reality in the world is far more brutal, especially for trans women and even more so for trans women of color.
\n
You can think of your Resistance Quotient (RQ) as your overall health - if you run all the way out the game is over. If you win ten awards by overcoming transphobes, you'll be declared pro trans. Try again and again to see how high you can score!"""

def clamp(val, min, max):
  if val < min:
    return min, True
  if val > max:
    return max, True
  return val, False

class DriftingCircle:
  """A red 50-px wide circle that drifts around slowly and randomly."""

  def __init__(self, cent):
    self.center = cent
    self.drift_rate = 0.0002
    self.vel = (0.05,-0.05)
  
  def update(self):
    pass
 
  def draw(self, surface):
    pygame.draw.circle(surface, color= (255,0,0), center= self.center, radius= 15)

class GameSimulation:
  def __init__(self, viewer: viewer.Viewer):
    self.viewer = viewer
    self.all_objects = [DriftingCircle((WIDTH/2,HEIGHT/2))]

  def update(self):
    for obj in self.all_objects:
      obj.update()
    self.viewer.set_current_scene(starting, None, ["first option", "second option"])
    s = self.viewer.selected_option()
    print(f"debug: User wants index {s}")

  def draw(self, surface):
    for obj in self.all_objects:
      obj.draw(surface)