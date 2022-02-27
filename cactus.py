import random
from enum import Enum

import pygame
from pygame.sprite import AbstractGroup

from core.artefacts import Artefact
from core.rl_movement import MovementRight2Left


class CactusSize(Enum):

    SMALL = 0
    BIG = 1

    def get_class(self):
        return {
            CactusSize.SMALL: SmallCactus,
            CactusSize.BIG: BigCactus
        }[self]

    @staticmethod
    def get_random_class():
        result = random.choice([CactusSize.SMALL, CactusSize.BIG])
        return result.get_class()


class BaseCactus(Artefact):

    def __init__(self, image, width, height, *groups: AbstractGroup):
        x, y = random.randrange(720, 1000), 175
        super().__init__(image, x, y, *groups)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.movement = MovementRight2Left(self, 4, -100)
        self.is_cactus = True
        self.is_ptera = False

    def update(self):
        self.move()

    def move(self):
        self.movement.move()


class SmallCactus(BaseCactus):

    def __init__(self, *groups: AbstractGroup):
        super().__init__("sprites/cacti-small.png", 45, 45, *groups)


class BigCactus(BaseCactus):

    def __init__(self, *groups: AbstractGroup):
        super().__init__("sprites/cacti-big.png", 45, 65, *groups)
