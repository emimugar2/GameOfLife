import pygame
import numpy as np
import time


pygame.init()


# Ancho y alto de la pantall
width, height = 1000, 1000

# Creación de la pantalla
screen = pygame.display.set_mode((height, width))

# Color del fondo = Casi negro, casi oscuro
bg = 25, 25, 25

# Pintamos el fondo con el color elegido
screen.fill(bg)

# Número de celdas
nxC, nyC = 25, 25

# Dimensión de la celda
dimCW = width / nxC
dimCH = height / nyC

# Estado de  las celdas. Vivas = 1; Muertas = 0
gameState = np.zeros((nxC, nyC))

# Autómata palo
gameState[5, 3] = 1
gameState[5, 4] = 1
gameState[5, 5] = 1

# Autómata movil
gameState[21, 21] = 1
gameState[22, 22] = 1
gameState[22, 23] = 1
gameState[21, 23] = 1
gameState[20, 23] = 1

# Bucle de ejecución
while True:

    newGameState = np.copy(gameState)

    screen.fill(bg)
    time.sleep(0.1)
    for y in range(0, nxC):
        for x in range(0, nyC):

            # Calculamos el número de vecinos cercanos
            n_neigh = gameState[(x - 1) % nxC, (y - 1) % nyC] + \
                gameState[(x) % nxC, (y - 1) % nyC] + \
                gameState[(x + 1) % nxC, (y - 1) % nyC] + \
                gameState[(x - 1) % nxC, (y) % nyC] + \
                gameState[(x + 1) % nxC, (y) % nyC] + \
                gameState[(x - 1) % nxC, (y + 1) % nyC] + \
                gameState[(x) % nxC, (y + 1) % nyC] + \
                gameState[(x + 1) % nxC, (y + 1) % nyC]

            # Rule #1 : Una célda muerta con exactamente 3 vecinas vivas, "revive"
            if gameState[x, y] == 0 and n_neigh == 3:
                newGameState[x, y] = 1

            # Rule #2: Una célda viva con menos de 2 o más de 3 vecinas vivas, "muere"
            if gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                newGameState[x, y] = 0

            # Creamos el polígono de cada celda a dibujar
            poly = [((x) * dimCW, y * dimCH),
                    ((x+1) * dimCW, y * dimCH),
                    ((x+1) * dimCW, (y+1) * dimCH),
                    ((x) * dimCW, (y+1) * dimCH)]

            # Y dibujamos la celda para cada par de x e y
            if newGameState[x, y] == 0:
                pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
            else:
                pygame.draw.polygon(screen, (255, 255, 255), poly, 0)

            # Actualizamos el estado del juego
            gameState = np.copy(newGameState)

    pygame.display.flip()
