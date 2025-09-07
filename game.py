import pygame
from pygame.image import load
from pygame.display import update
from pygame.key import get_pressed
from pygame.mixer import Sound
from pygame.font import Font
from pygame.transform import rotozoom
from sys import exit
from movements import enable_quit_game
import time
from random import randint

pygame.init()

clock = pygame.Clock()

# DISPLAY
screen = pygame.display.set_mode((800, 400))
caption = pygame.display.set_caption('Game On!')

# MUSIC
pygame.mixer.music.load('audio\music.wav')
pygame.mixer.music.set_volume(0.01)
pygame.mixer.music.play(loops=-1)

# SKY
sky_surf = load('graphics\Sky.png').convert_alpha()
sky_rect = sky_surf.get_rect(topleft=(0, 0))
screen.blit(sky_surf, (0, 0))

# GROUND
ground_surf = load('graphics\ground.png').convert_alpha()
ground_rect = ground_surf.get_rect(topleft=sky_rect.bottomleft)

# PLAYER
player_x_pos = ground_rect.topleft[0] + 50
player_y_pos = ground_rect.topleft[1]
player_surf = load('graphics\Player\player_stand.png')
player_walk1_surf = load('graphics\Player\player_walk_1.png')
player_walk1_surf_flipped = pygame.transform.flip(
    player_walk1_surf, flip_x=True, flip_y=False)
player_walk2_surf = load('graphics\Player\player_walk_2.png')
player_walk2_surf_flipped = pygame.transform.flip(
    player_walk2_surf, flip_x=True, flip_y=False)
player_rect = player_surf.get_rect(midbottom=(player_x_pos, player_y_pos))
player_jump_surf = load('graphics\Player\jump.png')

# TEXT
text_font = Font('font\Pixeltype.ttf', size=50)

# VARIABLES/CONSTANTS
game_status = True
start_time = 0
pause_start_time = 0
pause_duration_time = 0

# EVENTS AND OBSTACLES
OBSTACLE_SPAWN = pygame.USEREVENT + 1
pygame.time.set_timer(OBSTACLE_SPAWN, 2500)
SNAIL_ANIMATION = pygame.USEREVENT+2
pygame.time.set_timer(SNAIL_ANIMATION, 200)
FLY_ANIMATION = pygame.USEREVENT+3
pygame.time.set_timer(FLY_ANIMATION, 200)

snail1_surf = load('graphics\snail\snail1.png')
snail2_surf = load('graphics\snail\snail2.png')
snail_animation = [snail1_surf, snail2_surf]
snail_surf = snail_animation[0]
fly1_surf = load('graphics\Fly\Fly1.png')
fly2_surf = load('graphics\Fly\Fly2.png')
fly_animation = [fly1_surf, fly2_surf]
fly_surf = fly_animation[0]
obstacle_rect_list = []


def obstacle_movement(obstacle_rect_list, speed=5):
    global obstacle_rect
    if obstacle_rect_list:
        for obstacle_rect in obstacle_rect_list:
            obstacle_rect.x -= speed
            if obstacle_rect.midbottom[1] == 300:
                screen.blit(snail_surf, obstacle_rect)
            else:
                screen.blit(fly_surf, obstacle_rect)

        obstacle_rect_list = [
            obstacle_rect for obstacle_rect in obstacle_rect_list if obstacle_rect.x > -100]
        return obstacle_rect_list
    else:
        return []


def obstacle_collision(player_rect, obstacle_rect_list):
    if obstacle_rect_list:
        for obstacle_rect in obstacle_rect_list:
            if player_rect.collidepoint(obstacle_rect.center):
                return False
    return True


def display_score():
    if pause_duration_time:
        game_time = pygame.time.get_ticks() - pause_duration_time
    else:
        game_time = pygame.time.get_ticks() - start_time

    print(f'{pause_duration_time}')
    time_surf = text_font.render(
        f'{int(game_time/1000)}', antialias=True, color='Black', bgcolor=None, wraplength=0)
    time_rect = time_surf.get_rect(midbottom=(400, 50))
    screen.blit(time_surf, time_rect)
    return game_time


def sound_button():
    button = Sound(r'audio\button.mp3')
    button.set_volume(0.2)
    button.play()


