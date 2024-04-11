# Imports
import pygame
import sys
import random
import time
from pygame.locals import *

# Initializing Pygame
pygame.init()

# Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Creating colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COIN_WEIGHTS = [1, 2, 3]  # Weights of the coins
N = 5  # Number of coins to collect before increasing speed

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Create a white screen
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(random.randint(40, SCREEN_WIDTH - 40), 0, 30, 30)

    def move(self):
        global SPEED, SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            SCORE += 1
            self.rect.top = 0
            self.rect.centerx = random.randint(40, SCREEN_WIDTH - 40)
            # Increase speed if SCORE is a multiple of N
            if SCORE % N == 0:
                SPEED += 1

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(160, 520, 30, 30)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.rect = pygame.Rect(x, y, 20, 20)

    def move(self):
        global SPEED
        self.rect.move_ip(0, SPEED)

# Setting up Sprites
P1 = Player()
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)

# Adding a new User event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Game Loop
while True:
    # Cycles through all events occurring
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.fill(WHITE)

    # Generate coins randomly on the road
    for i in range(3):
        coin_weight = random.choice(COIN_WEIGHTS)
        coin_x = 80 * (i + 1)
        coin_y = -30
        coin = Coin(coin_x, coin_y)
        all_sprites.add(coin)

    scores = font_small.render("Score: " + str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (SCREEN_WIDTH - scores.get_width() - 10, 10))

    # Moves and Re-draws all Sprites
    for entity in all_sprites:
        if isinstance(entity, Player):
            pygame.draw.rect(DISPLAYSURF, BLUE, entity.rect)
            entity.move()
        elif isinstance(entity, Coin):
            pygame.draw.circle(DISPLAYSURF, GREEN, entity.rect.center, 10)
            entity.move()
            if entity.rect.colliderect(P1.rect):
                SCORE += 1
                entity.kill()

    # Create enemies
    if random.randint(0, 20) == 0:
        E1 = Enemy()
        enemies.add(E1)
        all_sprites.add(E1)

    # Moves and Re-draws all Enemies
    for enemy in enemies:
        pygame.draw.rect(DISPLAYSURF, RED, enemy.rect)
        enemy.move()

    # To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)

        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)
