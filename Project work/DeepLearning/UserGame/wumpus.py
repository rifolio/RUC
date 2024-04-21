import pygame
import config as cng

class Wumpus(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image
        #self.image = pygame.image.load("wumpus.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (cng.CELL_SIZE, cng.CELL_SIZE))
        self.rect = self.image.get_rect()
        self.row = 0
        self.col = 0
        self.dead = False
        
    def update(self):
        self.rect.x = self.col * cng.CELL_SIZE
        self.rect.y = self.row * cng.CELL_SIZE
        
    def destroy(self):
        self.kill()