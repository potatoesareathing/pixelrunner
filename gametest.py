import pygame
from pygame.image import load
from pygame.font import Font
from pygame.display import set_mode
from pygame.display import update
from movements import enable_quit_game
from random import randint

pygame.init()
screen = set_mode((400, 400))


ANIMATION = pygame.USEREVENT+1
pygame.time.set_timer(ANIMATION, 50)
number = 1

surf = load(r'C:\Users\aaliy\OneDrive\Desktop\pixelart\rasengan\rasengan0.png')

while True:
    pygame.Clock().tick(60)
    screen.fill('red')

    for event in pygame.event.get():
        if event.type == ANIMATION:
            if number == 1:
                surf = load(
                    r'C:\Users\aaliy\OneDrive\Desktop\pixelart\rasengan\rasengan0.png')
                number = 2
            elif number == 2:
                surf = load(
                    r"C:\Users\aaliy\OneDrive\Desktop\pixelart\rasengan\rasengan1.png")
                number = 3
            elif number == 3:
                surf = load(
                    r"C:\Users\aaliy\OneDrive\Desktop\pixelart\rasengan\rasengan2.png")
                number = 4
            elif number == 4:
                surf = load(
                    r"C:\Users\aaliy\OneDrive\Desktop\pixelart\rasengan\rasengan3.png")
                number = 5
            if number == 5:
                surf = load(
                    r'C:\Users\aaliy\OneDrive\Desktop\pixelart\rasengan\rasengan2.png')
                number = 6
            elif number == 6:
                surf = load(
                    r"C:\Users\aaliy\OneDrive\Desktop\pixelart\rasengan\rasengan1.png")
                number = 7
            elif number == 7:
                surf = load(
                    r"C:\Users\aaliy\OneDrive\Desktop\pixelart\rasengan\rasengan0.png")
                number = 1

    screen.blit(surf, surf.get_rect(center=(200, 200)))

    enable_quit_game()
    update()
