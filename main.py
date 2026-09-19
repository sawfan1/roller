import math
from collections import deque
import pygame

pygame.init()
WIDTH, HEIGHT = 864, 486
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Happy Roller")

# Track parameters
MAX_POINTS = 300       # Controls the length/tail of the track path
STEP_SIZE = 2         # Distance between consecutive track points
TURN_SPEED = 2.5       # Degrees turned per frame when holding Up/Down

# State variables
head_x, head_y = 100, HEIGHT // 2
angle_deg = 0.0        # 0 degrees points straight right

# Store path coordinates: maxlen automatically drops points from the back
path = deque(maxlen=MAX_POINTS)
path.append((head_x, head_y))

running = True
while running:
    clock.tick(60)
    
    # 1. Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. Key Controls (Adjust Path Angle)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        angle_deg -= TURN_SPEED
        angle_deg = max(angle_deg, -90)
    if keys[pygame.K_DOWN]:
        angle_deg += TURN_SPEED
        angle_deg = min(angle_deg, 90)

    # 3. Calculate Next Point
    angle_rad = math.radians(angle_deg)
    head_x += STEP_SIZE * math.cos(angle_rad)
    head_y += STEP_SIZE * math.sin(angle_rad)

    # Wrap or restrict coordinates to keep inside screen window
    head_x %= WIDTH
    head_y %= HEIGHT

    # Add new head position (drops oldest tail point automatically)
    path.append((head_x, head_y))

    # 4. Rendering
    screen.fill("black")

    # Draw continuous polyline if we have at least 2 points
    if len(path) >= 2:
        # pygame.draw.lines requires a list of (x, y) tuples
        pygame.draw.lines(screen, (255, 220, 250), False, list(path), 6)

    # Optional: Draw small indicator circle at the front
    pygame.draw.circle(screen, (255, 80, 80), (int(head_x), int(head_y)), 5)

    pygame.display.flip()

pygame.quit()