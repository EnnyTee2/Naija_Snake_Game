#!/usr/bin/python3

# Naija Snake Python Game
import random
import time


# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the game window and snake section size
size_x = 650
size_y = 475

screen = pygame.display.set_mode((700, 540))

# Set up some colors
blue = (0, 0, 255)
red = (255, 30, 0)
black = (0, 0 ,0)
white = (255, 255, 255)
yellow = (255, 255, 102)
bg = (156, 234, 235)
snake_col = (242, 78, 2)
button = (232, 183, 2)


# Set game title
pygame.display.set_caption('Naija Snake')

# snake features
snake_len = 10
speed = 10
clock = pygame.time.Clock()


# font types and sizes
bold_font = pygame.font.SysFont(None, 50)
text_font = pygame.font.SysFont(None, 25)
score_font = pygame.font.SysFont("comicsansms", 35)


# Button objects
left_butt = pygame.Rect(5, 482, 100, 50)
right_butt = pygame.Rect(595, 482, 100, 50)


def draw(surf, color, obj, br=0):
    """ Draw the desired rectangle object """
    return pygame.draw.rect(surf, color, obj, border_radius=br)

def show_message(msg, color):
    """ Display a custom message on the screen """
    mssg = bold_font.render(msg, True, color)
    screen.blit(mssg, [(size_x/2) - 70, size_y/2])

def writer(txt, color, pos):
    """"
    Helps with text interlay, writing custom text on the surface
    txt - string
    color - tuple
    pos - list
    """
    text = text_font.render(txt, True, color)
    screen.blit(text, pos)
    
def food_pos_gen():
    """ generates a tuple with random positions for the snake food """
    x = round(random.randrange(50, size_x - snake_len) / 10.0) * 10.0
    y = round(random.randrange(50, size_y - snake_len) / 10.0) * 10.0
    return (x, y)

def xtend_snake(snake_length, snake_list):
    """ Increase the snake length according to initial length increments """
    for pos in snake_list:
        pygame.draw.rect(screen, snake_col, [pos[0], pos[1], snake_length, snake_length])
      
def main_loop():
    # Run until the user asks to quit
    running = True
    
    
    # Snake position, size and movement initialisers
    x_pos = 50
    y_pos = 60
    move_hor = 0
    move_ver = 0
    snake_len_list = []
    Snake_length = 1
    
    # generate food position
    food_pos = food_pos_gen()
    
    while running:

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Listen for key events and take desired action
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move_hor = -snake_len
                    move_ver = 0
                elif event.key == pygame.K_RIGHT:
                    move_hor = snake_len
                    move_ver = 0
                elif event.key == pygame.K_UP:
                    move_ver = -snake_len
                    move_hor = 0
                elif event.key == pygame.K_DOWN:
                    move_ver = snake_len
                    move_hor = 0

        # Game over if snake hits border
        if x_pos < (size_x-snake_len) and x_pos >= 50:
            x_pos += move_hor
        elif x_pos <= 50 or x_pos >= 640:
            running = False
        
        if y_pos < (size_y-snake_len) and y_pos >= 50:
            y_pos += move_ver
        elif y_pos <= 50 or y_pos >= 465:
            running = False


        # Fill the background with specified background color
        screen.fill(bg)

        # Draw Line for snake section
        pygame.draw.line(screen, blue, (50, 50), (size_x, 50))
        pygame.draw.line(screen, blue, (50, size_y), (size_x, size_y))
        pygame.draw.line(screen, blue, (50, 50), (50, size_y))
        pygame.draw.line(screen, blue, (size_x, 50), (size_x, size_y))

        # Button Section
        left = [35, 498]
        right = [619, 498]
        draw(screen, button, left_butt, br=14)
        writer("Menu", blue, left)
        draw(screen, button, right_butt, br=14)
        writer("Pause", red, right)

        # Create the food
        food = pygame.Rect(food_pos, (snake_len, snake_len))
        
        # Draw the food on the screen
        draw(screen, blue, food, br=3)

        # Create the snake head rect
        snake_Head = []
        snake_Head.append(x_pos)
        snake_Head.append(y_pos)
        snake_len_list.append(snake_Head)
        if len(snake_len_list) > Snake_length:
            del snake_len_list[0]
        
        # Game over when snake bites itself
        for x in snake_len_list[:-1]:
            if x == snake_Head:
                time.sleep(2) # wait 2 seconds
                running = False

        # Extend the snake
        xtend_snake(snake_len, snake_len_list)
        
        # Write Scoreboard
        writer("Your Score: " + str(Snake_length - 1), snake_col, [20, 20])

        #update display
        pygame.display.update()
        #snake_head = pygame.Rect(x_pos, y_pos, snake_len, snake_len)

        ## Draw the snake on the screen
        #draw(screen, snake_col, snake_head)

        # Flip the display
        pygame.display.update()
        
        # Increase the snake Length scoreboard as it eats food and respawn the food in new position
        if (x_pos, y_pos) == food_pos:
            food_pos = food_pos_gen()
            Snake_length += 1

        # Increment the clock time
        clock.tick(speed)

    # show game-over message
    screen.fill(bg)
    show_message("Game Over", red)
    writer("Your Score: " + str(Snake_length - 1), blue, [(size_x/2) - 50, (size_y/2) + 60])
    pygame.display.update()
    time.sleep(5) # wait 5 seconds
        
    # Done! Time to quit.
    pygame.quit()
    quit()

main_loop()
