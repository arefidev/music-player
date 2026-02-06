import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame

def main():
    try:
        pygame.mixer.init()
    except pygame.error() as e:
        print("failed to intialization audio!", e)

if __name__ == "__main__":
    main()