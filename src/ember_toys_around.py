import pygame
import random
import sim

# reminder: pygame coordinate system has (0,0) in top left
# and (WIDTH,HEIGHT) in the bottom right.

import viewer
WIDTH = 1280
HEIGHT = 800

def run_game():
  gs = sim.GameSimulation(viewer.Viewer())

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