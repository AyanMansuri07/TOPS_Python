import pygame
import math
import sys
import time

pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hypnotic Prank")

clock = pygame.time.Clock()

# Spiral settings
angle = 0
rotation_speed = 2
dot_size = 5
last_speed_increase = time.time()

# Scary stuff
jump_scare_time = 10  # seconds until scare
scary_image = pygame.image.load("C:\\Users\\Ayan\\Downloads\\crepy.png")
scary_image = pygame.transform.scale(scary_image, (WIDTH, HEIGHT))

start_time = time.time()
scare_triggered = False

running = True
while running:
    screen.fill((0, 0, 0))  # Black background

    if not scare_triggered:
        # Draw hypnotic dots
        for i in range(200):
            radius = i * 4
            x = WIDTH // 2 + math.cos(math.radians(angle + i * 10)) * radius
            y = HEIGHT // 2 + math.sin(math.radians(angle + i * 10)) * radius

            # Alternate colors black/white
            color = (255, 255, 255) if i % 2 == 0 else (0, 0, 0)
            pygame.draw.circle(screen, color, (int(x), int(y)), dot_size)

        # Increase speed every second
        if time.time() - last_speed_increase >= 1:
            rotation_speed += 0.3
            dot_size += 0.1
            last_speed_increase = time.time()

        # Rotate
        angle += rotation_speed

        # Trigger image after set time
        if time.time() - start_time >= jump_scare_time:
            scare_triggered = True
    else:
        # Show scary image fullscreen
        screen.blit(scary_image, (0, 0))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
