import time
import sys
from colorama import init, Fore, Style

init()

def message(sender, msg, sec):
    time.sleep(sec)
    print("\n" + str(sender) + ": " + str(msg), flush=True)

def consoleMessage(msg, sec=0, msg_type=""):
    time.sleep(sec)
    if msg_type == 'warn':
        print(Fore.RED + Style.BRIGHT + msg, end="" + Style.RESET_ALL, flush=True)
    elif msg_type == 'blue':
        print(Fore.BLUE + msg, end="" + Style.RESET_ALL, flush=True)
    elif msg_type == 'yellow':
        print(Fore.YELLOW + msg, end="" + Style.RESET_ALL, flush=True)
    else:
        print(msg, end="", flush=True)  # Default message with no color

def inputConsoleMessage(msg, sec=0, msg_type=""):
    time.sleep(sec)
    if msg_type == 'warn':
        input(Fore.RED + Style.BRIGHT + msg + Style.RESET_ALL)
    elif msg_type == 'blue':
        input(Fore.BLUE + msg + Style.RESET_ALL)
    elif msg_type == 'yellow':
        input(Fore.YELLOW + msg + Style.RESET_ALL)
    else:
        input(msg)  # Default message with no color


def inputMessage(sender, msg, sec=0):
    time.sleep(sec)
    input("\n" + str(sender) + ": " + str(msg), flush=True)
def menu(prompt, min, max):

    while True:
        try:
            choice = int(input(prompt))
        except ValueError:
            print("\nInput must be an integer")
            continue

        if min <= choice <= max:
            return choice
            break
        else:
            print("\nInteger must be in range")

def ellipsis(sec=0.75):
    time.sleep(sec)
    print(".", end="", flush=True)
    time.sleep(sec)
    print(".", end="", flush=True)
    time.sleep(sec)
    print(".", end="", flush=True)
    time.sleep(sec)
    print()
    print()
