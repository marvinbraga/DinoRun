from pygame.sprite import AbstractGroup

from core.animated_artefacts import AnimatedArtefact


class Enemy(AnimatedArtefact):
    
    def __init__(self, x, y, *groups: AbstractGroup):
        super().__init__("assets/enemy{}.png", x, y, (0, 3), *groups)
        self.tick_limit = 3
