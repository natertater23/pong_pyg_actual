import pygame
from random import randint

RED = (255, 0, 0)


class Ball(pygame.sprite.Sprite):

    def __init__(self, color, center, radius, width):
        super.__init__()
        self.image = pygame.Surface([radius, width])
        self.image.fill(RED)
        self.image.set_colorkey(RED)
        pygame.draw.circle(self.image, color, center, radius, width)
        self.velocity = [randint(4, 8), randint(-8, 8)]
        self.circle = self.image.get_rect()

    def update(self):
        self.circle.x += self.velocity[0]
        self.circle.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8, 8)
