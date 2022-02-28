from enum import Enum

from pygame.sprite import AbstractGroup

from core.artefacts import Artefact


class BackgroundMoveType(Enum):
    TOP_BOTTOM = 0
    BOTTOM_TOP = 1
    LEFT_RIGHT = 2
    RIGHT_LEFT = 3

    def get_movement(self):
        return {
            BackgroundMoveType.RIGHT_LEFT: MoveRight2Left,
            BackgroundMoveType.TOP_BOTTOM: MoveRight2Left,
            BackgroundMoveType.LEFT_RIGHT: MoveRight2Left,
            BackgroundMoveType.BOTTOM_TOP: MoveRight2Left,
        }[self]

    def get_positions(self, background):
        return {
            BackgroundMoveType.TOP_BOTTOM: (background.x, background.y - background.height),
            BackgroundMoveType.BOTTOM_TOP: (background.x, background.y + background.height),
            BackgroundMoveType.LEFT_RIGHT: (background.x - background.width, background.y),
            BackgroundMoveType.RIGHT_LEFT: (background.x + background.width, background.y),
        }[self]


class MoveRight2Left:

    def __init__(self, image1, image2, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image1 = image1
        self.image2 = image2

    def get_positions(self):
        return self.x + self.width, self.y

    def move(self, speed):
        self.image1.rect[0] = self.image1.x \
            if self.image1.rect[0] <= -self.width else self.image1.rect[0] - speed
        self.image2.rect[0] = self.image2.x \
            if self.image2.rect[0] <= self.image1.x else self.image2.rect[0] - speed


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
        self.movement = self.move_type.get_movement()(self.image1, self.image2, x, y, width, height)

    def get_image_position(self):
        result = {
            BackgroundMoveType.TOP_BOTTOM: (self.x, self.y - self.height),
            BackgroundMoveType.BOTTOM_TOP: (self.x, self.y + self.height),
            BackgroundMoveType.LEFT_RIGHT: (self.x - self.width, self.y),
            BackgroundMoveType.RIGHT_LEFT: (self.x + self.width, self.y),
        }[self.move_type]
        return result

    def move(self):
        self.movement.move(self.speed)

    def update(self):
        self.move()