scale = 0
is_scaling = 'expand'


def text_animation(text: str, coordinates, color=(224, 176, 255), animate=False, size=1):
    global scale, is_scaling

    text_surf = text_font.render(
        text, antialias=False, color=color, bgcolor=None)

    if animate:
        print(f'Entered animate logic {is_scaling, {scale}}')
        if is_scaling == 'expand':
            scale += 0.015
            if scale >= 0.8:
                is_scaling = 'shrink'

        elif is_scaling == 'shrink':

            scale -= 0.015
            if scale <= 0.6:
                is_scaling = 'expand'

        text_surf = rotozoom(text_surf, 0, scale)
        text_rect = text_surf.get_rect(center=coordinates)
    else:
        text_surf = rotozoom(text_surf, 0, scale=size)
        text_rect = text_surf.get_rect(center=coordinates)

    screen.blit(text_surf, text_rect)


def obstacle_animation():
    global snail_surf, fly_surf
    for event in pygame.event.get():
        if event.type == SNAIL_ANIMATION:
            if snail_surf == snail_animation[0]:
                snail_surf = snail_animation[1]

            elif snail_surf == snail_animation[1]:
                snail_surf = snail_animation[0]

        if event.type == FLY_ANIMATION:
            if fly_surf == fly_animation[0]:
                fly_surf = fly_animation[1]

            elif fly_surf == fly_animation[1]:
                fly_surf = fly_animation[0]


