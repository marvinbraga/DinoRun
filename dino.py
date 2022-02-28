import pygame
from pygame.sprite import AbstractGroup

from core.animated_artefacts import AnimatedArtefact


class Dino(AnimatedArtefact):

    def __init__(self, *groups: AbstractGroup):
        x, y = 20, 170
        super().__init__(None, x, y, (1, 2), *groups)
        self.width, self.height = 44, 48
        self.jump = self.load_jump()
        self.tick_limit = 8

        self.run_images = self.load_run()
        self.duck_images = self.load_duck()
        self.images = self.run_images

        self.gravity = -0.25
        self.up = 7

        self.is_ducking = False
        self.is_jumping = False

    def load_jump(self):
        self.load_image("sprites/dino_.png", self.x, self.y)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        return self.image.copy()

    def load_run(self):
        self.load_images(["sprites/dino_1.png", "sprites/dino_2.png"]).adjust_images(self.width, self.height)
        return self.images.copy()

    def load_duck(self):
        self.load_images(
            ["sprites/dino_ducking1.png", "sprites/dino_ducking2.png"]).adjust_images(self.width, self.height)
        return self.images.copy()
