import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Matrix Code Rain")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BRIGHT_GREEN = (180, 255, 180)  # Top character highlight

# Font for Matrix characters
font_size = 25
# Use a font that is monospace and clear
font = pygame.font.SysFont("consolas", font_size, bold=True)

# Characters to display
matrix_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&*"

# Column class
class Column:
    def __init__(self, x):
        self.x = x
        self.y_positions = [random.randint(-600, 0) for _ in range(20)]
        self.speed = random.randint(5, 15)
    
    def fall(self):
        for i in range(len(self.y_positions)):
            self.y_positions[i] += self.speed
            if self.y_positions[i] > HEIGHT:
                self.y_positions[i] = random.randint(-100, 0)
    
    def draw(self):
        for i, y in enumerate(self.y_positions):
            char = random.choice(matrix_chars)
            # Make the top character brighter
            color = BRIGHT_GREEN if i == len(self.y_positions) - 1 else GREEN
            text = font.render(char, True, color)
            screen.blit(text, (self.x, y))

# Create columns across the screen
columns = [Column(x) for x in range(0, WIDTH, font_size)]

# Main loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Slightly transparent black background to create trails
    screen.fill(BLACK)
    
    for col in columns:
        col.fall()
        col.draw()
    
    pygame.display.flip()
    clock.tick(30)  # FPS
