from pygame.sprite import AbstractGroup

from core.background_manager import Background, BackgroundMoveType


class Ground(Background):

    def __init__(self, *groups: AbstractGroup):
        image = "sprites/ground.png"
        x, y = 0, 200
        width, height = 1202, 0
        move_type = BackgroundMoveType.RIGHT_LEFT
        speed = 4
        super().__init__(image, x, y, width, height, move_type, speed, *groups)
