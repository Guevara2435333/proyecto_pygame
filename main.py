#Fundamentos Programacion Imperativa
#Proyecto Pygame
#Profesor: John Alexander Vargas
#Samuel David Sepulveda - 2435333
#Sebastian Muñoz Giraldo - 2516108



import pygame
import random
import time

pygame.init() 

screen_width = 700
screen_height = 800

black = (0, 0, 0)  # Color negro
white = (255, 255, 255)
blue = (0, 0, 255)  
red = (255, 0, 0)

# Dimensiones de la pantalla (matriz de píxeles)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Atrapa objetos")

#reloj y FPS:
clock = pygame.time.Clock()
FPS= 60

#PUNTUACIÓN Y TEXTO:
score = 0
lives = 5
font = pygame.font.Font(None,36)
game_over_font = pygame.font.Font(None, 72)

#SECCION JUGADOR

# propiedades del jugador
player_width = 100
player_height = 20
player_color = blue
player_speed = 25

# posicion inicio jugador
player_start_x = (screen_width / 2) - (player_width / 2)
# posicion y, la parte inferior menos un pequeño margen
player_start_y = screen_height - player_height - 20

# Rect (rectangulo) del jugador
player_rect = pygame.Rect(player_start_x, player_start_y, player_width, player_height)

#/FIN SECCION JUGADOR

#Sección de objetos:

#  DEFINICIÓN DE LOS OBJETOS QUE CAEN
object_width = 40
object_height = 40
object_color = red
object_speed = 5.7
# Esta es la lista que guardará todos los objetos que están en la pantalla.
falling_objects = []


#bucle principal
running = True
game_over = False
while running:
    #control de FPS: 
    clock.tick(FPS)
    
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

    
# Crear un nuevo objeto de vez en cuando
    
    if random.random() < 0.01:
        object_x = random.randint(0, screen_width- object_width)
        new_object_rect = pygame.Rect(object_x, 0, object_width, object_height)
        falling_objects.append(new_object_rect)
        
# Mover cada objeto en la lista hacia abajo
    
    for obj_rect in falling_objects[:]:
        obj_rect.y += object_speed
    #Comprobar si hay un choque con el jugador:
        if player_rect.colliderect(obj_rect):
            score += 1
            falling_objects.remove(obj_rect)
            print(f"¡Punto! Puntuación: {score}")
        elif obj_rect.top > screen_height:
            #perder vidas:
            lives -= 1
            print(f"¡Objeto perdido! Vidas restantes: {lives}")
            falling_objects.remove(obj_rect)
    
    # COMPROBAR CONDICIÓN PARA QUE FINALICE EL JUEGO:
    if lives <= 0:
        game_over = True
        running = False

    screen.fill(black)

    # dibujar jugador
    pygame.draw.rect(screen, player_color, player_rect)


#Dibujar objetos que quedan en la lista
    for obj_rect in falling_objects:
       pygame.draw.rect(screen, object_color, obj_rect)
           
#Dibujar la puntuación:
    
    score_surface = font.render(f"Puntuación: {score}", True, white)
    screen.blit(score_surface, (10, 10))

#Dibujar las vidas:
    lives_surface = font.render(f"Vidas: {lives}", True, white)
    screen.blit(lives_surface, (screen_width - lives_surface.get_width() - 10, 10))

    pygame.display.flip()  # Actualizar la pantalla

#Bucle para acabar el juego "GAME OVER":

if game_over:
    screen.fill(black)
    game_over_text = game_over_font.render("GAME OVER", True, red)
    final_score_text = font.render(f"Puntuación Final: {score}", True, white)

    game_over_rect = game_over_text.get_rect(center=(screen_width / 2, screen_height / 2 - 40))
    final_score_rect = final_score_text.get_rect(center=(screen_width / 2, screen_height / 2 + 40))

    screen.blit(game_over_text, game_over_rect)
    screen.blit(final_score_text, final_score_rect)


    pygame.display.flip()
    #espera 3 segundos antes de cerrar el juego
    time.sleep(3)
        


pygame.quit()

print("Juego terminado")

