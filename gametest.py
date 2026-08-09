import pygame
from pygame.image import load
from pygame.font import Font
from pygame.display import set_mode
from pygame.display import update
from random import randint
import sys
pygame.init()
screen = set_mode((400, 400))


class Player:

    def __init__(self):
        self.surf = load(r'graphics\Player\jump.png')
        self.rect = self.surf.get_rect(midbottom=(200, 300))
        self.gravity = -20

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom <= 300:
            self.gravity += 1
            self.rect.y += self.gravity
            if self.rect.bottom >= 300:
                self.rect.bottom = 300
        else:
            self.gravity = -20


player = Player()

while True:
    pygame.Clock().tick(60)
    screen.fill('red')

    for event in pygame.event.get():
        print(f'{event}')
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    player.player_input()

    update()
