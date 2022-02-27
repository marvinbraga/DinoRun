import os

import pygame.font


class Text:

    def __init__(self, value: str, size=30, color=(0, 0, 0)):
        self.color = color
        try:
            file_name = os.path.normpath("../assets/font/font.ttf")
            self.font = pygame.font.Font(file_name, size)
        except FileNotFoundError:
            self.font = pygame.font.SysFont(value, size)

        self.render = self.font.render(value, True, color)

    def draw(self, window, x=0, y=0):
        window.blit(self.render, (x, y))

    def update(self, value: str):
        self.render = self.font.render(value, False, self.color)
        return self
