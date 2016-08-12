"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import sys, pygame, random

# Define some colors
GREEN = (101, 255, 149)
RED = (232, 6, 98)
BLUE = (59, 143, 255)
BLUE2 = (112, 8, 255)

colors = [GREEN, RED, BLUE, BLUE2]

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
x_speed=random.randint(-10, 10)
y_speed=random.randint(-10, 10)

size = random.randint(20, 80)
xb = 700 - size
yb = 500 - size

x=100
y=100



# -------- MAIN PROGRAM LOOP -----------
while not done:
    
    
    # --- MAIN EVENT LOOP --------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if (x<xb and y<yb):
        x_speed = x_speed
        y_speed = y_speed
    if (x>=xb or x<size):
        x_speed = -x_speed
    if (y>=yb or y<size):
        y_speed = -y_speed
    
    x = x + x_speed
    y = y + y_speed


    # --- GAME LOGIC should go here

    screen.fill(GREEN)

    # SCREEN CODE:

    pygame.draw.circle(screen, random.choice(colors), [x, y], size)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
