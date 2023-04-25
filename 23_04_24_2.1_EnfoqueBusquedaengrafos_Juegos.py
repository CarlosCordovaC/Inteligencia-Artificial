import pygame
import random

# Inicializar Pygame
pygame.init()

# Configuración de la ventana del juego
width = 640
height = 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Laberinto")

# Colores
black = (0, 0, 0)
white = (255, 255, 255)

# Tamaño de la celda del laberinto
cell_size = 40

# Generar un laberinto aleatorio
maze_width = int(width / cell_size)
maze_height = int(height / cell_size)
maze = [[random.randint(0, 1) for y in range(maze_height)] for x in range(maze_width)]

# Posición inicial del jugador
player_x = 0
player_y = 0

# Ciclo principal del juego
game_running = True
while game_running:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    # Dibujar el laberinto
    for x in range(maze_width):
        for y in range(maze_height):
            if maze[x][y] == 1:
                pygame.draw.rect(screen, white, (x * cell_size, y * cell_size, cell_size, cell_size))
            else:
                pygame.draw.rect(screen, black, (x * cell_size, y * cell_size, cell_size, cell_size))

    # Dibujar al jugador
    pygame.draw.circle(screen, (255, 0, 0), (player_x * cell_size + cell_size/2, player_y * cell_size + cell_size/2), cell_size/3)

    # Actualizar la pantalla
    pygame.display.update()

# Salir de Pygame
pygame.quit()
