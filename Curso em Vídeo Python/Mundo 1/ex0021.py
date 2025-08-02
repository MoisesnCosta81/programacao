# Faça um programa em python que abrar e reproduza o áudio de um
# arquivo MP3.

import pygame
pygame.init()
pygame.mixer.music.load('ex0021.mp3')
#set_volume(de 0.0 a 1.0) - ajusta o volume da execução
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play()
input()
pygame.event.wait()
#atualização no pygame exige a inclusão de input()

