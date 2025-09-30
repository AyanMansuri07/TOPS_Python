import os
import random
import time
from colorama import init, Fore, Style

init(autoreset=True)

# Terminal size
WIDTH = 80
HEIGHT = 24

# Characters to display
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&*"

# Initialize drop positions for each column
drops = [random.randint(-HEIGHT, 0) for _ in range(WIDTH)]

try:
    while True:
        os.system('cls')  # Clear screen
        screen = [[' ' for _ in range(WIDTH)] for _ in range(HEIGHT)]

        # Update drops
        for i in range(WIDTH):
            row = drops[i]
            if 0 <= row < HEIGHT:
                screen[row][i] = random.choice(chars)
            # Make trailing effect
            if 0 <= row-1 < HEIGHT:
                screen[row-1][i] = Fore.GREEN + Style.DIM + random.choice(chars)
            if 0 <= row-2 < HEIGHT:
                screen[row-2][i] = ' '
            drops[i] += 1
            if drops[i] > HEIGHT + 5:  # Reset drop randomly after it goes down
                drops[i] = random.randint(-20, 0)

        # Print the screen
        for row in screen:
            print(''.join(row))
        
        time.sleep(0.05)  # Adjust speed

except KeyboardInterrupt:
    print("\nMatrix effect stopped!")
    