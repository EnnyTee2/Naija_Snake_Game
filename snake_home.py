# Naija Snake Python Game
import random

def food_pos_gen(a, b):
    return ()

# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the game window
size_x = 650
size_y = 475
screen = pygame.display.set_mode((700, 540))

# Set uup some colors
blue = (0, 0, 255)
red = (255, 0, 0)
black = (0, 0 ,0)
white = (255, 255, 255)
bg = (156, 234, 235)
snake = (242, 78, 2)
button = (232, 183, 2)

# Set game title
pygame.display.set_caption('Naija Snake')

# Run until the user asks to quit
running = True

# Position and movement initialisers
x_pos = 100
y_pos = 200
speed = 5

move_hor = 0
move_ver = 0

clock = pygame.time.Clock()

# Button objects
left_butt = pygame.Rect(5, 482, 100, 50)
right_butt = pygame.Rect(595, 482, 100, 50)

def draw(surf, color, obj, br=0):
    """ Draw the desired rectangle object """
    return pygame.draw.rect(surf, color, obj, border_radius=br)

while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Listen for key events and take desired action
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_hor = -speed
                move_ver = 0
            elif event.key == pygame.K_RIGHT:
                move_hor = speed
                move_ver = 0
            elif event.key == pygame.K_UP:
                move_ver = -speed
                move_hor = 0
            elif event.key == pygame.K_DOWN:
                move_ver = speed
                move_hor = 0

    # Make the snake continue in the headed direction
    # when it moves out of the screen border
    if x_pos < (size_x) and x_pos >= 50:
        x_pos += move_hor
    elif (x_pos >= size_x):
        x_pos = 50
    elif (x_pos < 50):
        x_pos = size_x-1

    if y_pos+5 < size_y and y_pos >= 50:
        y_pos += move_ver
    elif (y_pos+5 >= size_y):
        y_pos = 51
    elif (y_pos-10 <= 50):
        y_pos = size_y-1

    # Fill the background with black
    screen.fill(bg)
    
    # Snake section
    pygame.draw.line(screen, blue, (50,50), (650,50))
    pygame.draw.line(screen, blue, (50,475), (650,475))
    pygame.draw.line(screen, blue, (50,50), (50,475))
    pygame.draw.line(screen, blue, (650,50), (650,475))

    # Button Section
    draw(screen, button, left_butt, br=14)
    draw(screen, button, right_butt, br=14)

    # Create the snake head rect
    snake_head = pygame.Rect(x_pos, y_pos, 10, 10)
    
    # Draw the snake on the screen
    draw(screen, snake, snake_head, br=3)

    # Flip the display
    pygame.display.update()

    # Increment the clock time
    clock.tick(30)

# Done! Time to quit.
pygame.quit()
quit()
