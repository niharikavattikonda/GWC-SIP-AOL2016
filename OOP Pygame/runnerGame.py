# part 1.2
import pygame
import random

# part 1.4f
from scroller import Scroller as Scroller

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# part 1.3
pygame.init()
screen_width = 700
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])

# part 1.6a
any_scroller = Scroller(screen_width, 300, screen_height, (255, 100, 100), 3)

done = False

clock = pygame.time.Clock()

class RunnerSprite(pygame.sprite.Sprite):
    def __init__(self, color, size):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.size = size
        self.image = pygame.Surface(size)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = screen_width
        self.score = 0
        self.lives = 5
    def update(self):
        self.rect.x -= 4
        if self.rect.x <= 0:
            self.rect.y= random.randint(0, 500)
            self.rect.x = 700
    def check(self, sprites):
        removed_sprites = pygame.sprite.spritecollide(self, sprites, True)
        if sprites == good_sprites:
            for item in removed_sprites:
                self.score += 1
        elif sprites == bad_sprites:
            for item in removed_sprites:
                self.lives -= 1
        print("Score: " + str(self.score) + "  " + "Lives: " + str(self.lives))          

pixie = RunnerSprite(RED, [35, 25])
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(pixie)

good_sprites = pygame.sprite.Group()
bad_sprites = pygame.sprite.Group()

for i in range(100):
    new_good = RunnerSprite(BLUE, (35, 25))
    good_sprites.add(new_good)
    new_good.rect.x = random.randint (700, 10000)
    new_good.rect.y = random.randint (10, 490)

for i in range(20):
    new_bad = RunnerSprite(BLACK, (35, 25))
    bad_sprites.add(new_bad)
    new_bad.rect.x = random.randint (700, 10000)
    new_bad.rect.y = random.randint (10, 490)

for item in good_sprites:
    all_sprites_list.add(item)

for item in bad_sprites:
    all_sprites_list.add(item)

# part 1.5a-5b
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
        # optional
        """elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and can_restart:
                score = 0
                lives = 5
                all_sprites_list.empty()
                make_blocks()
                can_restart = False"""

    pixie.check(good_sprites)
    pixie.check(bad_sprites)

    if pixie.lives == 0:
        print("GAME OVER!!")
        pygame.quit()
        exit()
    
    # part 1.6b
    screen.fill(WHITE)  

    # part 1.6c
    any_scroller.draw_buildings(screen)
    any_scroller.move_buildings()

    mouse_pos = pygame.mouse.get_pos()
    pixie.rect.x = mouse_pos[0]
    pixie.rect.y = mouse_pos[1]

    good_sprites.update()
    bad_sprites.update()

    all_sprites_list.draw(screen)
    
    # part 1.5c
    pygame.display.flip()
 
    clock.tick(60)

# part 1.5d
pygame.quit()
exit()
