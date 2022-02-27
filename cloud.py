import random

import pygame
from pygame.sprite import AbstractGroup

from core.artefacts import Artefact
from core.rl_movement import MovementRight2Left


class Cloud(Artefact):

    def __init__(self, *groups: AbstractGroup):
        x, y = 700, random.randrange(10, 110)
        super().__init__("sprites/cloud.png", x, y, *groups)
        self.image = pygame.transform.scale(self.image, (70, 40))
        self.movement = MovementRight2Left(self, 1, -100)

    def update(self):
        super().update()
        self.movement.move()
