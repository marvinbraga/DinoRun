from enum import Enum

from pygame.sprite import AbstractGroup

from core.artefacts import Artefact


class BackgroundMoveType(Enum):
    TOP_DOWN = 0
    DOWN_TOP = 1
    LEFT_RIGHT = 2
    RIGHT_LEFT = 3


class Background(Artefact):

    def __init__(self, image, x, y, *groups: AbstractGroup):
        super().__init__(image, x, y, *groups)


class BaseBackgroundManager:

    def __init__(self, scene):
        self.scene = scene
        self._artefacts1 = []
        self._artefacts2 = []
