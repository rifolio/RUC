'''---------------------------program_imports-------------------------------------'''
import pygame, random
import numpy as np
import sys


'''---------------------------setting constants-------------------------------------'''
col_new_fish = (0, 128, 255)
col_young_fish = (15,82,186) #blue
col_breeding_fish = (220,35,157)

col_new_bear = (150,75,0) #brown
col_young_bear = (165,113,78)
col_breeding_bear = (150,75,0)
col_starving_bear = (75,75,75)

col_new_plant =(0,255,0)
col_old_plant=(0,128,0)

col_meteorite_fall = (0,     0, 0) #oragne
col_meteorite_down = (204, 0, 0) #dark orange
col_meteorite_down2 = (255, 51, 51)
col_meteorite_down3 = (255, 102, 102)
col_meteorite_down4 = (255, 153, 153) 


col_empty = (213, 196, 161)
col_grid = (30, 30, 60)


FRAMES_PER_SECOND = 60
SPEED = 10
ID = 0  # to identify each animal uniquely (for checking correctness)


'''---------------------------initial_functions-------------------------------------'''
def new_ID():
    global ID
    currentID = ID
    ID += 1
    return currentID

# Fish initial definition
def new_fish():
    ID_fish = new_ID()
    age = 0
    status='new'
    without_food=0
    fish = {'type': 'fish', 'col':col_new_fish, 'ID': ID_fish, 'age': age,'without_food':without_food,'status':status}
    return fish

# Bear initial definition
def new_bear():
    ID_bear = new_ID()
    age = 0
    without_food=0
    status='new'
    bear = {'type': 'bear', 'col':col_new_bear, 'ID': ID_bear, 'age': age,'without_food':without_food,'status':status}
    return bear

# Plant initial definition
def new_plant():
    ID_plant = new_ID()
    age = 0
    status='new'
    plant = {'type': 'plant', 'col':col_new_plant, 'ID': ID_plant, 'age': age,'status':status}
    return plant

# Meteorite initial definition
def new_meteorite():
    ID_meteorite = new_ID()
    age = 0
    detonate = random.randint(1, 200)
    status = 'new'
    meteorite = {'type': 'meteorite', 'col':col_meteorite_fall, 'ID': ID_meteorite, 'age': age, 'status': status, 'detonate': detonate}
    return meteorite

# Empty cell initial definition
def empty():
    return {'type': 'empty'}

def init(dimx, dimy, fish, bear, plant, meteorite):
    """Creates a starting grid, of dimension dimx * dimy and inserts.
    The rest of the cells in the grid are filled with empty dictionaries. """

    content_list = []
    for i in range(fish):
        content_list.append(new_fish())
    for i in range(bear):
        content_list.append(new_bear())
    for i in range(plant):
        content_list.append(new_plant())
    for i in range(meteorite):
        content_list.append(new_meteorite()) 
    for i in range((dimx * dimy - fish - bear - plant - meteorite)):
        content_list.append(empty())
    random.shuffle(content_list)
    # typecast the into a numpy array and reshape the 1 dimensional array to dimx * dimy
    cells_array = np.array(content_list)
    cells = np.reshape(cells_array, (dimy, dimx)) # the shape information is given in an  odd order
    return cells



'''---------------------------getting_neighbors-------------------------------------'''
def get_neighbors(cur, r, c):
    #Computes a list with the neighbouring cell positions of (r,c) in the grid {cur}
    r_min, c_min = 0 , 0
    r_max, c_max = cur.shape
    r_max, c_max = r_max-1 , c_max-1 # it's off by one
    # r+1,c-1 | r-1,c  | r+1,c+1
    # --------|--------|---------
    # r  ,c-1 | r  ,c  | r  ,c+1
    # --------|--------|---------
    # r-1,c-1 | r+1,c  | r-1,c+1
    neighbours = []
    # r-1:
    if r-1 >= r_min :
        if c-1 >= c_min: neighbours.append((r-1,c-1))
        neighbours.append((r-1,c))  # c is inside cur
        if c+1 <= c_max: neighbours.append((r - 1, c+1))
    # r:
    if c-1 >= c_min: neighbours.append((r,c-1))
    # skip center (r,c) since we are listing its neighbour positions
    if c + 1 <= c_max: neighbours.append((r,c+1))
    # r+1:
    if r + 1 <= r_max:
        if c - 1 >= c_min: neighbours.append((r+1,c-1))
        neighbours.append((r+1, c))  # c is inside cur
        if c + 1 <= c_max: neighbours.append((r+1,c+1))
    return neighbours


