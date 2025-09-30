import pygame
import math
import random
import sys

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Digital Tunnel of Code")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BRIGHT_GREEN = (180, 255, 180)

# Font
font_size = 20
font = pygame.font.SysFont("consolas", font_size, bold=True)

# Characters for the tunnel
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&*"

# Tunnel parameters
num_chars = 200
radius = 200
speed = 0.05

# Generate initial characters with angles
tunnel_chars = []
for i in range(num_chars):
    angle = random.uniform(0, 2*math.pi)
    z = random.uniform(0, 600)
    char = random.choice(chars)
    tunnel_chars.append([angle, z, char])

# Main loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill(BLACK)
    
    for i in range(num_chars):
        angle, z, char = tunnel_chars[i]
        
        # Perspective projection
        factor = 500 / (z + 1)
        x = int(WIDTH / 2 + radius * math.cos(angle) * factor)
        y = int(HEIGHT / 2 + radius * math.sin(angle) * factor)
        
        # Choose brighter for closer chars
        color = BRIGHT_GREEN if z < 300 else GREEN
        
        # Draw character
        text = font.render(char, True, color)
        screen.blit(text, (x, y))
        
        # Move char closer to viewer
        z -= 4
        if z < 0:
            z = 600
            angle = random.uniform(0, 2*math.pi)
            char = random.choice(chars)
        tunnel_chars[i] = [angle, z, char]
    
    pygame.display.flip()
    clock.tick(60)
