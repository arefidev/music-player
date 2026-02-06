import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame

def main():
    try:
        pygame.mixer.init()
    except pygame.error() as e:
        print("failed to intialization audio!", e)

    folder = "mp3"

    if not os.path.isdir(folder):
        print(f"Folder {folder} not found!")

    mp3_files = [file for file in os.listdir(folder) if file.endswith(".mp3")]
    while True:
        print("***** MP3 Player *****")
        print("My song list: ")
        
        for index, song in enumerate(mp3_files, start=1):
            print(f"{index}. {song}")
        

        choice_input = input("Enter the number of the song to play (or 'Q' for quit): ")
        if choice_input.upper() == "Q":
            print("Bye!")
            break
        
        if not choice_input.isdigit():
            print("Enter a valid number!")
            
        choice = int(choice_input) - 1
        
        if 0 <= choice < len(mp3_files):
            # music_player()
            pass
        else:
            print("Invalid input!")
        

if __name__ == "__main__":
    main()