import pygame

from cactus import CactusSize
from cloud import Cloud
from core.scene import Scene
from dino import Dino
from ground import Ground
from ptera import Ptera


class Game(Scene):

    def __init__(self):
        super().__init__()
        self.is_finished = False
        self.all_sprites = pygame.sprite.Group()
        self.all_grounds = pygame.sprite.Group()
        self.all_clouds = pygame.sprite.Group()
        self.all_cactus = pygame.sprite.Group()
        self.all_ptera = pygame.sprite.Group()
        self.all_enemies = pygame.sprite.Group()
        self.all_players = pygame.sprite.Group()
        self.ground = Ground(self.all_sprites, self.all_grounds)

        self.ADD_CLOUD = pygame.USEREVENT + 1
        pygame.time.set_timer(self.ADD_CLOUD, 3000)
        self.ADD_CACTUS = pygame.USEREVENT + 2
        pygame.time.set_timer(self.ADD_CACTUS, 2000)
        self.ADD_PTERA = pygame.USEREVENT + 3
        pygame.time.set_timer(self.ADD_PTERA, 5000)

        self.create_clouds()
        self.create_cactus()
        self.create_ptera()
        self.player = Dino(self.all_sprites, self.all_players)

    def check_events(self, event):
        if event.type == self.ADD_CLOUD:
            self.create_clouds()
        elif event.type == self.ADD_CACTUS:
            self.create_cactus()
        elif event.type == self.ADD_PTERA:
            self.create_ptera()

    def create_clouds(self, count=1):
        for i in range(count):
            Cloud(self.all_sprites, self.all_clouds)

    def create_cactus(self, count=1):
        for i in range(count):
            CactusSize.get_random_class()(self.all_sprites, self.all_cactus, self.all_enemies)

    def create_ptera(self, count=1):
        for i in range(count):
            Ptera(self.all_sprites, self.all_ptera, self.all_enemies)

    def draw(self, window):
        self.all_sprites.draw(window)

    def update(self):
        self.all_sprites.update()
        self.ground.update()
        self.player.update()
