import time
import sys
import gameFunctions as game
from colorama import init, Fore, Style

init()

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
    game.consoleMessage("[Connection Established: Temporal Echo Detected]\n", 1.5, 'blue')
    print()
    game.consoleMessage("[Warning: Anomaly Identified in Timeline Fragmentation]", 1.5, 'warn')

boot()
