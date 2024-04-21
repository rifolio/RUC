import pygame
import random
pygame.init()

# Set up the display
WINDOW_SIZE = (400, 400)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Wumpus World")

# Define the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define the grid size
CELL_SIZE = 100
GRID_SIZE = 4

# Create the player sprite
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.row = 0
        self.col = 0

    def update(self):
        self.rect.x = self.col * CELL_SIZE
        self.rect.y = self.row * CELL_SIZE
        
class Wumpus(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("wumpus.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (CELL_SIZE, CELL_SIZE))
        self.rect = self.image.get_rect()
        self.row = 0
        self.col = 0
        
    def update(self):
        self.rect.x = self.col * CELL_SIZE
        self.rect.y = self.row * CELL_SIZE
        
class Pit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pit.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (CELL_SIZE, CELL_SIZE))
        self.rect = self.image.get_rect()
        self.row = 0
        self.col = 0
        
    def update(self):
        self.rect.x = self.col * CELL_SIZE
        self.rect.y = self.row * CELL_SIZE
        
class Gold(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("gold.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (CELL_SIZE, CELL_SIZE))
        self.rect = self.image.get_rect()
        self.row = 0
        self.col = 0
        
    def update(self):
        self.rect.x = self.col * CELL_SIZE
        self.rect.y = self.row * CELL_SIZE

# Create the game board
def draw_board():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, WHITE, rect, 1)

# Set up the game
player = Player()
wumpus = Wumpus()
gold = Gold()

all_sprites = pygame.sprite.Group()
all_sprites.add(player, wumpus, gold)

# makes a list of pairs of all possible positions
positions = [(row, col) for row in range(GRID_SIZE) for col in range(1, GRID_SIZE)]
random.shuffle(positions) # shuffles the positions

num_pits = 2
pits = []
# creates pits and assigns them to random positions from the list
for i in range(num_pits):
    pit = Pit()
    pit.row, pit.col = positions[i]
    pits.append(pit)
    all_sprites.add(pit)
    
# puts Wumpus on the num_pits+1th position and gold on num_pits+2nd position
wumpus.row, wumpus.col = positions[num_pits]
gold.row, gold.col = positions[num_pits+1]

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player.col = max(0, player.col - 1)
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player.col = min(GRID_SIZE - 1, player.col + 1)
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                player.row = max(0, player.row - 1)
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player.row = min(GRID_SIZE - 1, player.row + 1)

    # Update the sprites and draw the screen
    all_sprites.update()
    screen.fill(BLACK)
    draw_board()
    all_sprites.draw(screen)
    pygame.display.flip()

# Clean up the game
pygame.quit()
