from abc import ABCMeta

import pygame
from pygame.sprite import AbstractGroup


class BaseArtefact(pygame.sprite.Sprite):

    def __init__(self, image, x, y, *groups: AbstractGroup):
        super().__init__(*groups)
        self.image = None
        self.rect = None
        self.x = x
        self.y = y
        if image:
            self.load_image(image, x, y)

    def load_image(self, image, x, y):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.x = self.rect[0] = x
        self.y = self.rect[1] = y
        return self

    def draw(self, window):
        return self
