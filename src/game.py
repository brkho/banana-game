import bananawoman
import pygame
import sys

class Game(object):
  def __init__(self):
    self.speed = 3
    self.score = 0
    self.lives = 10
    self.bananawoman = bananawoman.BananaWoman(self.speed)
    self.font = pygame.font.SysFont(None, 60)

  def update(self, dt):
    if not self.bananawoman.update(dt):
      self.bananawoman = bananawoman.BananaWoman(self.speed)
      self.lives -= 1
    if self.lives == 0:
      print 'u lose'
      sys.exit()

  def draw(self, surface):
    surface.fill((0, 255, 0))
    score_text = self.font.render('score: {}'.format(self.score), False, (255, 0, 0))
    surface.blit(score_text, (30, 30))
    lives_text = self.font.render('lives: {}'.format(self.lives), False, (0, 0, 255))
    surface.blit(lives_text, (30, 100))
    self.bananawoman.draw(surface)

  def handle_click(self, x, y):
    if self.bananawoman.rect.collidepoint(x, y):
      self.speed -= 0.1
      self.score += 1
      self.bananawoman = bananawoman.BananaWoman(self.speed)
