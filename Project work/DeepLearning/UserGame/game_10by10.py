import pygame
import random
from sys import exit
import config as cng
from player import Player
from wumpus import Wumpus
from gold import Gold
from pit import Pit

pygame.init()
screen = cng.SCREEN
clock = pygame.time.Clock()     #Clock that controls the frames per second

screen_w, screen_h = screen.get_size()
image_w, image_h = cng.BACKGROUND.get_size()

for x in range(0, screen_w, image_w):
    for y in range(0, screen_h, image_h):
        screen.blit(cng.BACKGROUND, (x, y))

color = cng.COLOR_INACTIVE

class Wumpus_World:
    def __init__(self):
        self.fps = cng.FPS


        
        self.caption = pygame.display.set_caption(cng.NAME_OF_GAME) #Sets game title at the top of the game window

    # Create the game board
    def draw_board(self):
        for row in range(cng.GRID_SIZE):
            for col in range(cng.GRID_SIZE):
                rect = pygame.Rect(col * cng.CELL_SIZE, row * cng.CELL_SIZE, cng.CELL_SIZE, cng.CELL_SIZE)
                pygame.draw.rect(screen, cng.WHITE, rect, 1)
    
    # A def that saves the score and the steps the player has taken
    def save_data(self):
        with open('score.txt', 'a') as score:
            data_array = []
            data_array.append(cng.PLAYER_TEXT)
            data_array.append(cng.SCORE)
            data_array.append(cng.PLAYER_STEPS)
            data_array.append(cng.ROUNDS)
            data_array.append(cng.GRID_SIZE)
            data_array.append(cng.WIN)
            data_array.append(cng.GOLDS)
            data_array.append(cng.KILLS)
            
            data = str(data_array)
            score.write("\n")
            score.write(data)

            
    # A function for the loading screen 
    def loading_screen(self):
        for x in range(4, cng.WINDOW_X, cng.IMAGE_W):
            for y in range(4, cng.WINDOW_Y, cng.IMAGE_H):
                screen.blit(cng.BACKGROUND, (x, y))


        font = pygame.font.Font(cng.FONT, 28)                                       #Creates the font and the font size, using a ttf font document
        text = font.render("WELCOME TO WUMPUS WORLD!", 1, cng.PINK)                          #Creates the text using the font over
        screen.blit(text, (cng.WINDOW_X // 2 - text.get_width() // 2, 140))             #Sets the location of the text on the screen
        fontTwo = pygame.font.Font(cng.FONT, 20)                                    #Creates the font and the font size, using a ttf font document 
        textTwo = fontTwo.render("Write your name in the box under", 1, cng.WHITE)
        #Create the text using the font over
        screen.blit(textTwo,(cng.WINDOW_X // 2 - textTwo.get_width() // 2, 180))
        
        textThree = fontTwo.render("Press SPACE to start the game", 1, cng.WHITE)
        screen.blit(textThree,(cng.WINDOW_X // 2 - textThree.get_width() // 2, 280))


        #Loop that gives the player the choice to start the game by pressing space
        #If player hits space, we will exit the loop
        active = False
        starting = True
        while starting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        starting = False
                    if event.key == pygame.K_ESCAPE:
                        exit()
                    if event.key == pygame.K_BACKSPACE:
                        cng.PLAYER_TEXT = cng.PLAYER_TEXT[:-1]


                        
                    else:
                        cng.PLAYER_TEXT += event.unicode

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if cng.PLAYER_INPUT_RECT.collidepoint(event.pos):
                        active = True
                    else:
                        active = False
            
            if active:
                color = cng.COLOR_ACTIVE
            else:
                color = cng.COLOR_INACTIVE
            
            pygame.draw.rect(screen, color, cng.PLAYER_INPUT_RECT, 2)
            text_surface = pygame.font.Font(cng.FONT, 20).render(cng.PLAYER_TEXT, True, color)
            screen.blit(text_surface, (cng.PLAYER_INPUT_RECT.x + 5, cng.PLAYER_INPUT_RECT.y + 5))
            
            pygame.display.flip()
            clock.tick(cng.FPS)
        self.run()

    def pause_screen(self):
        for x in range(0, cng.WINDOW_X, cng.IMAGE_W):
            for y in range(0, cng.WINDOW_Y, cng.IMAGE_H):
                screen.blit(cng.BACKGROUND, (x, y))

        font = pygame.font.Font(cng.FONT, 30)                                       
        text = font.render("GAME PAUSED!", 1, cng.WHITE)                                
        screen.blit(text, (cng.WINDOW_X // 2 - text.get_width() // 2, 120))             
        fontTwo = pygame.font.Font(cng.FONT, 20)                                    
        textTwo = fontTwo.render("Press space to continue the game", 1, cng.WHITE)      
        screen.blit(textTwo,(cng.WINDOW_X // 2 - textTwo.get_width() // 2, 180))        

        #Loop that gives the player the choice to start the game by pressing space
        #If player hits space, we will exit the loop
        pause = True
        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:     # Sets space as an unpause button
                        pause = False                   # Exits the pause screen and continues the game
                    if event.key == pygame.K_ESCAPE:
                        exit()
            pygame.display.update()
    
    def game_won_screen(self):
        for x in range(0, cng.WINDOW_X, cng.IMAGE_W):
            for y in range(0, cng.WINDOW_Y, cng.IMAGE_H):
                screen.blit(cng.BACKGROUND, (x, y))

        font = pygame.font.Font(cng.FONT, 30)                                       
        text = font.render("GAME WON!", 1, cng.PINK)                                
        screen.blit(text, (cng.WINDOW_X // 2 - text.get_width() // 2, 120))             
        fontTwo = pygame.font.Font(cng.FONT, 20)                                    
        textTwo = fontTwo.render("Press R to play the game again", 1, cng.WHITE)
        screen.blit(textTwo,(cng.WINDOW_X // 2 - textTwo.get_width() // 2, 180))
        textThree = fontTwo.render("Press ESC to exit the game", 1, cng.WHITE)
        screen.blit(textThree,(cng.WINDOW_X // 2 - textThree.get_width() // 2, 210))
        
        cng.ROUNDS += 1
        self.save_data()

        #Loop that gives the player the choice to start the game by pressing space
        #If player hits space, we will exit the loop
        pause = True
        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:     # Sets space as an unpause button
                        cng.SCORE = 1000
                        cng.PLAYER_STEPS = 0
                        cng.WIN = 0
                        cng.GOLDS = 0
                        cng.KILLS = 0
                        self.run()                   
                    if event.key == pygame.K_ESCAPE:
                        exit()
            pygame.display.update()
    
    def game_over_screen(self):
            
        for x in range(0, cng.WINDOW_X, cng.IMAGE_W):
            for y in range(0, cng.WINDOW_Y, cng.IMAGE_H):
                screen.blit(cng.BACKGROUND, (x, y))

        font = pygame.font.Font(cng.FONT, 30)                                       
        text = font.render("GAME OVER!", 1, cng.PINK)                                
        screen.blit(text, (cng.WINDOW_X // 2 - text.get_width() // 2, 120))             
        fontTwo = pygame.font.Font(cng.FONT, 20)                                    
        textTwo = fontTwo.render("Press R to restart the game", 1, cng.WHITE)
        screen.blit(textTwo,(cng.WINDOW_X // 2 - textTwo.get_width() // 2, 180))
        textThree = fontTwo.render("Press ESC to exit the game", 1, cng.WHITE)
        screen.blit(textThree,(cng.WINDOW_X // 2 - textThree.get_width() // 2, 210))
        
        cng.ROUNDS += 1
        self.save_data()

        #Loop that gives the player the choice to start the game by pressing space
        #If player hits space, we will exit the loop
        pause = True
        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:     # Sets space as an unpause button
                        cng.SCORE = 1000
                        cng.PLAYER_STEPS = 0
                        cng.WIN = 0
                        cng.GOLDS = 0
                        cng.KILLS = 0
                        self.run()                   
                    if event.key == pygame.K_ESCAPE:
                        exit()
            pygame.display.update()


    def score(self): 
        font = pygame.font.Font(cng.FONT, 25)
        score = font.render(f"SCORE: {cng.SCORE}", 1, cng.PINK)
        screen.blit(score, (10, 10))
    
    def steps(self): 
        font = pygame.font.Font(cng.FONT, 25)
        score = font.render(f"STEPS: {cng.PLAYER_STEPS}", 1, cng.BLUE)
        screen.blit(score, (200, 10))
    
    def arrow_remaining(self): 
        font = pygame.font.Font(cng.FONT, 25)
        score = font.render(f"ARROW: {self.player.ammo}/{cng.AMMO}", 1, cng.PURPLE)
        screen.blit(score, (160, cng.WINDOW_Y-40))
        
    def gold_counter(self): 
        font = pygame.font.Font(cng.FONT, 25)
        goldcount = font.render(f"GOLD: {self.player.gold}/{cng.NUMBER_OF_WUMPUS}", 1, cng.YELLOW)
        screen.blit(goldcount, (10, cng.WINDOW_Y-40))

    def run(self):
        # Set up the game

        
        all_sprites_list = pygame.sprite.Group()
        player_arrow = pygame.sprite.Group()
        cells_list = pygame.sprite.Group()
        
        self.player = Player(cng.PLAYER_IMAGE, 0, 0, "right", player_arrow, 1)
        all_sprites_list.add(self.player)
    
        
        breezes = []
        for i in range(cng.NUMBER_OF_PITS*4):
            self.breeze = Pit(cng.BREEZE_IMAGE)
            all_sprites_list.add(self.breeze)
            breezes.append(self.breeze)
            i += 1


        stenches = []
        for i in range(cng.NUMBER_OF_WUMPUS*4):
            self.stench = Pit(cng.STENCH_IMAGE)
            all_sprites_list.add(self.stench)
            stenches.append(self.stench)
            i += 1
            
        golds = []
        for i in range(cng.NUMBER_OF_WUMPUS):
            self.gold = Gold(cng.GOLD_IMAGE)
            all_sprites_list.add(self.gold)
            golds.append(self.gold)
            i += 1
        

        wumpuses = []
        for i in range(cng.NUMBER_OF_WUMPUS):
            self.wumpus = Wumpus(cng.WUMPUS_IMAGE)
            all_sprites_list.add(self.wumpus)
            wumpuses.append(self.wumpus)
            i += 1

        
        pits = []
        for i in range(cng.NUMBER_OF_PITS):
            self.pit = Pit(cng.PIT_IMAGE)
            all_sprites_list.add(self.pit)
            pits.append(self.pit)
            i += 1
            
        
        # Makes the cell that eventually will be removed as the player moves
        for row in range(cng.GRID_SIZE):
            for col in range(cng.GRID_SIZE):
                x = col * cng.CELL_SIZE
                y = row * cng.CELL_SIZE
                
                cell = pygame.sprite.Sprite()
                cell.image = pygame.Surface((cng.CELL_SIZE, cng.CELL_SIZE))
                cell.image.fill(cng.LIGHT_GRAY)
                cell.rect = pygame.Rect(x, y, cng.CELL_SIZE, cng.CELL_SIZE)
                
                cells_list.add(cell)


        # Sets random positions for the wumpus, gold and pit
        # Creates an array to represent the grid
        grid = []
        for row in range(cng.GRID_SIZE):
            grid.append([])
            for col in range(cng.GRID_SIZE):
                grid[row].append(0)
            

        
        # Sets position for the player
        self.player.row = 0
        self.player.col = 0
        
        # Puts player in the grid
        grid[self.player.row][self.player.col] = 1

        
        # Puts the wumpus the grid
        for wumpus in wumpuses:
            while grid[wumpus.row][wumpus.col] != 0 or wumpus.row == 0 and wumpus.col==0: 
                wumpus.row = random.randint(1, cng.GRID_SIZE - 1)  
                wumpus.col = random.randint(1, cng.GRID_SIZE - 1)
            grid[wumpus.row][wumpus.col] = 2
    
        # Puts the gold in the grid
        for gold in golds:
            while grid[gold.row][gold.col] != 0 or gold.row == 0 and gold.col == 0: 
                gold.row = random.randint(1, cng.GRID_SIZE - 1)
                gold.col = random.randint(1, cng.GRID_SIZE - 1)
            grid[gold.row][gold.col] = 3

          
        # Puts the pit in the grid
        for pit in pits:
            while grid[pit.row][pit.col] != 0 or pit.row == 0 and pit.col==0: 
                pit.row = random.randint(1, cng.GRID_SIZE - 1)
                pit.col = random.randint(1, cng.GRID_SIZE - 1)
            grid[pit.row][pit.col] = 4

                    
        for wumpus in wumpuses:
            for gold in golds:
                for pit in pits:
                    # Makes the wumpus, gold and pit not have the same position in the grid
                    while wumpus.row == gold.row and wumpus.col == gold.col \
                        or wumpus.row == pit.row and wumpus.col == pit.col \
                        or gold.row == pit.row and gold.col == pit.col:
                    
                        if wumpus.row == gold.row and wumpus.col == gold.col:
                            gold.row = random.randint(1, cng.GRID_SIZE - 1)
                            gold.col = random.randint(1, cng.GRID_SIZE - 1)
                    
                        if wumpus.row == pit.row and wumpus.col == pit.col:
                            pit.row = random.randint(1, cng.GRID_SIZE - 1)
                            pit.col = random.randint(1, cng.GRID_SIZE - 1)
                    
                        if gold.row == pit.row and gold.col == pit.col:
                            pit.row = random.randint(1, cng.GRID_SIZE - 1)
                            pit.col = random.randint(1 , cng.GRID_SIZE - 1)
            
        # Puts the breeze in the adjacent rooms of the pit in the grid
        adjacent_rooms_pit=[]
        for pit in pits:
            adjacent_rooms_pit.append((pit.row - 1, pit.col))   # Up
            adjacent_rooms_pit.append((pit.row + 1, pit.col))   # Down
            adjacent_rooms_pit.append((pit.row, pit.col - 1))   # Left
            adjacent_rooms_pit.append((pit.row, pit.col + 1))   # Right

        for breeze in breezes:
                    foundPos = False
                    for row, col in adjacent_rooms_pit:
                        if row >= 0 and row < cng.GRID_SIZE and col >= 0 and col < cng.GRID_SIZE:
                            grid[row][col] = 5
                            breeze.row = row
                            breeze.col = col
                            foundPos = True
                            adjacent_rooms_pit.remove((row, col))
                        if(foundPos == True):
                            break
                    if(foundPos == False):
                        breeze.kill()
                          

        # Puts the stench in the adjacent rooms of the wumpus in the grid
        # Puts the breeze in the adjacent rooms of the pit in the grid
        adjacent_rooms_wumpus=[]
        for wumpus in wumpuses:
            adjacent_rooms_wumpus.append((wumpus.row - 1, wumpus.col))   # Up
            adjacent_rooms_wumpus.append((wumpus.row + 1, wumpus.col))   # Down
            adjacent_rooms_wumpus.append((wumpus.row, wumpus.col - 1))   # Left
            adjacent_rooms_wumpus.append((wumpus.row, wumpus.col + 1))   # Right


        for stench in stenches:
                    foundPos = False
                    for row, col in adjacent_rooms_wumpus:
                        if row >= 0 and row < cng.GRID_SIZE and col >= 0 and col < cng.GRID_SIZE:
                            grid[row][col] = 5
                            stench.row = row
                            stench.col = col
                            foundPos = True
                            adjacent_rooms_wumpus.remove((row, col))
                        if(foundPos == True):
                            break
                    if(foundPos == False):
                        stench.kill()



        # Updates the grid with the new positions of the wumpus, gold, pit, breeze and stench
        grid[self.wumpus.row][self.wumpus.col] = 2
        grid[self.gold.row][self.gold.col] = 3
        grid[self.pit.row][self.pit.col] = 4        
        grid[self.breeze.row][self.breeze.col] = 5
        grid[self.stench.row][self.stench.col] = 6 
        


         # Main game loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:               # Sets escape as a pause button
                        pause = True 
                        self.pause_screen()

                    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        if not self.player.image == cng.PLAYER_IMAGE_L:
                            self.player.image = cng.PLAYER_IMAGE_L
                            self.player.direction = "left"
                        
                        else:
                            self.player.direction = "left"
                            prev_direction = self.player.direction
                            
                            if self.player.direction == "left" and prev_direction == "left":
                                self.player.col = max(0, self.player.col - 1)
                                cng.PLAYER_STEPS += 1
                                cng.SCORE -= 10
                                self.player.image = cng.PLAYER_IMAGE_L
                        
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        if not self.player.image == cng.PLAYER_IMAGE_R:
                            self.player.image = cng.PLAYER_IMAGE_R
                            self.player.direction = "right"
                        
                        else: 
                            self.player.direction = "right"
                            prev_direction = self.player.direction
                        
                            if self.player.direction == "right" and prev_direction == "right":
                                self.player.col = min(cng.GRID_SIZE - 1, self.player.col + 1)
                                cng.PLAYER_STEPS += 1
                                cng.SCORE -= 10
                                self.player.image = cng.PLAYER_IMAGE_R
                            
                    elif event.key == pygame.K_UP or event.key == pygame.K_w:
                        if not self.player.image == cng.PLAYER_IMAGE_UP:
                            self.player.image = cng.PLAYER_IMAGE_UP
                            self.player.direction = "up"
                        
                        else: 
                            self.player.direction = "up"
                            prev_direction = self.player.direction
                        
                            if self.player.direction == "up" and prev_direction == "up":
                                self.player.row = max(0, self.player.row - 1)
                                cng.PLAYER_STEPS += 1
                                cng.SCORE -= 10
                                self.player.image = cng.PLAYER_IMAGE_UP

                        
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        if not self.player.image == cng.PLAYER_IMAGE_DOWN:
                            self.player.image = cng.PLAYER_IMAGE_DOWN
                            self.player.direction = "down"

                        else: 
                            self.player.direction = "down"
                            prev_direction = self.player.direction
                        
                            if self.player.direction == "down" and prev_direction == "down":
                                self.player.row = min(cng.GRID_SIZE - 1, self.player.row + 1)
                                cng.PLAYER_STEPS += 1
                                cng.SCORE -= 10
                                self.player.image = cng.PLAYER_IMAGE_DOWN
                                

                    elif (self.player and event.type == pygame.KEYDOWN):
                        if event.key == pygame.K_SPACE and self.player.ammo>0:
                            self.player.shoot_arrow(self.player.direction, self.player.ammo)
                            self.player.ammo -=1

                    #Checks for collision when key is pressed and adds to the score
                    for gold in golds:
                        if gold != None:
                            if pygame.sprite.collide_mask(self.player, gold) and event.key == pygame.K_e:
                                cng.SCORE += 500
                                golds.remove(gold)
                                gold.destroy()
                                self.player.gold += 1
                                cng.GOLDS += 1
                        if self.player.gold == cng.NUMBER_OF_WUMPUS:
                            cng.WIN = 1
                            self.game_won_screen()

            # Checks for collision between objects and update the score
            if self.player != None:
                pygame.sprite.spritecollide(self.player, cells_list, True)
                for wumpus in wumpuses:
                    if wumpus != None:
                        if pygame.sprite.collide_mask(self.player, wumpus) and (self.player.row != 0 or self.player.col != 0):
                            self.player.kill()
                            self.player = None
                            cng.SCORE -= 500
                            cng.WIN == 0
                            self.game_over_screen()
            
            if self.player != None:
                pygame.sprite.spritecollide(self.player, cells_list, True)
                for pit in pits:
                    if pygame.sprite.collide_mask(self.player, pit) and (self.player.row != 0 or self.player.col != 0):
                        self.player.kill()
                        self.player = None
                        cng.SCORE -= 500
                        cng.WIN == 0
                        self.game_over_screen()

            for wumpus in wumpuses:
                if wumpus != None:
                    if pygame.sprite.spritecollideany(wumpus, player_arrow):
                        wumpuses.remove(wumpus)
                        wumpus.destroy()
                        cng.SCORE += 500
                        cng.KILLS += 1

            # Sets the background image onto the screen in tiles
            for x in range(0, cng.WINDOW_X, cng.IMAGE_W):
                for y in range(0, cng.WINDOW_Y, cng.IMAGE_H):
                    screen.blit(cng.BACKGROUND, (x, y))

            #Game logic
            # Update the sprites and draw the screen
            #cells_list.draw(screen)
            self.draw_board()
            all_sprites_list.draw(screen)
            all_sprites_list.update()
            cells_list.draw(screen)
            self.steps()
            self.score()
            self.arrow_remaining()
            self.gold_counter()
            player_arrow.draw(screen)
            player_arrow.update()
            pygame.display.flip()
            clock.tick(cng.FPS)

        # Clean up the game
        self.pause_screen()
        pygame.quit()

if __name__ == '__main__':
    game = Wumpus_World()
    game.loading_screen()