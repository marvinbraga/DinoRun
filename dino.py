from abc import ABCMeta
from enum import Enum

import pygame
from pygame.sprite import AbstractGroup

from core.animated_artefacts import AnimatedArtefact


class DinoStatus(Enum):
    RUNNING = 0
    JUMPING = 1
    DUCKING = 2


class AbstractStatus(metaclass=ABCMeta):

    def __init__(self, dino, files):
        self.height = dino.height
        self.width = dino.width
        self.y = dino.y
        self.x = dino.x
        self.dino = dino
        self.images = self._load_images(files)

    def _load_images(self, files):
        images = AnimatedArtefact.load_images(files)
        return AnimatedArtefact.adjust_images(images, self.width, self.height)


class DinoRun(AbstractStatus):

    def __init__(self, dino):
        super().__init__(dino, ["sprites/dino_1.png", "sprites/dino_2.png"])


class DinoJump(AbstractStatus):
    _UP = 9
    _GRAVITY = -0.25
    _TIME = 0
    _BOTTOM_LIMIT = 170

    def __init__(self, dino):
        super().__init__(dino, ["sprites/dino_.png", "sprites/dino_.png"])
        self.sound = None

        self.gravity = self._GRAVITY
        self.up = self._UP
        self.time = self._TIME
        self.bottom_limit = self._BOTTOM_LIMIT

    def go(self):
        self.dino.y -= self.up
        if DinoStatus.JUMPING not in self.dino.status:
            self.dino.status.append(DinoStatus.JUMPING)
        if self.sound:
            self.sound.play()
        return self

    def update(self):
        self.check_jumping().set_complete()
        self.dino.rect[1] = self.dino.y

    def check_jumping(self):
        if self.dino.y < self.bottom_limit:
            self.up += self.gravity * self.time
            self.dino.y -= self.up
            self.time += 0.12
        return self

    def set_complete(self):
        if self.dino.y > self.bottom_limit:
            self.up = self._UP
            self.dino.y = self._BOTTOM_LIMIT
            self.time = self._TIME
            self.dino.status.remove(DinoStatus.JUMPING)
        return self


class DinoDuck(AbstractStatus):

    def __init__(self, dino):
        super().__init__(dino, ["sprites/dino_ducking1.png", "sprites/dino_ducking2.png"])

    def go(self):
        if DinoStatus.DUCKING not in self.dino.status:
            self.dino.status.append(DinoStatus.DUCKING)
        return self

    def set_complete(self):
        self.dino.status.remove(DinoStatus.DUCKING)
        return self


class Dino(AnimatedArtefact):

    def __init__(self, *groups: AbstractGroup):
        x, y = 20, 170
        super().__init__(None, x, y, (1, 2), *groups)
        self.width, self.height = 44, 48
        self.tick_limit = 8
        self.status = [DinoStatus.RUNNING]
        self.valid_keys = [pygame.K_SPACE, pygame.K_DOWN]

        self.jump = DinoJump(self)
        self.run = DinoRun(self)
        self.duck = DinoDuck(self)
        self.init_images()

    def init_images(self):
        self.image = self.jump.images[0]
        self.get_rect()
        self.images = self.run.images
        return self

    def check_keys(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.jump.go()
            elif event.key == pygame.K_DOWN:
                self.duck.go()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                self.duck.set_complete()

    def update(self):
        if DinoStatus.JUMPING in self.status:
            self.images = self.jump.images
            self.jump.update()
        elif DinoStatus.DUCKING in self.status:
            self.images = self.duck.images
        else:
            self.images = self.run.images
        super().update()

    def is_collide(self, group, kill=False):
        return pygame.sprite.spritecollide(self, group, kill)
