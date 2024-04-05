# C
import pygame

COLOR_ORANGE = (255, 128, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 255, 128)

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'EXIT')
# W
WIN_WIDTH = 576
WIN_HEIGHT = 324

# E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {'Level1Bg0': 0,
                'Level1Bg1': 1,
                'Level1Bg2': 2,
                'Level1Bg3': 3,
                'Level1Bg4': 4,
                'Level1Bg5': 5,
                'Level1Bg6': 6,
                'Player1': 4.7,
                'Player2': 4.7,
                'Enemy1': 3.0,
                'Enemy2': 2
                }
# P
PLAYER_K_UP = {'Player1': pygame.K_UP,
               'Player2': pygame.K_w}

PLAYER_K_DOWN = {'Player1': pygame.K_DOWN,
                 'Player2': pygame.K_s}

PLAYER_K_RIGHT = {'Player1': pygame.K_RIGHT,
                  'Player2': pygame.K_d}

PLAYER_K_LEFT = {'Player1': pygame.K_LEFT,
                 'Player2': pygame.K_a}
