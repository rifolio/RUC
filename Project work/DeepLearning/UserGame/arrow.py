import pygame
import config as cng

class Arrow(pygame.sprite.Sprite):
    def __init__(self, image, x, y, direction):
        super().__init__()
        self.image = image
        self.image = pygame.transform.scale(self.image, (cng.CELL_SIZE, cng.CELL_SIZE))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.direction = direction
        self.speed = cng.ARROW_SPEED

    def update(self):
        if self.direction == "left":
            self.rect.x -= self.speed
        elif self.direction == "right":
            self.rect.x += self.speed
        elif self.direction == "up":
            self.rect.y -= self.speed
        elif self.direction == "down":
            self.rect.y += self.speed

        # Remove arrow when it goes off screen
        #if self.rect.left > cng.SCREEN_X or self.rect.right < 0 or self.rect.top > cng.SCREEN_Y or self.rect.bottom < 0:
        #    self.kill()