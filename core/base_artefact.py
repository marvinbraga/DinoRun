from abc import ABCMeta

import pygame
from pygame.sprite import AbstractGroup


class BaseArtefact(pygame.sprite.Sprite):

    def __init__(self, image, x, y, *groups: AbstractGroup):
        super().__init__(*groups)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect[0] = x
        self.rect[1] = y

    def draw(self, window):
        return self
