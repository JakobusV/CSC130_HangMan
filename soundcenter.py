from pygame import mixer
import time


#pip install pygame
def play_sound_file(value):

    mixer.init()
    mixer.music.load('sounds/' + value + '.mp3')
    mixer.music.play()
    while mixer.music.get_busy():  # wait for music to finish playing
        time.sleep(1)

    
play_sound_file("main")