def neighbour_empty_rest(cur,neighbours):
    # divide neighbours
    fish_neighbours =[]
    empty_neighbours =[]
    plant_neighbours=[]
    bear_neighbours=[]
    meteor_neighbours=[]
    for neighbour in neighbours:
        if cur[neighbour]['type'] == "fish":
            fish_neighbours.append(neighbour)
        elif cur[neighbour]['type'] == "plant":
            plant_neighbours.append(neighbour)
        elif cur[neighbour]['type'] == "bear":
            bear_neighbours.append(neighbour)
        elif cur[neighbour]['type'] == "meteorite":
            meteor_neighbours.append(neighbour)
        else:
            empty_neighbours.append(neighbour)

    return fish_neighbours, empty_neighbours, plant_neighbours, bear_neighbours, meteor_neighbours 


#RULES FOR ANIMALS AND OTHER
'''---------------------------plant_rules------------------------------------'''
plant_overcrowd=2

def plant_rules(cur,r,c,neighbour_empty, neighbour_plant):
    # implementing the plant rules
    if cur[r, c]['age']%2 == 0 and len(neighbour_empty) > 0: #if age is even and no neighbours
        new_pos = random.choice(neighbour_empty)
        cur[new_pos] = new_plant()
        neighbour_plant.append(new_pos)  
        neighbour_empty.remove(new_pos) 
    
    if (len(neighbour_plant) >= plant_overcrowd) or (cur[r, c]['age']>=5):
        cur[r, c] = empty()
            
    return cur


'''---------------------------fish_rules-------------------------------------'''
fish_overcrowd = 2

def fish_rules(cur,r,c,neighbour_fish, neighbour_empty, neighbour_plant):
    # implementing the fish rules
    
    #breeding
    if cur[r, c]['age'] >= 12 and len(neighbour_empty) > 0:
        new_pos = random.choice(neighbour_empty)
        cur[new_pos] = new_fish()
        neighbour_fish.append(new_pos)  
        neighbour_empty.remove(new_pos)
    
    #overcrowd
    if len(neighbour_fish) >= fish_overcrowd:
        cur[r, c] = empty()
    
    #eating
    if (len(neighbour_plant)>=1) and ( cur[r, c] != empty()):
        new_pos=random.choice(neighbour_plant)
        cur[r, c]['without_food']=0
        old_fish = cur[r, c]
        cur[new_pos] = old_fish
        cur[new_pos]['status']='new'
        cur[r, c] = empty()  
    
    #dying*   
    if (len(neighbour_plant)==0) and  (cur[r, c] != empty()):
        cur[r, c]['without_food'] += 1
        if cur[r, c]['without_food'] >= 15:
            cur[r, c] = empty()
        if len(neighbour_empty) > 0:
            new_pos = random.choice(neighbour_empty)
            old_fish = cur[r, c]
            cur[new_pos] = old_fish
            cur[new_pos]['status']='new'
            cur[r, c] = empty()


    
    return cur


'''---------------------------bear_rules-------------------------------------'''
bear_overcrowd = 2

