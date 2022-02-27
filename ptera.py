import random

import pygame
from pygame.sprite import AbstractGroup

from core.animated_artefacts import AnimatedArtefact
from core.rl_movement import MovementRight2Left


class Ptera(AnimatedArtefact):

    def __init__(self, *groups: AbstractGroup):
        x, y = random.randrange(750, 1000), random.choice([175, 156, 110])
        image = "sprites/ptera{}.png"
        frames = (1, 2)
        super().__init__(image, x, y, frames, *groups)
        self.adjust_images(50, 40)
        self.movement = MovementRight2Left(self, 8, -100)
        self.tick_limit = 3

    def update(self):
        super().update()
        self.move()

    def move(self):
        self.movement.move()