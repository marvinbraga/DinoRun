from enum import Enum

from pygame.sprite import AbstractGroup

from core.artefacts import Artefact


class BackgroundMoveType(Enum):
    TOP_DOWN = 0
    DOWN_TOP = 1
    LEFT_RIGHT = 2
    RIGHT_LEFT = 3


class Background:

    def __init__(self, image, x, y, width, height, move_type, speed, *groups: AbstractGroup):
        self.x = x
        self.y = y
        self.speed = speed
        self.move_type = move_type
        self.height = height
        self.width = width
        image2_position = self.get_image_position() 
        self.image1 = Artefact(image, x, y, *groups)
        self.image2 = Artefact(image, *image2_position, *groups)

    def get_image_position(self):
        result = {
            BackgroundMoveType.TOP_DOWN: (self.x, self.y - self.height),
            BackgroundMoveType.DOWN_TOP: (self.x, self.y + self.height),
            BackgroundMoveType.LEFT_RIGHT: (self.x - self.width, self.y),
            BackgroundMoveType.RIGHT_LEFT: (self.x + self.width, self.y),
        }[self.move_type]
        return result

    def move(self):
        self.image1.rect[0] = self.image1.x \
            if self.image1.rect[0] <= -self.width else self.image1.rect[0] - self.speed
        self.image2.rect[0] = self.image2.x \
            if self.image2.rect[0] <= self.image1.x else self.image2.rect[0] - self.speed
        
    def update(self):
        self.move()


class BaseBackgroundManager:

    def __init__(self, scene):
        self.scene = scene
        self._artefacts1 = []
        self._artefacts2 = []
