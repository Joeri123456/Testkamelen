import time
import pygame
from defines import TUNES


class SoundManager:
    def __init__(self):
        #pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512, devicename="kameel", allowedchanges=5)
        pygame.mixer.pre_init(buffer=4096);
        pygame.init()
        pygame.mixer.init()
        #print("nr of channels:")
        #print(pygame.mixer.get_num_channels() )
        pygame.mixer.set_num_channels(25)
        #print("nr of channels:")
        #print(pygame.mixer.get_num_channels() )
        #pygame.mixer.Channel[1].set_volume(1,1)
        self._starttune = pygame.mixer.Sound('./sounds/kamelenrace_lang.wav')
        #self._starttune.set_volume(1)
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
        print("nr of channels:")
        print(pygame.mixer.get_num_channels() )
        

    def starttune(self, tunename):
        match tunename:
            case TUNES.camelsong:
                pygame.mixer.Channel(1).play(self._starttune)
                #self._starttune.play()
            case TUNES.countdown5:
                pygame.mixer.Channel(2).play(self._countdown5)
                #self._countdown5.play()
            case TUNES.countdown4:
                pygame.mixer.Channel(3).play(self._countdown4)
                #self._countdown4.play()
            case TUNES.countdown3:
                pygame.mixer.Channel(4).play(self._countdown3)
                #self._countdown3.play()
            case TUNES.countdown2:
                pygame.mixer.Channel(5).play(self._countdown2)
                #self._countdown2.play()
            case TUNES.countdown1:
                pygame.mixer.Channel(6).play(self._countdown1)
                #self._countdown1.play()
            case TUNES.start:
                pygame.mixer.Channel(7).play(self._start)
                #self._start.play()
            case TUNES.punt1:
                pygame.mixer.Channel(8).play(self._punt1)
                #self._punt1.play()
            case TUNES.punt2:
                pygame.mixer.Channel(9).play(self._punt2)
                #self._punt2.play()
            case TUNES.punt3:
                pygame.mixer.Channel(10).play(self._punt3)
                #self._punt3.play()
            case TUNES.punt4:
                pygame.mixer.Channel(11).play(self._punt4)
                #self._punt4.play()
            case TUNES.winner1:
                pygame.mixer.Channel(12).play(self._winner1)
                #self._winner1.play()
            case TUNES.winner2:
                pygame.mixer.Channel(13).play(self._winner2)
                #self._winner2.play()
            case TUNES.winner3:
                pygame.mixer.Channel(14).play(self._winner3)
                #self._winner3.play()
            case TUNES.winner4:
                pygame.mixer.Channel(15).play(self._winner4)
                #self._winner4.play()

    def tuneisplaying(self):
        return pygame.mixer.get_busy()
    
    def waittunefinished(self):
        while self.tuneisplaying(): time.sleep(0.1);



if __name__ == "__main__":
    #test class
    sounds = SoundManager();
    if(False): 
        sounds.starttune(TUNES.camelsong);
        sounds.waittunefinished();
        sounds.starttune(TUNES.countdown5);
        sounds.waittunefinished();
        sounds.starttune(TUNES.countdown4);
        sounds.waittunefinished();
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
    


    sounds.starttune(TUNES.camelsong);
    #sounds.waittunefinished()
    time.sleep(4);
    sounds.starttune(TUNES.countdown5);
    time.sleep(0.1);
    sounds.starttune(TUNES.countdown4);
    time.sleep(0.1);
    sounds.starttune(TUNES.countdown3);
    time.sleep(0.1);
    sounds.starttune(TUNES.countdown2);
    time.sleep(0.1);
    sounds.starttune(TUNES.countdown1);
    sounds.waittunefinished()

