import pygame
from pygame.sprite import AbstractGroup

from core import settings
from core.base_artefact import BaseArtefact


class AnimatedArtefact(BaseArtefact):

    def __init__(self, image, x, y, frames=(1, 4), *groups: AbstractGroup):
        super().__init__(image.format(1), x, y, *groups)
        self.tick = 0
        self.tick_limit = settings.FPS

        self.frames = (frames[0], frames[1] + 1)
        self.frame = 0
        self.images = [pygame.image.load(image.format(i)) for i in range(*self.frames)]

    def update(self):
        super().update()
        self.animate()

    def animate(self):
        self.tick += 1
        if self.tick > self.tick_limit:
            self.tick = 0
            self.frame = self.frame + 1 if self.frame < self.frames[1] - 1 else self.frames[0]
        self.image = self.images[self.frame - 1]
