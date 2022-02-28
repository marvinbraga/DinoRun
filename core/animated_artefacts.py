import os

import pygame
from pygame.sprite import AbstractGroup

from core import settings
from core.base_artefact import BaseArtefact


class AnimatedArtefact(BaseArtefact):

    def __init__(self, image, x, y, frames=(1, 4), *groups: AbstractGroup):
        first_image = None
        if image:
            first_image = image.format(1)
        super().__init__(first_image, x, y, *groups)
        self.index = 0
        self.speed = 10
        self.tick_limit = settings.FPS
        self.ticks = 0

        self.frames = (frames[0], frames[1] + 1)
        self.frame = 0
        self.images = []
        if first_image:
            self.images = [pygame.image.load(image.format(i)) for i in range(*self.frames)]

    @staticmethod
    def load_images(files):
        return [pygame.image.load(i) for i in files]

    @staticmethod
    def adjust_images(images, width, height):
        return [
            pygame.transform.scale(image, (width, height)) for image in images
        ]

    def update(self):
        super().update()
        self.animate()

    def animate(self):
        self.ticks += 1
        if self.ticks >= self.tick_limit:
            self.ticks = 0
            self.index = (self.index + 1) % (max(*self.frames) - 1)

        if self.images:
            self.image = self.images[self.index]
