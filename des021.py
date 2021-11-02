# Abrir e reproduzir um arquivo MP3

import pygame

print('='*5, ' DESAFIO 21 ', '='*5)
print('     ================  ')
print('\n \U0001F3B5  Python Player  \U0001F3B5')
print('\nMúsica: Radio Gaga \nArtista: Queen')

pygame.init()
pygame.mixer.music.load('radiogagaqueen.mp3')
pygame.mixer.music.play()
input()



