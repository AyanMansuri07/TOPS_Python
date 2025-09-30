import os
import random
import time
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&*"
commands = ["connect", "decrypt", "scan", "override", "hack", "access"]
responses = ["Access Granted ✅", "Firewall Blocked ❌", "Decrypting...", "System Overload ⚠️", "Connection Established 🔗"]

# Matrix rain column positions
WIDTH = 80
HEIGHT = 20
drops = [random.randint(-HEIGHT, 0) for _ in range(WIDTH)]

def matrix_rain():
    """Generates one frame of Matrix rain"""
    screen = [[' ' for _ in range(WIDTH)] for _ in range(HEIGHT)]
    for i in range(WIDTH):
        row = drops[i]
        if 0 <= row < HEIGHT:
            screen[row][i] = Fore.GREEN + random.choice(chars)
        if 0 <= row-1 < HEIGHT:
            screen[row-1][i] = Fore.GREEN + Style.DIM + random.choice(chars)
        if 0 <= row-2 < HEIGHT:
            screen[row-2][i] = ' '
        drops[i] += 1
        if drops[i] > HEIGHT + 5:
            drops[i] = random.randint(-20, 0)
    return screen

def print_screen(screen):
    for row in screen:
        print(''.join(row))

def run_terminal_game():
    print(Fore.GREEN + "\n*** Welcome to Neo Terminal Simulator ***\n")
    time.sleep(1)
    while True:
        # Show Matrix rain
        screen = matrix_rain()
        os.system('cls' if os.name == 'nt' else 'clear')
        print_screen(screen)
        
        # Randomly ask for a command
        if random.random() > 0.95:  # 5% chance each frame
            cmd = random.choice(commands)
            user_input = input(Fore.GREEN + f"\n>> Type '{cmd}': ")
            if user_input.strip().lower() == cmd:
                print(Fore.GREEN + random.choice(responses))
            else:
                print(Fore.RED + "Command failed ❌")
            time.sleep(1)

try:
    run_terminal_game()
except KeyboardInterrupt:
    print("\nExiting Neo Terminal Simulator...")
