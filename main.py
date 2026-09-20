import math
from collections import deque
import pygame

pygame.init()
WIDTH, HEIGHT = 864, 486
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Happy Roller")

minecart_sprite = pygame.image.load("minecart.png").convert_alpha()
minecart_sprite = pygame.transform.smoothscale(minecart_sprite, (40, 30))

MAX_POINTS = 300
PATH_SPEED = 100      
  
class Game:
    TURN_SPEED = 2.5 
    head_x, head_y = 100, HEIGHT // 2
    angle_deg = 0.0
    running = True
    path = deque(maxlen=MAX_POINTS)
    path_color = (255, 255, 255) # white basically
    pointer_color = (255, 80, 80)
    minecart_pos = [100, 100]
    minecart_velocity = [50, 0]
    dt = 1/60
    GRAVITY = 10

    def __init__(self, fps):
        self.path.append((self.head_x, self.head_y))
        self.dt = 1/fps

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.angle_deg -= self.TURN_SPEED
            self.angle_deg = max(self.angle_deg, -90)
        if keys[pygame.K_DOWN]:
            self.angle_deg += self.TURN_SPEED
            self.angle_deg = min(self.angle_deg, 90)

    def game_loop(self):
        angle_rad = math.radians(self.angle_deg)
        self.head_x += PATH_SPEED * self.dt * math.cos(angle_rad)
        self.head_y += PATH_SPEED * self.dt * math.sin(angle_rad)
        self.head_x %= WIDTH
        self.head_y %= HEIGHT

        self.minecart_pos[0] += self.minecart_velocity[0] * self.dt
        self.minecart_pos[1] += self.minecart_velocity[1] * self.dt

        self.path.append((self.head_x, self.head_y))
        screen.fill("black")



    def draw(self):
        if len(self.path) >= 2:
            pygame.draw.lines(screen, self.path_color, False, list(self.path), 6)

        screen.blit(minecart_sprite, self.minecart_pos)
        pygame.draw.circle(screen, self.pointer_color, (int(self.head_x), int(self.head_y)), 5)
        pygame.display.flip()


game = Game(60) # get an instance of the game object

# the main game loop
while game.running:
    clock.tick(60)
    game.handle_input()
    game.game_loop()
    game.draw()    

pygame.quit()