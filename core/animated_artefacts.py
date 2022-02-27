import pygame
from pygame.sprite import AbstractGroup

from core import settings
from core.base_artefact import BaseArtefact


class AnimatedArtefact(BaseArtefact):

    def __init__(self, image, x, y, frames=(1, 4), *groups: AbstractGroup):
        super().__init__(image.format(1), x, y, *groups)
        self.index = 0
        self.speed = 10
        self.tick_limit = settings.FPS
        self.ticks = 0

        self.frames = (frames[0], frames[1] + 1)
        self.frame = 0
        self.images = [pygame.image.load(image.format(i)) for i in range(*self.frames)]

    def update(self):
        super().update()
        self.animate()

    def animate(self):
        self.ticks += 1
        if self.ticks >= self.tick_limit:
            self.ticks = 0
            self.index = (self.index + 1) % (max(*self.frames) - 1)

        self.image = self.images[self.index]
