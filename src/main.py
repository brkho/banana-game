import pygame
import game
import sys

FPS = 60
SHOW_FPS = True

def main():
  pygame.init()
  pygame.display.set_mode((800, 600))
  main_surface = pygame.display.get_surface()
  g = game.Game()
  fps_clock = pygame.time.Clock()
  pygame.mouse.set_visible(True)
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
      elif event.type == pygame.MOUSEBUTTONDOWN:
        g.handle_click(*pygame.mouse.get_pos())
      else:
        pass
    fps_clock.tick(FPS)
    if fps_clock.get_fps() > 0:
      g.update(1.0 / fps_clock.get_fps())
      g.draw(main_surface)
    pygame.display.update()
    pygame.display.flip()

  sys.exit()


if __name__ == '__main__':
    main()