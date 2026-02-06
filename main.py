import os
import pygame

def main():
    try:
        pygame.mixer.init()
    except pygame.error() as e:
        print("failed to intialization audio!")

if __name__ == "__main__":
    main()