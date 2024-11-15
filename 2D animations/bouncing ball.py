import pygame
import random
pygame.init()
screen_width, screen_height = 1200, 700
background_color = (0, 0, 0)
speed = [1, 1]
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bouncing Ball")
ball = pygame.draw.circle(screen,(255,0,0),[200,450],radius = 30)
running = True
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    ball = ball.move(speed)
    if ball.left < 0 or ball.right > screen_width:
        speed[0] = -speed[0]
    if ball.top < 0 or ball.bottom > screen_height:
        speed[1] = -speed[1]
    a = random.randint(0,255)
    b = random.randint(0,255)
    c = random.randint(0,255)
    screen.fill(background_color)
    pygame.draw.circle(screen,(a,b,c),ball.center,radius = 30)
    pygame.display.flip()
pygame.quit()
