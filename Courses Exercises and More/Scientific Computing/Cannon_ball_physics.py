''' Cannon game: First Assignment 1 for Scientific Computing at Roskilde University
Author: Vladyslav Horbatenko, vladyslav@ruc.dk

Program controles:
    Press q to quit,
          g to show/hide grid
          SPACE to shoot
          Mouse click to set new velocity
          r to reset rounds and wind velocity

Skeleton Authors: Maja H Kirkeby & Ulf R. Pedersen
'''

# Import modules
import pygame
import sys
import random
import math

# Initialize pygame
pygame.init()
pygame.font.init()

# Define colors 
BLACK = 0, 0, 0
WHITE = 255, 255, 255
BLUE = 0, 0, 255
RED = 255, 0, 0
GREEN = 0, 255, 0

# Define a frame rate
frames_per_second = 60

# Initialize real world parameters
g = 9.8   # Gravitational acceleration (m/s**2)
mass = 4  # Mass of projectile (kg)

# Set parameters for time
speedup = 7   # in order to reduce waiting time for impact we speed up by increasing the timestep
t = 0.0        # time in seconds
dt = (1 / frames_per_second)*speedup  # time increment in seconds


width = 2000.0   # Position of wall to the right and width of the coordinate system
height = 1000.0  # Height of the coordinate system
x_grid = 100 # the interval of x-axis grid of the coordinate system
y_grid = 100  # the interval of y-axis grid of the coordinate system

scale_real_to_screen = 0.5 # scale from the real-world to the screen-coordinate system


def convert(real_world_x, real_world_y, scale=scale_real_to_screen, real_world_height=height):
    ''' conversion from real-world coordinates to pixel-coordinates '''
    pixel_x = real_world_x*scale
    pixel_y = (real_world_height-real_world_y)*scale
    return int(pixel_x), int(pixel_y)


cannon_width, cannon_height = 20, 16
cannon1 = {"x": 200,
           "y": 0+cannon_height,
           "vx": 84.85,  # ≈ 120 m/s angle 45
           "vy": 84.85,  # ≈ 120 m/s angle 45
           "width": cannon_width,
           "height": cannon_height,
           "color": BLUE,
           'ball_radius': 7  # radius in meters
            }


# list of players
players = [cannon1]

def calc_init_ball_pos(cannon):
    ''' Finds the center of the cannon '''
    return cannon['x'] + cannon['width']/2, cannon['y'] - cannon['height']/2

def draw_cannon(surface, cannon):
    ''' Draw the cannon (the barrel will be the length of the initial velocity of the ball '''
    rect = (
        convert(cannon['x'], cannon['y']),
        (cannon['width']*scale_real_to_screen, cannon['height']*scale_real_to_screen)
    )
    pygame.draw.rect(surface, cannon['color'], rect)
    cannon_center = calc_init_ball_pos(cannon)
    line_from = convert(cannon_center[0], cannon_center[1])
    line_to = convert(cannon_center[0]+cannon['vx']*scale_real_to_screen, cannon_center[1]+cannon['vy']*scale_real_to_screen)
    line_width = 3
    pygame.draw.line(surface, cannon['color'], line_from, line_to, line_width)

    
def is_inside_field(real_world_x, real_world_y, field_width=width):
    ''' Return true if input is within world '''
    # Note: there is no ceiling
    return 0 < real_world_x < field_width and real_world_y > 0

# Create PyGame screen:
# 1. specify screen size
screen_width, screen_height = int(width*scale_real_to_screen), int(height*scale_real_to_screen)
# 2. define screen
screen = pygame.display.set_mode((screen_width, screen_height))
# 3. set caption
pygame.display.set_caption("Shooting game with pygame")
# Update pygames clock use the framerate
clock = pygame.time.Clock()


def draw_grid(surface, color, real_x_grid, real_y_grid, real_width=width, real_height=height):
    ''' Draw real-world grid on screen '''
    # vertical lines
    for i in range(int(real_width / real_x_grid)):
        pygame.draw.line(surface, color, convert(i * real_x_grid, 0),  convert(i * real_x_grid, real_height))
    # horisontal lines
    for i in range(int(real_height / y_grid)):
        pygame.draw.line(surface, color, convert(0 , i * real_y_grid ), convert(real_width, i * real_y_grid))


# Initialize game loop variables
running = True
game_end = False
shooting = False
show_grid = True
D = 0.47 #coefficient of friction
turn = 0 
turns = 1
wind_vel_x = random.randint(-15,15) #random value from -15 to 15 for wind
wind_vel_y = 0

# Initialize projectile values (see also function below)
x, y = calc_init_ball_pos(players[turn])
vx = players[turn]['vx']  # x velocity in meters per second
vy = players[turn]['vy']  # y velocity in meters per second
ball_color = players[turn]['color']
ball_radius = players[turn]['ball_radius']

#making round counter function
def turn_counter():
    turns_font = pygame.font.SysFont('Arial Black', 32)
    turns_text = turns_font.render(f'Round: {str(turns)}', True, WHITE)
    screen.blit(turns_text, (20,20))


def change_player():
    ''' initialize the global variables of the projectile to be those of the players cannon '''
    
    global players, turn, x, y, vx, vy, ball_color, ball_radius, wind_vel_x, shooting
    turn = (turn + 1) % len(players)   # will rotate through the list of players
    x, y = calc_init_ball_pos(players[turn])
    vx, vy = players[turn]['vx'], players[turn]['vy']
    ball_color = players[turn]['color']
    ball_radius = players[turn]['ball_radius']
    wind_vel_x = random.randint(-15, 15) #generating random int value of wind between -15 and 15 for each new round and player

