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
red = (255, 0, 0)
black = (0, 0 ,0)
white = (255, 255, 255)
bg = (156, 234, 235)
snake_col = (242, 78, 2)
button = (232, 183, 2)

# Set game title
pygame.display.set_caption('Naija Snake')

# snake features
snake_len = 10
speed = 5

# font type and size
bold_font = pygame.font.SysFont(None, 50)
text_font = pygame.font.SysFont(None, 10)



# Button objects
left_butt = pygame.Rect(5, 482, 100, 50)
right_butt = pygame.Rect(595, 482, 100, 50)

def draw(surf, color, obj, br=0):
    """ Draw the desired rectangle object """
    return pygame.draw.rect(surf, color, obj, border_radius=br)

def show_message(msg, color):
    """ Display a custom message on the screen """
    mssg = bold_font.render(msg, True, color)
    screen.blit(mssg, [size_x/2, size_y/2])

def writer(txt, color, pos):
    """"
    Helps with text interlay, writing custom text
    txt - string
    color - tuple
    pos - list
    """
    text = text_font.render(txt, True, color)
    screen.blit(text, pos)
    
def food_pos_gen():
    """ generates a tuple with random positions for the snake food """
    x = random.randrange(0, size_x - snake_len) / 10.0) * 10.0
    y = random.randrange(0, size_y - snake_len) / 10.0) * 10.0
    return (x, y)

def xtend_snake(snake_len, snake_list):
    """ Increase the snake length according to initial length increments """
    for pos in snake_list:
        pygame.draw.rect(screen, snake_col, [pos[0], pos[1], snake_len, snake_len])

clock = pygame.time.Clock()
        
def main_loop():
    # Run until the user asks to quit
    running = True
    closed = False
    
    # Snake position, size and movement initialisers
    x_pos = size_x / 2
    y_pos = size_y / 2
    move_hor = 0
    move_ver = 0
    snake_len_list = []
    snake_len = 10
    
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

        # Game over when snake bites itself
        #if x_pos in snake_pos or y_pos in snake_pos:
        #    running = False

        # Fill the background with specified background color
        screen.fill(bg)

        # Draw Line for snake section
        pygame.draw.line(screen, blue, (50, 50), (size_x, 50))
        pygame.draw.line(screen, blue, (50, size_y), (size_x, size_y))
        pygame.draw.line(screen, blue, (50, 50), (50, size_y))
        pygame.draw.line(screen, blue, (size_x, 50), (size_x, size_y))

        # Button Section
        left = [5, 452]
        right = [595, 452]
        draw(screen, button, left_butt, br=14)
        writer("Menu", blue, left)
        draw(screen, button, right_butt, br=14)
        writer("Pause", red, right)
        

        # Create the snake head rect
        snake_head = pygame.Rect(x_pos, y_pos, snake_len, snake_len)

        # Draw the snake on the screen
        draw(screen, snake_col, snake_head, br=3)

        # Flip the display
        pygame.display.update()
        
        if (x_pos, y_pos) == food_pos:
            print("SWALLOWED")

        # Increment the clock time
        clock.tick(speed)

# show game-over message
show_message("Game Over", red)
pygame.display.update()
time.sleep(5)    
    
# Done! Time to quit.
pygame.quit()
quit()
