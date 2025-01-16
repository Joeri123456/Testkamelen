import time
import pygame
from defines import TUNES


class SoundManager:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self._starttune = pygame.mixer.Sound('./sounds/kamelenrace_lang.wav')
        self._starttune.set_volume(1)
        self._countdown5 = pygame.mixer.Sound('./sounds/countdown5.wav')
        self._countdown4 = pygame.mixer.Sound('./sounds/countdown4.wav')
        self._countdown3 = pygame.mixer.Sound('./sounds/countdown3.wav')
        self._countdown2 = pygame.mixer.Sound('./sounds/countdown2.wav')
        self._countdown1 = pygame.mixer.Sound('./sounds/countdown1.wav')
        self._start = pygame.mixer.Sound('./sounds/start1.wav')
        self._punt1 = pygame.mixer.Sound('./sounds/punt1.wav')
        self._punt2 = pygame.mixer.Sound('./sounds/punt2.wav')
        self._punt3 = pygame.mixer.Sound('./sounds/punt3.wav')
        self._punt4 = pygame.mixer.Sound('./sounds/punt4.wav')
        self._winner1 = pygame.mixer.Sound('./sounds/winner1.wav')
        self._winner2 = pygame.mixer.Sound('./sounds/winner2.wav')
        self._winner3 = pygame.mixer.Sound('./sounds/winner3.wav')
        self._winner4 = pygame.mixer.Sound('./sounds/winner4.wav')      


    def starttune(self, tunename):
        match tunename:
            case TUNES.camelsong:
                self._starttune.play()
            case TUNES.countdown5:
                self._countdown5.play()
            case TUNES.countdown4:
                self._countdown4.play()
            case TUNES.countdown3:
                self._countdown3.play()
            case TUNES.countdown2:
                self._countdown2.play()
            case TUNES.countdown1:
                self._countdown1.play()
            case TUNES.start:
                self._start.play()
            case TUNES.punt1:
                self._punt1.play()
            case TUNES.punt2:
                self._punt2.play()
            case TUNES.punt3:
                self._punt3.play()
            case TUNES.punt4:
                self._punt4.play()
            case TUNES.winner1:
                self._winner1.play()
            case TUNES.winner2:
                self._winner2.play()
            case TUNES.winner3:
                self._winner3.play()
            case TUNES.winner4:
                self._winner4.play()

    def tuneisplaying(self):
        return pygame.mixer.get_busy()
    
    def waittunefinished(self):
        while self.tuneisplaying(): time.sleep(1);



if __name__ == "__main__":
    #test class
    sounds = SoundManager();
    sounds.starttune(TUNES.camelsong);
    sounds.waittunefinished()
    sounds.starttune(TUNES.countdown5);
    sounds.waittunefinished()
    sounds.starttune(TUNES.countdown4);
    sounds.waittunefinished()
    sounds.starttune(TUNES.countdown3);
    sounds.waittunefinished()
    sounds.starttune(TUNES.countdown2);
    sounds.waittunefinished()
    sounds.starttune(TUNES.countdown1);
    sounds.waittunefinished()
    sounds.starttune(TUNES.start);
    sounds.waittunefinished()
    sounds.starttune(TUNES.punt1);
    sounds.waittunefinished()
    sounds.starttune(TUNES.punt2);
    sounds.waittunefinished()
    sounds.starttune(TUNES.punt3);
    sounds.waittunefinished()
    sounds.starttune(TUNES.punt4);
    sounds.waittunefinished()
    sounds.starttune(TUNES.winner1);
    sounds.waittunefinished()
    sounds.starttune(TUNES.winner2);
    sounds.waittunefinished()
    sounds.starttune(TUNES.winner3);
    sounds.waittunefinished()
    sounds.starttune(TUNES.winner4);
    sounds.waittunefinished()


