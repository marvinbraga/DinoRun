import pygame

from core.scene import Scene
from ground import Ground


class Game(Scene):

    def __init__(self):
        super().__init__()
        self.is_finished = False
        self.all_sprites = pygame.sprite.Group()
        self.all_grounds = pygame.sprite.Group()
        groups = (self.all_sprites, self.all_grounds)
        self.ground = Ground(*groups)

    def draw(self, window):
        self.all_sprites.draw(window)

    def update(self):
        self.all_sprites.update()
        self.ground.update()
