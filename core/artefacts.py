import pygame
from pygame.sprite import AbstractGroup

from core.base_artefact import BaseArtefact
from core.animated_artefacts import AnimatedArtefact


class Artefact(BaseArtefact):

    def __init__(self, image, x, y, *groups: AbstractGroup):
        super().__init__(image, x, y, *groups)
