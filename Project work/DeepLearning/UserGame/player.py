import pygame
from arrow import Arrow
import config as cng

class Player(pygame.sprite.Sprite):
    def __init__(self, image, row, col, direction, arrow_callback, ammo):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.row = row
        self.col = col
        self.direction = direction
        self.arrow_callback = arrow_callback
        self.score = cng.SCORE
        self.ammo = cng.AMMO
        self.gold = 0
    
    def update(self):
        self.rect.x = self.col * cng.CELL_SIZE
        self.rect.y = self.row * cng.CELL_SIZE
    
    def shoot_arrow(self, direction, ammo):
        img = cng.ARROW_IMAGE
        
        if self.direction != "right":
            img = pygame.transform.flip(img, True, False)
        if self.direction == "up":
            img = pygame.transform.flip(img, False, True)
        if self.direction == "down":
            img = pygame.transform.flip(img, False, True)
            

        if ammo > 0:
            arrow_callback = Arrow(img, self.rect.centerx, self.rect.centery, direction)
            self.arrow_callback.add(arrow_callback)