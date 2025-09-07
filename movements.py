import pygame
from pygame.display import update
from pygame.mixer import Sound


def enable_quit_game():
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print('X button pressed')
            pygame.quit()
            exit()


# def handle_jump(player_y_pos, player_x_pos, player_rect,
#                 ground_rect, sky_surf, sky_rect,
#                 player_jump_surf, screen, update_func):
#     """Handle player jump movement"""

#     if player_y_pos >= ground_rect.topleft[1]:
#         print('KEYDOWN AND SPACE')
#         Sound('audio/jump.mp3').play()

#         # Jump upwards
#         while player_y_pos >= 150:
#             player_y_pos -= 0.2
#             player_rect.midbottom = (player_x_pos, player_y_pos)

#             screen.blit(sky_surf, sky_rect)
#             screen.blit(player_jump_surf, player_rect)

#             print(f'Y POS {player_y_pos}')
#             update()

#         else:
#             print(f'Falling')

#             # Falling down
#             while player_y_pos <= ground_rect.topleft[1]:
#                 player_y_pos += 0.2
#                 player_rect.midbottom = (player_x_pos, player_y_pos)

#                 screen.blit(sky_surf, sky_rect)
#                 screen.blit(player_jump_surf, player_rect)

#                 print(f'Y POS {player_y_pos}')
#                 update()

#     return player_y_pos, player_rect
