import pygame
import random
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

dodged = 0

#Define the screen size.
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# Create the screen.
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Create event for adding new enemys
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

def score(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score " + str(dodged), True, (255,255,255))
    screen.blit(text, (300,0))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        
    def update(self, pressed_keys):
        
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
            
        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((20,10))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(
            center = (
            random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
            random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5, 20)
    
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
            

player = Player()
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
# Setup the clock for a decent framerate
clock = pygame.time.Clock()



pygame.init()
#Game loop
running = True
while running:
    
    # for loop through the event queue
    for event in pygame.event.get():
        # Check for KEYDOWN event
        if event.type == KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
            if event.key == K_ESCAPE:
                running = False
        # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == QUIT:
            running = False
            
        #Add a new enemy.
        elif event.type == ADDENEMY:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
            #adding the score every time a enemy spawns.
            dodged += 1
            
    
    #Update enemy position.
    enemies.update()

    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()
    
    #Update "movment" from class player.
    player.update(pressed_keys)
    
    # Fill the screen with black
    screen.fill((0, 0, 0))
    score(dodged)

    # Draw the player on the screen
    screen.blit(player.surf, player.rect)
    
    # Draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
        
    if pygame.sprite.spritecollideany(player, enemies):
        player.kill()
        running = False

    # Update the display
    pygame.display.flip()
    
    # make the game a 30FPS "frames per second."
    clock.tick(30)