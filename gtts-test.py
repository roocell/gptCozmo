from gtts import gTTS
from io import BytesIO
import pygame
import time

pygame.init()
pygame.mixer.init(buffer=4096) #prevent underrun errors

class Speech():

    @classmethod
    def speak(cls, text):
        mp3_file_object = BytesIO()
        tts = gTTS(text, lang='en')
        tts.write_to_fp(mp3_file_object)
        pygame.mixer.music.load(mp3_file_object, 'mp3')
        pygame.mixer.music.play()
        #pygame.mixer.Sound("hello.wav").play()
        

Speech.speak('hello world')
time.sleep(20) # can't close before pygame plays the sound