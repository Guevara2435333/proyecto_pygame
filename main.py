import pygame
import random

pygame.init()  

black = (0, 0, 0)  # Color negro

# Dimensiones de la pantalla (matriz de píxeles)
pygame.display.set_caption("Juego de atrapa objetos")
screen = pygame.display.set_mode((800, 600))

#bucle principal
running = True
while running:
    for event in pygame.event.get():

        # Si se cierra la ventana, salir del bucle
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)

    pygame.display.flip()  # Actualizar la pantalla



pygame.quit()

print("Juego terminado")