def arrow(): #making function to draw an wind arrow and show wind value
    global wind_vel_x
    #drawing arrow for each round
    x = 300
    y = 225 
    status = WHITE #setting standart color for arrow
    x_rect_cor = x+wind_vel_x*10 #x ending coordinate for line 
    
    #adding polygon to the end coordinates, to make arrow shape
    #to set polygon we need three coordinates, which we'll determine from line ending coordinates
    foundation_1 = y + 15 
    foundation_2 = y - 15

    #changing direction of arrow (which direction it looks when drawing polygon in the "end point" of the line)
    if x_rect_cor < x:
        top_cor = x_rect_cor - 17
        status = RED #changing arrow color depending on direction
    else:
        top_cor = x_rect_cor +  17
        status = GREEN
    pygame.draw.line(screen,status, (x, y), (x_rect_cor, y), 10)
    
    pygame.draw.polygon(screen,status, 
                    [[x_rect_cor, foundation_1],[x_rect_cor, foundation_2],[top_cor, y]])

    #adding text visualization of wind (what is it equal to)
    wind_font = pygame.font.SysFont('Arial Black Light', 20)
    wind_text = wind_font.render(f'Wind is: {str(wind_vel_x)}', True, WHITE)
    screen.blit(wind_text, (top_cor,foundation_2-30))


def velocity_mouse(): #setting up velocity from mouse position
    global vx, vy, cannon1
    mouse_coordinates = pygame.mouse.get_pos() #getting position of mouse in pixels
    mouse_x = mouse_coordinates[0] / scale_real_to_screen #converting to real world coordinates
    mouse_y = height - mouse_coordinates[1] / scale_real_to_screen
    
    #changing velocities
    vx = mouse_x - cannon1['x']
    vy = mouse_y - cannon1['y']
    
    cannon1["vx"] = vx #updating values in draw_cannon() 
    cannon1["vy"] = vy
            


def ending(): #making ending screen
    if game_end:    
        end_screen_font = pygame.font.SysFont('Arial Black', 48)
        end_screen_font_small = pygame.font.SysFont('Arial Black', 24)
        end_screen_text = end_screen_font.render(f'GAME FINISHED', True, WHITE)
        end_screen_text_r = end_screen_font_small.render(f'If You want to start again, press "R"', True, WHITE)
        end_screen_text_q = end_screen_font_small.render(f'If You want to quit the game, press "Q"', True, WHITE)
        screen.blit(end_screen_text, (280,190))
        screen.blit(end_screen_text_r, (255,260))
        screen.blit(end_screen_text_q, (245,300))
    

'''----------Game loop----------'''
while running:
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        '''------------keys------------'''
            #quiting game
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            running = False
            
            #showing grid
        if event.type == pygame.KEYDOWN and event.key == pygame.K_g:
            show_grid = not show_grid
            
            #shooting
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            shooting = True
            
            # velocity_mouse()
        if event.type == pygame.MOUSEBUTTONDOWN and shooting == False:
            velocity_mouse()
            
            #restart game
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            turns = 1
            game_end = not(game_end)
            wind_vel_x = random.randint(-15,15)
             


    # Check whether the ball is outside the field
    if not is_inside_field(x,y):
        change_player() # if there is only one player, the ball will restart at that players center
        shooting = not(shooting) #if ball out of field we stop shooting, and after will change round number


    screen.fill(BLACK)

    # convert the real-world coordinates to pixel-coordinates
    x_pix, y_pix = convert(x, y)
    ball_radius_pix = round(scale_real_to_screen * ball_radius)

    #all text and drawings
    if not(game_end):
        # draw grid
        if show_grid:
            draw_grid(screen, RED, x_grid, y_grid, width, height)

        # draw the player's cannon and text
        draw_cannon(screen, cannon1)

        # draw ball using the pixel coordinates
        pygame.draw.circle(screen, ball_color, (x_pix,y_pix), ball_radius_pix)

        arrow()
        turn_counter()

        # print time passed, position and velocity
        print(f"time: {t}, pos: ({x,y}), vel: ({vx,vy}, mouse pos:({x_pix},{y_pix}))")
    
    if shooting:
        
        #creating drag force Fdrag = -Dv where v  is velocity and D  is a coefficient of friction
        Fdrag_x = -D * (vx-wind_vel_x)
        Fdrag_y = -D * (vy-wind_vel_y)
    
        # update time passed, the projectile 's real-world acceleration, velocity,
        # position for the next time_step using the Leap-Frog algorithm
        t += dt

        # Apply force of gravitational acceleration
        Fx = Fdrag_x #adding all forces on x
        Fy = -mass*g + Fdrag_y

        # Compute acceleration
        ax = Fx/mass
        ay = Fy/mass

        # Update velocities from acceleration
        vx += ax*dt  
        vy += ay*dt 

        # Update positions from velocities
        x += vx * dt
        y += vy * dt

        if not is_inside_field(x,y): #checking if bullet in field, and counting rounds
            turns += 1
            
        if turns > 5: #displaying the end screen if game ends
            game_end = True
    else:
        pass
    
    ending()
    # Redraw the screen
    pygame.display.flip()

    # Limit the framerate (must be called in each iteration)
    clock.tick(frames_per_second)

# Close after the game loop
pygame.quit()
sys.exit()