def bear_rules(cur,r,c,neighbour_bear, neighbour_empty, neighbour_fish):
    # implementing the bear rules
    
    #breeding
    if cur[r, c]['age'] >= 8 and len(neighbour_empty) > 0  and cur[r,c]['without_food'] < 8: #need to eat food again to breed one more time
        new_pos = random.choice(neighbour_empty)
        cur[new_pos] = new_bear()
        neighbour_bear.append(new_pos)  
        neighbour_empty.remove(new_pos) 
    
    #overcrowd
    if len(neighbour_bear) >= bear_overcrowd:
        cur[r, c] = empty()

    #eating
    if (len(neighbour_fish)>=1) and (cur[r, c] != empty()):
        new_pos=random.choice(neighbour_fish)
        cur[r, c]['without_food']=0
        old_bear = cur[r, c]
        cur[new_pos] = old_bear
        cur[new_pos]['status']='new'
        cur[r, c] = empty()  
               
    #dying 
    if (len(neighbour_fish)==0) and (cur[r, c] != empty()):
        cur[r, c]['without_food'] += 1
        if cur[r, c]['without_food']==10:
            cur[r, c] = empty()
        elif len(neighbour_empty) > 0:
            new_pos = random.choice(neighbour_empty)
            old_bear_2 = cur[r, c]
            cur[new_pos] = old_bear_2
            cur[new_pos]['status']='new'
            cur[r, c] = empty()
    return cur


'''---------------------------meteorite_neighbors-------------------------------------'''

def get_meteor_neighbors(cur, r, c): #collecting data baout neighbour in nearest 2 cells range
    r_min, c_min = 0 , 0
    r_max, c_max = cur.shape
    r_max, c_max = r_max-1 , c_max-1 # it's off by one
    
    neighbours2 = []
    # r-1:
    if r-1 >= r_min :
        if c-1 >= c_min: neighbours2.append((r-1,c-1))
        neighbours2.append((r-1,c))  # c is inside cur
        if c+1 <= c_max: neighbours2.append((r - 1, c+1))
        if c-2 >= c_min: neighbours2.append((r-1,c-2))
        if c+2 <= c_max: neighbours2.append((r - 1, c+2))
    # r:
    if c-1 >= c_min: neighbours2.append((r,c-1))
    # skip center (r,c) since we are listing its neighbour positions
    if c + 1 <= c_max: neighbours2.append((r,c+1))
    if c + 2 <= c_max: neighbours2.append((r,c+2))
    if c - 2 <= c_max: neighbours2.append((r,c-2))
    # r+1:
    if r + 1 <= r_max:
        if c - 1 >= c_min: neighbours2.append((r+1,c-1))
        neighbours2.append((r+1, c))  # c is inside cur
        if c + 1 <= c_max: neighbours2.append((r+1,c+1))
        if c - 2 >= c_min: neighbours2.append((r+1,c-2))
        if c + 2 >= c_min: neighbours2.append((r+1,c+2))
    return neighbours2


'''---------------------------meteorite_rules-------------------------------------'''
def meteorite_rules(cur,r,c):    
    
    apocalyptic_age = 45
    
    if cur[r,c]['age'] < apocalyptic_age: #going through all neighbors and making this cells empty
        n = get_meteor_neighbors(cur,r,c)
        for i in range(len(n)):
            cur[n[i]] = empty()
            i += 1

    if speed_count//SPEED % apocalyptic_age == 0: #trying to make meteorite falls on random time
        apocalyptic_r = random.randint(4,25)
        apocalyptic_c = random.randint(4,56)
        r,c = apocalyptic_r, apocalyptic_c
        cur[r,c] = new_meteorite()
        
    if cur[r, c]['age'] >= apocalyptic_age: #making cell itself empty 
        cur[r, c] = empty()

    return cur


