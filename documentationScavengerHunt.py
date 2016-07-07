"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import sys, pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)



pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Bouncing Ball Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# WRITE YOUR CODE HERE
x_speed=3
y_speed=3

x=0
y=0

# -------- MAIN PROGRAM LOOP -----------
while not done:
    
    
    # --- MAIN EVENT LOOP --------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if (x<700 and y<500):
        x_speed = x_speed
        y_speed = y_speed
    if (x>=700 or x<0):
        x_speed = -x_speed
    if (y>=500 or y<0):
        y_speed = -y_speed
    
    x = x + x_speed
    y = y + y_speed


    # --- GAME LOGIC should go here

    screen.fill(WHITE)

    # SCREEN CODE:

    pygame.draw.circle(screen, BLUE, [x, y], 40)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
