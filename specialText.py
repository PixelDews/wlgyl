import time
import sys
from colorama import init, Fore, Style
import random
import os

def warp():
    text1 = Fore.BLUE + """ 
           __    ____   _  __   __ __   ____   _  __  _____         
      / /   /  _/  / |/ /  / //_/  /  _/  / |/ / / ___/         
     / /__ _/ /   /    /  / ,<    _/ /   /    / / (_ /  _  _  _ 
    /____//___/  /_/|_/  /_/|_|  /___/  /_/|_/  \___/  (_)(_)(_)

    """
    text2 = Fore.CYAN + """ 
        _/         _/_/_/       _/      _/       _/    _/       _/_/_/       _/      _/        _/_/_/                  
       _/           _/         _/_/    _/       _/  _/           _/         _/_/    _/      _/                         
      _/           _/         _/  _/  _/       _/_/             _/         _/  _/  _/      _/  _/_/                    
     _/           _/         _/    _/_/       _/  _/           _/         _/    _/_/      _/    _/                     
    _/_/_/_/   _/_/_/       _/      _/       _/    _/       _/_/_/       _/      _/        _/_/_/       _/   _/   _/   

    """
    text3 = Fore.RED + """ 
     _____      _____   ____  _____   ___  ____    _____   ____  _____     ______               
    |_   _|    |_   _| |_   \|_   _| |_  ||_  _|  |_   _| |_   \|_   _|  .' ___  |              
      | |        | |     |   \ | |     | |_/ /      | |     |   \ | |   / .'   \_|              
      | |   _    | |     | |\ \| |     |  __'.      | |     | |\ \| |   | |   ____              
     _| |__/ |  _| |_   _| |_\   |_   _| |  \ \_   _| |_   _| |_\   |_  \ `.___]  |  _   _   _  
    |________| |_____| |_____|\____| |____||____| |_____| |_____|\____|  `._____.'  (_) (_) (_) 


    """
    text4 = Fore.YELLOW + """ 
     _      ___  _   _  _  __ ___  _   _   ____          
    | |    |_ _|| \ | || |/ /|_ _|| \ | | / ___|         
    | |     | | |  \| || ' /  | | |  \| || |  _          
    | |___  | | | |\  || . \  | | | |\  || |_| | _  _  _ 
    |_____||___||_| \_||_|\_\|___||_| \_| \____|(_)(_)(_)

    """

    warpText = [text1, text2, text3, text4]

    i =0
    while i < 50:
        # Clear the terminal screen
        os.system('cls' if os.name == 'nt' else 'clear')

        # Randomly select a banner to display
        random_text = random.choice(warpText)

        # Print the banner
        print(random_text)

        # Delay before switching banners
        time.sleep(random.uniform(0.1, 0.3))  # Adjust for glitch speed
        i +=1
