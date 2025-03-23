import pygame 
 
pygame.init() 
screen = pygame.display.set_mode((800, 600)) 
done = False 
is_red = True 
x = 50 
y = 50 
 
clock = pygame.time.Clock() 
 
while not done: 
        for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                        done = True 
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: 
                        is_red = not is_red 
         
        pressed = pygame.key.get_pressed() 
        if pressed[pygame.K_UP] and y - 3 >= 0: y -= 20 
        if pressed[pygame.K_DOWN] and y + 3 < 600: y += 20 
        if pressed[pygame.K_LEFT] and x - 3 >= 0: x -= 20 
        if pressed[pygame.K_RIGHT] and x + 3 < 800: x += 20 
         
        screen.fill((255, 255, 255)) 
        if is_red: color = (255, 0, 0) 
        else: color = (255, 0, 0) 
        pygame.draw.circle(screen, color, (x, y), 25) 
         
        pygame.display.flip() 
        clock.tick(60)