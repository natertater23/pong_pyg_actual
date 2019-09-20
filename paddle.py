import pygame
pygame.init()
RED = (255, 0, 0)


class Paddle(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        # create the surface, we make it transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(RED)
        self.image.set_colorkey(RED)
        # draw rect with given color and width height, coordinates don't matter since will be moving anyways
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        # make that rect our rect
        self.rect = self.image.get_rect()
    # These will affect the way the paddle moves and to make sure they stay in scope
    def move_up(self, pixels):

        self.rect.y -= pixels
        if self.rect.y < 0:
            self.rect.y = 0

    def move_down(self, pixels):
        self.rect.y += pixels
        if self.rect.y > 400:
            self.rect.y = 400

    def move_left(self, pixels):
        self.rect.x -= pixels
        if self.rect.x < 0:
            self.rect.x = 0

    def move_right(self, pixels):
        self.rect.x += pixels
        if self.rect.x > 700:
            self.rect.x = 700
