import pygame

# Inicializar Pygame
pygame.init()

# Configuración de la ventana del juego
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Juego de Rebote")

# Colores
white = (255, 255, 255)
blue = (0, 0, 255)

# Posición y velocidad de la bola
ball_x = 50
ball_y = 50
ball_speed_x = 5
ball_speed_y = 5

# Game loop
running = True
while running:
    # Procesar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Actualizar posición de la bola
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Rebotar la bola cuando llega a los límites de la ventana
    if ball_x < 0 or ball_x > width:
        ball_speed_x *= -1
    if ball_y < 0 or ball_y > height:
        ball_speed_y *= -1

    # Limpiar la pantalla
    screen.fill(white)

    # Dibujar la bola en la pantalla
    pygame.draw.circle(screen, blue, (ball_x, ball_y), 20)

    # Actualizar la pantalla
    pygame.display.flip()

# Cerrar Pygame
pygame.quit()
