import pygame
from pygame.locals import *
import random
import time

pygame.init() # initializes all the pygame sub-modules

WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # creating a game window
# set_mode() takes a tuple as an argument

image_background = pygame.image.load('/home/kali/my_project/urban-octo-memory/Lab8/AnimatedStreet.png')
image_player = pygame.image.load('/home/kali/my_project/urban-octo-memory/Lab8/Player.png')
image_enemy = pygame.image.load('/home/kali/my_project/urban-octo-memory/Lab8/Enemy.png')
image_coin = pygame.image.load('/home/kali/my_project/urban-octo-memory/Lab8/coin2.png')

pygame.mixer.music.load('/home/kali/my_project/urban-octo-memory/Lab8/background.wav')
pygame.mixer.music.play(-1)

sound_crash = pygame.mixer.Sound('/home/kali/my_project/urban-octo-memory/Lab8/crash.wav')

font = pygame.font.SysFont("Verdana", 60)
image_game_over = font.render("Game Over", True, "black")
image_game_over_rect = image_game_over.get_rect(center = (WIDTH // 2, HEIGHT // 2))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_player
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT
        self.speed = 5
        # or
        # self.rect.midbottom = (WIDTH // 2, HEIGHT)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(self.speed, 0)
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_enemy
        self.rect = self.image.get_rect()
        self.speed = 10
        # or
        # self.rect.midbottom = (WIDTH // 2, HEIGHT)

    def generate_random_rect(self):
        self.rect.left = random.randint(0, WIDTH - self.rect.w)
        self.rect.bottom = 0

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > HEIGHT:
            self.generate_random_rect()
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_coin
        self.rect = self.image.get_rect()
        self.speed = 3
        # or
        # self.rect.midbottom = (WIDTH // 2, HEIGHT)

    def generate_random_rect(self):
        self.rect.center = (random.randint(50, 370), random.randint(50, 570))

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > HEIGHT:
            self.generate_random_rect()
running = True

# this object allows us to set the FPS
clock = pygame.time.Clock()
FPS = 60

player = Player()
enemy = Enemy()
Coin1 = Coin()

all_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()
Coin_sprites = pygame.sprite.Group()

all_sprites.add(player, enemy, Coin1)
enemy_sprites.add(enemy)
Coin_sprites.add(Coin1)
f1 = pygame.font.Font(None, 20)
score = 0

while running: # game loop
    for event in pygame.event.get(): # event loop
        if event.type == pygame.QUIT:
            running = False
    label = f1.render(str(score), True, (255, 255, 0))
    player.move()

    screen.blit(image_background, (0, 0))
    screen.blit(image_coin, (330, 10))
    screen.blit(label, (370, 20))
    for entity in all_sprites:
        entity.move()
        screen.blit(entity.image, entity.rect)

    if pygame.sprite.spritecollideany(player, enemy_sprites):
        sound_crash.play()
        time.sleep(1)
        screen.fill("red")
        screen.blit(image_game_over, image_game_over_rect)
        pygame.display.flip()
        time.sleep(1)
        screen.blit(image_background, (0, 0))
        pygame.display.flip()
        enemy.generate_random_rect()
        for entity in all_sprites:
            entity.move()
            screen.blit(entity.image, entity.rect)


    if pygame.sprite.spritecollideany(player, Coin_sprites):
        Coin1.generate_random_rect()
        score += 1
        
    
    pygame.display.flip() # updates the screen
    clock.tick(FPS) # sets the FPS

pygame.quit()