import pygame
import sys
import random
import math

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Arena Battle")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)

# Snake (player) settings
snake_pos = [WIDTH // 2, HEIGHT // 2]
snake_segments = []
snake_length = 20
snake_size = 15
snake_speed = 5
snake_color = GREEN

# Enemy settings
enemies = []
enemy_size = 15
enemy_base_speed = 3
enemy_count = 3  # number of enemies

# Food settings
food_size = 10
foods = []
food_count = 6  # number of foods

# Score & Level
score = 0
level = 1
font = pygame.font.SysFont(None, 35)

clock = pygame.time.Clock()

def draw_text(text, x, y, color=WHITE):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

def distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def spawn_enemy():
    return {
        "pos": [random.randint(50, WIDTH-50), random.randint(50, HEIGHT-50)],
        "segments": [],
        "length": 20,
        "color": (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255)),
        "speed": enemy_base_speed
    }

def spawn_food():
    return [random.randint(20, WIDTH - 20), random.randint(20, HEIGHT - 20)]

# Create starting enemies
for _ in range(enemy_count):
    enemies.append(spawn_enemy())

# Create starting food
for _ in range(food_count):
    foods.append(spawn_food())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # === Player movement ===
    mouse_x, mouse_y = pygame.mouse.get_pos()
    dx = mouse_x - snake_pos[0]
    dy = mouse_y - snake_pos[1]
    dist = max(1, (dx**2 + dy**2) ** 0.5)
    snake_pos[0] += (dx / dist) * snake_speed
    snake_pos[1] += (dy / dist) * snake_speed

    snake_segments.insert(0, list(snake_pos))
    if len(snake_segments) > snake_length:
        snake_segments.pop()

    # === Enemy movement ===
    for enemy in enemies:
        # Find nearest food for enemy
        if foods:
            target_food = min(foods, key=lambda f: distance(enemy["pos"], f))
            ex = target_food[0] - enemy["pos"][0]
            ey = target_food[1] - enemy["pos"][1]
            edist = max(1, (ex**2 + ey**2) ** 0.5)
            enemy["pos"][0] += (ex / edist) * enemy["speed"]
            enemy["pos"][1] += (ey / edist) * enemy["speed"]

        enemy["segments"].insert(0, list(enemy["pos"]))
        if len(enemy["segments"]) > enemy["length"]:
            enemy["segments"].pop()

    # === Check food collisions ===
    # Player eats food
    for food in foods[:]:
        if distance(snake_pos, food) < snake_size:
            score += 1
            snake_length += 3
            snake_color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
            foods.remove(food)
            foods.append(spawn_food())

    # Enemy eats food
    for enemy in enemies:
        for food in foods[:]:
            if distance(enemy["pos"], food) < enemy_size:
                enemy["length"] += 3
                foods.remove(food)
                foods.append(spawn_food())

    # === Check collisions: Player vs Enemy ===
    for enemy in enemies[:]:
        # If enemy head or body touches player head or body → enemy dies
        for seg in snake_segments:
            if distance(enemy["pos"], seg) < snake_size:
                score += enemy["length"] // 5
                snake_length += enemy["length"] // 3
                enemies.remove(enemy)
                enemies.append(spawn_enemy())
                break
            # Enemy body touching player head
            if distance(snake_pos, seg) < snake_size:
                pass  # already handled above

    # === Drawing ===
    screen.fill(BLACK)

    # Draw player snake
    for seg in snake_segments:
        pygame.draw.circle(screen, snake_color, (int(seg[0]), int(seg[1])), snake_size // 2)

    # Draw enemies
    for enemy in enemies:
        for seg in enemy["segments"]:
            pygame.draw.circle(screen, enemy["color"], (int(seg[0]), int(seg[1])), enemy_size // 2)

    # Draw foods
    for food in foods:
        pygame.draw.circle(screen, RED, (int(food[0]), int(food[1])), food_size // 2)

    # Draw score & level
    draw_text(f"Score: {score}", 10, 10)
    draw_text(f"Level: {level}", 10, 40)

    pygame.display.flip()
    clock.tick(60)
