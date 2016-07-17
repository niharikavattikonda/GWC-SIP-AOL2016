"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Snow")


# Your SnowFlake class
'''
The SnowFlake contains:
A.) The attributes size and position.
    Size is the radius of the SnowFlake.
    Position is a 2 item list representing [x, y]
       which is the current position of the SnowFlake.
    Bonus: add an attribute named isWindy, which is a
       boolean value to indicate if there is wind.  It
       defaults to False.
B.) A constructor which sets the values of the attributes
    to the values in the parameters.
C.) A fall method, which takes in speed as a parameter.
    When the fall method is called, the position of the
    SnowFlake changes slightly, based on the speed.
D.) The draw method, which uses pygame to draw the
    SnowFlake, which is a circle.
'''

class Snowflake():
    def __init__(self, size, position):
        self.size = size
        self.position = position
        self.isWindy = False
    def fall(self, speed):
        self.position[1] += speed
        if self.isWindy == True:
            self.position[1] += 1
    def draw(self):
        pygame.draw.circle(screen, WHITE, self.position, self.size)
    def wind(self):
        self.isWindy = True

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Speed
speed = 3

# Snow List
snow_list = []
for item in range(random.randint(200,250)):
    snow_list.append(Snowflake(random.randint(5,8), [random.randint(0, 700), random.randint(0, 500)]))

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)

    # --- Drawing code should go here
    snow_list.append(Snowflake(random.randint(5,8), [random.randint(0, 700), random.randint(0, 10)]))

    if (random.randint(2, 4) == 3):
        for item in snow_list:
            item.fall(random.randint(1, 2))
            item.wind()
    
    for item in snow_list:
        item.fall(random.randint(1, 2))
        item.draw()
 
    # End Snow
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