while True:
    clock.tick(30)

    if game_status == "Pause":
        screen.fill((20, 70, 120))
        if not pause_start_time:
            pause_start_time = game_time

        # player
        player_zoomed_surf = rotozoom(player_surf, 0, 2)
        player_zoomed_rect = player_zoomed_surf.get_rect(center=(400, 200))
        screen.blit(player_zoomed_surf, player_zoomed_rect)

        text_animation(text='Press any Button to Start!',
                       color=(224, 176, 255), coordinates=(400, 350), animate=True)

        text_animation('Pixel Runner', color='White',
                       coordinates=(410, 80), animate=False)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                game_status = True
                print(f'pause start time {pause_start_time}')
                pause_end_time = pygame.time.get_ticks()
                print(f'pause end time {pause_end_time}')
                print(f'current game time {game_time}')
                pause_duration_time = pause_end_time - pause_start_time
                print(f'pause duration time {pause_duration_time}')
                pause_start_time = 0
                Sound('audio\exit_pause.mp3').play()

        enable_quit_game()
        update()

    elif game_status is False:
        obstacle_rect_list.clear()
        pause_duration_time = 0
        start_time = pygame.time.get_ticks()

        screen.fill((20, 70, 120))
        message_surf = Font(filename='font\Pixeltype.ttf', size=80).render(
            'Game Over!', antialias=True, color='Black', bgcolor='White', wraplength=0)
        message_rect = message_surf.get_rect(midtop=(400, 50))

        restart_surf = Font(filename='font\Pixeltype.ttf', size=50).render(
            'restart', antialias=True, color='Black', bgcolor='White', wraplength=0)
        restart_rect = restart_surf.get_rect(
            midtop=(message_rect.midbottom[0], message_rect.midbottom[1]+50))

        quit_surf = Font(filename='font\Pixeltype.ttf', size=50).render(
            'quit', antialias=True, color='Black', bgcolor='White', wraplength=0)
        quit_rect = quit_surf.get_rect(
            midtop=(message_rect.midbottom[0], message_rect.midbottom[1]+100))

        score_surf = Font(filename='font\Pixeltype.ttf', size=50).render(
            f'Score:{int(game_time/1000)}', antialias=True, color='Black', bgcolor='White', wraplength=0)
        score_rect = score_surf.get_rect(
            midtop=(message_rect.midbottom[0], message_rect.midbottom[1]+150))

        screen.blit(message_surf, message_rect)
        screen.blit(restart_surf, restart_rect)
        screen.blit(quit_surf, quit_rect)
        screen.blit(score_surf, score_rect)
        update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                print('X button pressed')
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN and restart_rect.collidepoint(pygame.mouse.get_pos()):

                sound_button()
                start_time = pygame.time.get_ticks()

                game_status = True

                player_x_pos = ground_rect.topleft[0] + 50
                player_y_pos = ground_rect.topleft[1]
                player_rect.midbottom = (player_x_pos, player_y_pos)

            if event.type == pygame.MOUSEBUTTONDOWN and quit_rect.collidepoint(pygame.mouse.get_pos()):

                sound_button()
                pygame.quit()
                exit()

    elif game_status is True:

        screen.blit(sky_surf, sky_rect)
        screen.blit(ground_surf, ground_rect)
        screen.blit(player_surf, player_rect)

        game_time = display_score()

        obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        game_status = obstacle_collision(player_rect, obstacle_rect_list)

        # INPUT HANDLER
        for event in pygame.event.get():
            if event.type == SNAIL_ANIMATION:
                if snail_surf == snail_animation[0]:
                    snail_surf = snail_animation[1]

                elif snail_surf == snail_animation[1]:
                    snail_surf = snail_animation[0]

            if event.type == FLY_ANIMATION:
                if fly_surf == fly_animation[0]:
                    fly_surf = fly_animation[1]

                elif fly_surf == fly_animation[1]:
                    fly_surf = fly_animation[0]

            if event.type == OBSTACLE_SPAWN:

                if randint(0, 2):
                    obstacle_rect_list.append(snail1_surf.get_rect(
                        midbottom=(randint(900, 1200), 300)))
                else:
                    obstacle_rect_list.append(fly1_surf.get_rect(
                        midbottom=(randint(900, 1200), randint(210, 250))))

            if event.type == pygame.QUIT:
                print('X button pressed')
                pygame.quit()
                exit()

            # KEYDOWN BLOCK
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:

                    if player_y_pos >= ground_rect.topleft[1]:
                        print('KEYDOWN AND SPACE')
                        Sound('audio\jump.mp3').play()
                        while player_y_pos >= 140:
                            clock.tick(30)
                            player_y_pos -= 10
                            player_rect.midbottom = (
                                player_x_pos, player_y_pos)
                            screen.blit(sky_surf, sky_rect)
                            screen.blit(player_jump_surf, player_rect)
                            display_score()
                            obstacle_rect_list = obstacle_movement(
                                obstacle_rect_list)
                            game_status = obstacle_collision(
                                player_rect, obstacle_rect_list)

                            obstacle_animation()

                            if game_status is False:
                                break
                            update()

                        else:
                            gravity = 1
                            print(f'Falling')
                            while player_y_pos < ground_rect.topleft[1]:
                                clock.tick(30)
                                player_y_pos += gravity
                                gravity += 1
                                player_rect.midbottom = (
                                    player_x_pos, player_y_pos)
                                screen.blit(sky_surf, sky_rect)
                                screen.blit(player_jump_surf, player_rect)
                                display_score()
                                obstacle_rect_list = obstacle_movement(
                                    obstacle_rect_list)
                                game_status = obstacle_collision(
                                    player_rect, obstacle_rect_list)

                                obstacle_animation()

                                if game_status is False:
                                    break

                                update()

                elif event.key == pygame.K_ESCAPE:
                    game_status = 'Pause'

            # KEYDOWN INPUTS

        if get_pressed()[pygame.K_w]:

            player_x_pos += 10
            player_rect.midbottom = player_x_pos, player_y_pos
            screen.blit(sky_surf, sky_rect)
            screen.blit(player_walk1_surf, player_rect)
            display_score()
            obstacle_movement(obstacle_rect_list, speed=1)

            temp = player_walk1_surf
            player_walk1_surf = player_walk2_surf
            player_walk2_surf = temp

        if get_pressed()[pygame.K_s]:

            player_x_pos -= 10
            player_rect.midbottom = player_x_pos, player_y_pos
            screen.blit(sky_surf, sky_rect)
            screen.blit(player_walk1_surf_flipped, player_rect)
            display_score()
            obstacle_movement(obstacle_rect_list, speed=1)

            temp = player_walk1_surf_flipped
            player_walk1_surf_flipped = player_walk2_surf_flipped
            player_walk2_surf_flipped = temp

        update()
