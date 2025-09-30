import random
import time
import os
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Characters to use for Matrix code
matrix_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&*"

# The normal "Matrix world" Neo sees
normal_text = [
    "Neo walks into a hallway.",
    "He sees two doors on the left and a window at the end.",
    "Agents are patrolling the corridor."
]

try:
    for line in normal_text:
        # Print normal text first
        print(line)
        time.sleep(1)

    print("\nNeo activates his Matrix vision...\n")
    time.sleep(1)

    # Transform text into Matrix code
    for _ in range(10):  # Number of animation frames
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
        for line in normal_text:
            coded_line = ''.join(random.choice(matrix_chars) for _ in line)
            print(Fore.GREEN + coded_line)
        time.sleep(0.2)

    print("\nNeo now sees everything as code!")
    
except KeyboardInterrupt:
    print("\nDemo stopped.")
