import pygame
import random

pygame.init() 

screen_width = 800
screen_height = 600

black = (0, 0, 0)  # Color negro
white = (255, 255, 255)
blue = (0, 0, 255)  
red = (255, 0, 0)

# Dimensiones de la pantalla (matriz de píxeles)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Atrapa objetos")

#SECCION JUGADOR

# propiedades del jugador
player_width = 100
player_height = 20
player_color = blue
player_speed = 2 

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


# movimiento

    keys = pygame.key.get_pressed() #detectar teclas

# mover jugador en base a teclas

    if keys[pygame.K_LEFT]: 
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += player_speed

# liimite movimiento jugador

    if player_rect.left < 0:
        player_rect.left = 0
    if player_rect.right > screen_width:
        player_rect.right = screen_width

    
# 1. Crear un nuevo objeto de vez en cuando
    
    if random.random() < 0.02:
        object_x = random.randint(0, SCREEN_WIDTH - OBJECT_WIDTH)
        new_object_rect = pygame.Rect(object_x, 0, OBJECT_WIDTH, OBJECT_HEIGHT)
        falling_objects.append(new_object_rect)
        
# 2. Mover cada objeto en la lista hacia abajo
    
    for obj_rect in falling_objects:
        obj_rect.y += OBJECT_SPEED


    screen.fill(black)

    # dibujar jugador
    pygame.draw.rect(screen, player_color, player_rect)


    pygame.display.flip()  # Actualizar la pantalla



pygame.quit()

print("Juego terminado")
