import pygame
import random

class BananaWoman(pygame.sprite.Sprite):
  def __init__(self, speed):
    super(BananaWoman, self).__init__()
    self.image = pygame.image.load('assets/bananawoman.png')
    self.transformed_image = self.image
    self.image_dimensions = self.image.get_rect()
    self.pos = (int(random.random() * 800), int(random.random() * 600))
    transformed_dim = self.transformed_image.get_rect()
    self.rect = pygame.Rect(self.pos[0] - (transformed_dim.width / 2),
        self.pos[1] - (transformed_dim.height / 2), transformed_dim.width, transformed_dim.height)
    self.size = 1.0
    self.speed = speed

  # returns false if bananawoman is dead
  def update(self, dt):
    self.size = max(self.size - (dt / self.speed), 0)
    self.transformed_image = pygame.transform.scale(self.image, (int(self.image_dimensions.width * self.size),
        int(self.image_dimensions.height * self.size)))
    transformed_dim = self.transformed_image.get_rect()
    self.rect = pygame.Rect(self.pos[0] - (transformed_dim.width / 2),
        self.pos[1] - (transformed_dim.height / 2), transformed_dim.width, transformed_dim.height)
    return self.size != 0

  def draw(self, surface):
    # pygame.draw.rect(surface, (255, 0, 0), self.rect)
    surface.blit(self.transformed_image, self.rect)
