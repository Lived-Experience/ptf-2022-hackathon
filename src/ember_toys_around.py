import pygame
import random

# reminder: pygame coordinate system has (0,0) in top left
# and (WIDTH,HEIGHT) in the bottom right.

WIDTH = 1280
HEIGHT = 800

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
    (x, y) = self.center
    (dx,dy) = self.vel
    nx, clamped = clamp(x+x*dx, 0, WIDTH)
    if clamped:
      dx = -dx

    ny, clamped2 = clamp(y+y*dy, 0, HEIGHT)
    if clamped2:
      dy = -dy
  
    (dx,dy) = (random.uniform(dx - dx * self.drift_rate, dx + dx * self.drift_rate), random.uniform(dy - dy * self.drift_rate, dy + dy * self.drift_rate))
    dx, _ = clamp(dx, -0.3,0.3)
    dy, _ = clamp(dy, -0.3,0.3)
    self.vel = (dx,dy)
    self.center = (nx,ny)

  def draw(self, surface):
    pygame.draw.circle(surface, color= (255,0,0), center= self.center, radius= 15)

class GameSimulation:
  def __init__(self):
    self.all_objects = [DriftingCircle((WIDTH/2,HEIGHT/2))]

  def update(self):
    for obj in self.all_objects:
      obj.update()
    
  def draw(self, surface):
    for obj in self.all_objects:
      obj.draw(surface)
  
def run_game():
  gs = GameSimulation()

  pygame.init()
  screen = pygame.display.set_mode((1280,800))

  running = True
  while running:
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        running = False
      elif event.type == pygame.QUIT:
        running = False
      elif event.type in [pygame.MOUSEMOTION,pygame.WINDOWLEAVE,pygame.WINDOWENTER,pygame.ACTIVEEVENT]:
        pass
      else:
        print(f"We saw an event like this! {event}")
    gs.update()
    screen.fill((0,0,0))
    gs.draw(screen)
    pygame.display.update()

if __name__ == "__main__":
  run_game()