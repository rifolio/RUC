import pygame
from pygame.math import Vector2 

pygame.init()

# GENERAL SETTINGS

'''------ CHANGE ONLY THIS HERE ------'''
GRID_SIZE = 4
'''------ CHANGE ONLY THIS HERE ------'''

# Sets screen - size is set based on grid size

BACKGROUND = pygame.image.load("background.png")
IMAGE_W = 120
IMAGE_H = 120

NAME_OF_GAME = "Wumpus World"
FPS = 60

FONT = "slkscr.ttf"

SCORE = 1000

WIN = 0
GOLDS = 0
KILLS = 0

ROUNDS = 0

# COLORS 
COLOR = [PINK, LIGHT_BLUE, BLUE, PURPLE, LIGHT_GRAY, GRAY, WHITE, BLACK, YELLOW] = [(255,105,180),(163, 227, 250),(0,191,255),(147,112,219),(85, 85, 85), (51, 51, 51), (255, 255, 255), (0, 0, 0), (253, 253, 150)]
COLOR_ACTIVE = LIGHT_BLUE
COLOR_INACTIVE = BLUE

# Define the grid size

if GRID_SIZE == 4:
    NUMBER_OF_PITS = 2
    NUMBER_OF_WUMPUS = 1
    NUMBER_OF_GOLD = 1
    WINDOW_X = 480
    WINDOW_Y = 480

if GRID_SIZE == 8:
    NUMBER_OF_PITS = 3
    NUMBER_OF_WUMPUS = 2  
    NUMBER_OF_GOLD = 2
    WINDOW_X = 600
    WINDOW_Y = 600
    
if GRID_SIZE == 10:
    NUMBER_OF_PITS = 4
    NUMBER_OF_WUMPUS = 3
    NUMBER_OF_GOLD = 3
    WINDOW_X = 750
    WINDOW_Y = 750`
    
if GRID_SIZE == 12:
    NUMBER_OF_PITS = 5
    NUMBER_OF_WUMPUS = 4 
    NUMBER_OF_GOLD = 4 
    WINDOW_X = 900
    WINDOW_Y = 900
    
SCREEN = pygame.display.set_mode((WINDOW_X, WINDOW_Y))
CELL_SIZE = WINDOW_X/GRID_SIZE

# PLAYER SETTINGS
PLAYER_IMAGE = pygame.image.load("agent_cat.png").convert_alpha()
PLAYER_IMAGE = pygame.transform.scale(PLAYER_IMAGE, (CELL_SIZE, CELL_SIZE))
PLAYER_IMAGE_R = pygame.image.load("agent_cat_right.png").convert_alpha()
PLAYER_IMAGE_R = pygame.transform.scale(PLAYER_IMAGE_R, (CELL_SIZE, CELL_SIZE))
PLAYER_IMAGE_L = pygame.image.load("agent_cat_left.png").convert_alpha()
PLAYER_IMAGE_L = pygame.transform.scale(PLAYER_IMAGE_L, (CELL_SIZE, CELL_SIZE))
PLAYER_IMAGE_UP = pygame.image.load("agent_cat_up.png").convert_alpha()
PLAYER_IMAGE_UP = pygame.transform.scale(PLAYER_IMAGE_UP, (CELL_SIZE, CELL_SIZE))
PLAYER_IMAGE_DOWN = pygame.image.load("agent_cat_down.png").convert_alpha()
PLAYER_IMAGE_DOWN = pygame.transform.scale(PLAYER_IMAGE_DOWN, (CELL_SIZE, CELL_SIZE))
PLAYER_DIRECTION = "right"
PLAYER_STEPS = 0
PLAYER_TEXT = ''
PLAYER_INPUT_RECT = pygame.Rect(((WINDOW_X/2))-(WINDOW_X/4), 224, (WINDOW_X/2), 32)


# ARROW SETTINGS
ARROW_IMAGE = pygame.image.load("arrow.png").convert_alpha()
ARROW_SPEED = 3
AMMO = NUMBER_OF_WUMPUS

WUMPUS_IMAGE = pygame.image.load("wumpus.png").convert_alpha()
GOLD_IMAGE = pygame.image.load("gold_bone.png").convert_alpha()
PIT_IMAGE = pygame.image.load("pit.png").convert_alpha()
BREEZE_IMAGE = pygame.image.load("breeze2.png").convert_alpha()
STENCH_IMAGE = pygame.image.load("stench2.png").convert_alpha()