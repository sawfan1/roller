import math
from collections import deque
import pygame

pygame.init()
WIDTH, HEIGHT = 864, 486
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Happy Roller")

MAX_POINTS = 300
STEP_SIZE = 2      
TURN_SPEED = 2.5   
head_x, head_y = 100, HEIGHT // 2
angle_deg = 0.0 


path = deque(maxlen=MAX_POINTS)
path.append((head_x, head_y))

running = True

def game_loop():
    angle_rad = math.radians(angle_deg)
    head_x += STEP_SIZE * math.cos(angle_rad)
    head_y += STEP_SIZE * math.sin(angle_rad)
    head_x %= WIDTH
    head_y %= HEIGHT

    path.append((head_x, head_y))
    screen.fill("black")

    if len(path) >= 2:
        pygame.draw.lines(screen, (255, 220, 250), False, list(path), 6)

    pygame.draw.circle(screen, (255, 80, 80), (int(head_x), int(head_y)), 5)


while running:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        angle_deg -= TURN_SPEED
        angle_deg = max(angle_deg, -90)
    if keys[pygame.K_DOWN]:
        angle_deg += TURN_SPEED
        angle_deg = min(angle_deg, 90)

    game_loop()

    pygame.display.flip()

pygame.quit()