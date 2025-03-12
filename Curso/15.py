# abra e reproduza um audio em mp3
import pygame

pygame.init()
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play()
pygame.event.wait()