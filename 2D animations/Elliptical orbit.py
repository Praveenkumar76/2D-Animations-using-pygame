import pygame
import math
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Elliptical Orbit Example")
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
CENTER = (400, 300)
a = 200
b = 100
e = math.sqrt(1 - (b ** 2 / a ** 2))
angle = 0
speed = 0.001
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BLACK)
    pygame.draw.ellipse(screen, WHITE, (CENTER[0] - a, CENTER[1] - b, 2 * a, 2 * b), 1)  # Draw ellipse
    x = CENTER[0] + a * math.cos(angle)
    y = CENTER[1] + b * math.sin(angle)
    pygame.draw.circle(screen, BLUE, (int(x), int(y)), 10)  # Draw orbiting circle
    angle += speed
    pygame.display.flip()
pygame.quit()
