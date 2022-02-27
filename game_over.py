import pygame.sprite

from core.artefacts import Artefact
from core.scene import Scene


class GameOver(Scene):

    def __init__(self):
        super().__init__()
        self.all_sprites = pygame.sprite.Group()
        self.background = Artefact("sprites/game_over.png", 0, 0, self.all_sprites)
        self.replay_button = Artefact("sprites/replay_button.png", 0, 0, self.all_sprites)
        self.logo = Artefact("sprites/logo.png", 100, 100, self.all_sprites)
