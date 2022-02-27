from abc import ABCMeta, abstractmethod

import pygame

from core import settings


class AbstractGameLoop(metaclass=ABCMeta):

    def __init__(self, width, height, title):
        pygame.init()
        self.window = pygame.display.set_mode([width, height])
        self.title = title
        pygame.display.set_caption(self.title)
        self.fps = pygame.time.Clock()

        self.loop = True
        self._valid_keys = []

    def add_valid_key(self, *keys):
        for key in keys:
            self._valid_keys.append(key)
        return self

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def check_keys(self, event):
        pass

    @abstractmethod
    def check_events(self, event):
        pass

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.loop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.loop = False
                if event.key in self._valid_keys:
                    self.check_keys(event)
            elif event.type == pygame.KEYUP:
                if event.key in self._valid_keys:
                    self.check_keys(event)
            else:
                self.check_events(event)

    def update(self):
        pygame.mixer.init()
        try:
            while self.loop:
                self.fps.tick(settings.FPS)
                self.draw()
                self.events()
                pygame.display.update()
        finally:
            # pygame.mixer.music.stop()
            pygame.mixer.quit()
            pygame.quit()
