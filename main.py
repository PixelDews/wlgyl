import time
import sys
import gameFunctions as game
import specialText as special
import pygame
from colorama import init, Fore, Style
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

pygame.mixer.init()
init()

computer_sfx = pygame.mixer.Sound("computer.mp3")
computer_sfx.set_volume(0.1)
error_sfx = pygame.mixer.Sound("error.mp3")
error_sfx.set_volume(2.5)
warp_sfx = pygame.mixer.Sound("warp.mp3")
warp_sfx.set_volume(2.5)

# Running the script with the `-u` flag programmatically
sys.stdout = open(sys.stdout.fileno(), mode='w', buffering=1)

def boot():

    print(Fore.BLUE + """
                                                                 ___                                                
    |\/|  _  _|_  _. __  /\       _  ._ _   _  ._  _|_  _   _|    |   _  ._ _  ._   _  ._  _. |    /\  ._ ._  _.    
    |  | (/_  |_ (_|    /--\ |_| (_| | | | (/_ | |  |_ (/_ (_|    |  (/_ | | | |_) (_) |  (_| |   /--\ |  |  (_| \/ 
                                  _|                                           |                                 /  
    """ + Style.RESET_ALL)

    print("                                 Written by: PixelDews    Published: November 24, 2024")
    print()
    print("[1] Boot")
    print("[0] Exit")
    print()
    choice = game.menu(">> ",0,1)

    if choice == 0:
        exit()

    computer_sfx.play()

    print()
    time.sleep(1)
    game.consoleMessage("Boot Sequence Initiated")
    game.ellipsis()
    game.consoleMessage("Data Synchronization in Progress")
    game.ellipsis()
    game.consoleMessage("Initializing Temporal Interface")
    game.ellipsis()
    game.consoleMessage("Linking Temporal Nodes")
    game.ellipsis()
    game.consoleMessage("[Connection Established: Temporal Echo Detected]", 1.5, 'blue')
    print()
    print()
    game.consoleMessage("[Warning: Anomaly Identified in Timeline Fragmentation]", 1.5, 'warn')
    error_sfx.play()
    print()
    print()
    game.consoleMessage("[Data Transmission Suspended]", 1.5, 'warn')
    error_sfx.play()
    print()
    print()
    game.consoleMessage("[Temporal Rift Detected: Energy Surge Imminent]", 1.5, 'warn')
    error_sfx.play()
    print()
    print()
    computer_sfx.stop()
    special.warp()
    warp_sfx.play()

boot()
