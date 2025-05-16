#!/usr/bin/env python3
import os
import time

def display_splash():
    # Clear the terminal screen (works on Windows and Unix-like systems)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # ASCII art for a leaf with HERBSCRIBE-CLI displayed under it
    splash_art = r"""
             ___
          .-'   '-.
        .'         '.
       /  .-'''-.    \
      |  /       \   |
      | |         |  |
      |  \       /   |
       \  '-...-'   /
        '.         .'
          '-.___.-'
    
         HERBSCRIBE-CLI
    """
    
    # Print the splash screen
    print(splash_art)
    
    # Display for 5 seconds
    time.sleep(5)

if __name__ == '__main__':
    display_splash()
