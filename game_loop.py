import pygame

from core.abstract_game_loop import AbstractGameLoop
from game import Game
from game_over import GameOver


class GameLoop(AbstractGameLoop):

    def __init__(self, width, height, title, background_color=(0, 0, 0)):
        super().__init__(width, height, title, pygame.image.load("sprites/dino_.png"), background_color)
        self.game = Game()
        self.background_color = self.game.background_color
        self.game_over = GameOver()
        self.add_valid_key(*self.game.valid_keys)

    def draw(self):
        pygame.display.set_icon(self.icon)
        self.game.draw(self.window)
        self.game.update()
        self.loop = not self.game.is_finished
        # self.game_over.draw(self.window)
        # self.game_over.update()

    def check_keys(self, event):
        self.game.check_keys(event)

    def check_events(self, event):
        self.game.check_events(event)