'''---------------------------updating_variables-------------------------------------'''
def update(surface, cur, sz):
    # for each cell
    for r, c in np.ndindex(cur.shape):
        # if there is a bear, fish, plant or meteorite
        if cur[r, c]['type'] == "fish" or cur[r, c]['type'] == "bear" or cur[r, c]['type'] == "plant" or cur[r,c]['type'] == "meteorite":
            if cur[r, c]['status']=='new':
                cur[r, c]['status']='old'
            else:            # calculate neighbours and find the empty and the fish neighbours (other bears are not important, currently)
                neighbours = get_neighbors(cur, r, c)
            
                neighbour_fish, neighbour_empty,neighbour_plant, neighbour_bear, neighbour_meteor = neighbour_empty_rest(cur, neighbours)

                # For checking the state of the animal or plant (correctness)
                print(f"Pos: ({r},{c}), Animal/Plant: {cur[r, c]}")
                # if it is a fish
                if cur[r, c]['type'] == "fish":
                    cur = fish_rules(cur, r, c, neighbour_fish, neighbour_empty,neighbour_plant)

                # if it is a bear
                elif cur[r, c]['type'] == "bear":
                    cur = bear_rules(cur, r, c, neighbour_bear, neighbour_empty, neighbour_fish)
                
                # if it is a plant
                elif cur[r, c]['type'] == "plant":
                    cur = plant_rules(cur, r, c, neighbour_empty,neighbour_plant)
                
                # if it is a meteorite
                elif cur[r, c]['type'] == "meteorite":
                    cur = meteorite_rules(cur,r,c)
# age update
    for r, c in np.ndindex(cur.shape):
        if cur[r, c]['type'] == "fish":
            cur[r, c]['age'] += 1
            if cur[r, c]['age']<12:
                cur[r,c]['col']=col_young_fish
            elif cur[r, c]['age']>=12:
                cur[r,c]['col']=col_breeding_fish
        elif cur[r, c]['type'] == "bear":
            cur[r, c]['age'] += 1
            if cur[r, c]['age']<8:
                cur[r,c]['col']=col_young_bear
            elif cur[r, c]['age']>=8:
                cur[r,c]['col']=col_breeding_bear
        elif cur[r, c]['type'] == "plant":
            cur[r, c]['age'] += 1
            if cur[r, c]['age']>3:
                cur[r,c]['col']=col_old_plant
        elif cur[r, c]['type'] == "meteorite":
            cur[r, c]['age'] += 1
            if cur[r, c]['age'] >= 10:
                cur[r,c]['col'] = col_meteorite_down
            if cur[r, c]['age'] >= 20:
                cur[r,c]['col'] = col_meteorite_down2
            if cur[r, c]['age'] >= 30:
                cur[r,c]['col'] = col_meteorite_down3
            if cur[r, c]['age'] >= 40:
                cur[r,c]['col'] = col_meteorite_down4
            
        cur[r, c]['status']='old'
            
    return cur


'''Given a grid {cur}, the size of the drawn cells, and a surface to draw on. Draw the'''
def draw_grid(surface,cur,sz):
    for r, c in np.ndindex(cur.shape):
        col = col_empty # if the cell is empty, the color should be that of "empty"
        if cur[r, c]['type'] != 'empty': # if the cell is not empty update the color according to its content
            col = cur[r, c]['col']
        pygame.draw.rect(surface, col, (c * sz, r * sz, sz - 1, sz - 1))



'''---------------------------main_game_function-------------------------------------'''
def main(dimx, dimy, cellsize,fish,bear,plant,meteorite):
    pygame.init()
    surface = pygame.display.set_mode((dimx * cellsize, dimy * cellsize))
    pygame.display.set_caption("Animal Kingdom")

    cells = init(dimx, dimy,fish,bear,plant,meteorite) # creates the grid representation
    draw_grid(surface, cells, cellsize)
    pygame.display.update()

    clock = pygame.time.Clock()
    global speed_count
    speed_count = 1
    running = True
    while running:
        # event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                running = False
                

        speed_count += 1
        surface.fill(col_grid)
        if(speed_count % SPEED == 0):   # slows down the time step without slowing down the frame rate
            # update grid
            print(f"timestep: {speed_count // SPEED}")
            cells = update(surface, cells, cellsize)
            
            
        # draw the updated grid
        draw_grid(surface, cells, cellsize)
        pygame.display.update()
        clock.tick(FRAMES_PER_SECOND)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    fish = 20
    bear = 10
    plant = 15
    meteorite = 5
    main(59, 30, 20,fish,bear,plant,meteorite)