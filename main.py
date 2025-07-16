import pygame
import random

pygame.init() 

screen_width = 800
screen_height = 600

black = (0, 0, 0)  # Color negro
white = (255, 255, 255)
blue = (0, 0, 255)  

# Dimensiones de la pantalla (matriz de píxeles)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Juego de atrapa objetos")

#SECCION JUGADOR

# propiedades del jugador
player_width = 100
player_height = 20
player_color = blue

# posicion inicio jugador
player_start_x = (screen_width / 2) - (player_width / 2)
# posicion y, la parte inferior menos un pequeño margen
player_start_y = screen_height - player_height - 20

# Rect (rectangulo) del jugador
player_rect = pygame.Rect(player_start_x, player_start_y, player_width, player_height)

#/FIN SECCION JUGADOR

#bucle principal
running = True
while running:
    for event in pygame.event.get():

        # Si se cierra la ventana, salir del bucle
        if event.type == pygame.QUIT:
            running = False


    screen.fill(black)

    # dibujar jugador
    pygame.draw.rect(screen, player_color, player_rect)


    pygame.display.flip()  # Actualizar la pantalla



pygame.quit()

print("Juego terminado")