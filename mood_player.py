import argparse
import os
import random
import pygame

def play_music(mood):
    music_dir = 'music'
    mood_dir = os.path.join(music_dir,mood)

    if(not os.path.exists(mood_dir)):
        print(f"No Music avalilable for mood : {mood}")
        return
    
    files = [f for f in os.listdir(mood_dir) if f.endswith(".mp3")]
    if not files:
        print(f"No music file for mood : {mood}")
        return
    
    random_file = random.choice(files)
    file_path = os.path.join(mood_dir,random_file)
    print(f'Playing {random_file} for mood : {mood}')
    
    pygame.mixer.init() #initializing the mixer module which is responsible for handling audio files
    pygame.mixer.music.load(file_path) # loaded the file path
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    

def main():

    # Create argument parser
    parser = argparse.ArgumentParser(description="Play music based on your mood")


    # Add a "mood argument"
    parser.add_argument("mood", type=str, help="Your current mood(eg. happy, sad, relaxed etc..)")

    arg = parser.parse_args()

    print(f"Your current mood is : {arg.mood}")
    play_music(arg.mood)




if __name__ == "__main__":
    main()