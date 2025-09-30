import random
import time
import os
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Characters for Matrix code
matrix_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&*"

# Sample world text (normal reality)
normal_text = [
    "Neo walks into a dark hallway.",
    "He sees two doors on the left and a window at the end.",
    "Agents are patrolling the corridor."
]

# Matrix rain setup
WIDTH = 80
HEIGHT = 20
drops = [random.randint(-HEIGHT, 0) for _ in range(WIDTH)]

def matrix_rain():
    """Generate one frame of falling Matrix code"""
    screen = [[' ' for _ in range(WIDTH)] for _ in range(HEIGHT)]
    for i in range(WIDTH):
        row = drops[i]
        if 0 <= row < HEIGHT:
            screen[row][i] = Fore.GREEN + random.choice(matrix_chars)
        if 0 <= row-1 < HEIGHT:
            screen[row-1][i] = Fore.GREEN + Style.DIM + random.choice(matrix_chars)
        if 0 <= row-2 < HEIGHT:
            screen[row-2][i] = ' '
        drops[i] += 1
        if drops[i] > HEIGHT + 5:
            drops[i] = random.randint(-20, 0)
    return screen

def print_screen(screen):
    for row in screen:
        print(''.join(row))

def digital_world_simulator():
    print(Fore.GREEN + "\n*** Welcome to Neo's Digital Reality Simulator ***\n")
    time.sleep(2)

    # Step 1: Show normal text world
    for line in normal_text:
        print(line)
        time.sleep(1.2)

    print("\nNeo activates his Matrix vision...\n")
    time.sleep(1.5)

    # Step 2: Transform text into Matrix code with falling effect
    for _ in range(20):  # Number of animation frames
        os.system('cls' if os.name == 'nt' else 'clear')
        # Print falling code frame
        screen = matrix_rain()
        # Overlay normal text as transformed code
        for i, line in enumerate(normal_text):
            if 0 <= i < HEIGHT:
                line_code = ''.join(random.choice(matrix_chars) for _ in line)
                screen[i][:len(line)] = [Fore.GREEN + ch for ch in line_code]
        print_screen(screen)
        time.sleep(0.1)

    print("\nNeo now sees everything as code! The digital world is revealed.\n")

try:
    digital_world_simulator()
except KeyboardInterrupt:
    print("\nSimulation stopped by user.")
