import os
import random
import time
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Characters for Matrix code
matrix_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&*"

# Commands and responses
commands = ["connect", "decrypt", "scan", "override", "hack", "access"]
responses = [
    "Access Granted ✅",
    "Firewall Blocked ❌",
    "Decrypting...",
    "System Overload ⚠️",
    "Connection Established 🔗",
]

# Terminal size for Matrix effect
WIDTH = 60
HEIGHT = 20
drops = [random.randint(-HEIGHT, 0) for _ in range(WIDTH)]

def matrix_rain_frame():
    """Generate one frame of Matrix-style rain"""
    screen = [[' ' for _ in range(WIDTH)] for _ in range(HEIGHT)]
    for i in range(WIDTH):
        row = drops[i]
        if 0 <= row < HEIGHT:
            screen[row][i] = Fore.GREEN + random.choice(matrix_chars)
        if 0 <= row-1 < HEIGHT:
            screen[row-1][i] = Fore.GREEN + Style.DIM + random.choice(matrix_chars)
        drops[i] += 1
        if drops[i] > HEIGHT + 5:
            drops[i] = random.randint(-20, 0)
    return screen

def print_screen(screen):
    for row in screen:
        print(''.join(row))

def hacker_terminal():
    print(Fore.GREEN + "\n*** Welcome to Neo's Hacker Terminal ***\n")
    time.sleep(1)
    while True:
        # Show Matrix rain
        screen = matrix_rain_frame()
        os.system('cls' if os.name == 'nt' else 'clear')
        print_screen(screen)
        
        # Occasionally ask for a command
        if random.random() > 0.95:  # 5% chance per frame
            cmd = random.choice(commands)
            user_input = input(Fore.GREEN + f"\n>> Type '{cmd}': ")
            if user_input.strip().lower() == cmd:
                print(Fore.GREEN + random.choice(responses))
            else:
                print(Fore.RED + "Command failed ❌")
            time.sleep(1)

try:
    hacker_terminal()
except KeyboardInterrupt:
    print("\nExiting Hacker Terminal...")
