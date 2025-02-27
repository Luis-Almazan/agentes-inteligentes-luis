import random
import time
import os

# Definir el entorno (mapa)
entorno = [
    ['.', '.', '.', '#', '.', '.'],
    ['.', '#', '.', '.', '.', '.'],
    ['.', '.', '#', '.', '#', '.'],
    ['#', '.', '.', '.', '.', '.'],
    ['.', '.', '#', '.', '.', '.']
]

# Posición inicial del agente
pos_x, pos_y = 0, 0
entorno[pos_x][pos_y] = 'A'

# Lista de posiciones visitadas
visitadas = {(pos_x, pos_y)}

# Posibles direcciones de movimiento (derecha, abajo, izquierda, arriba)
direcciones = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def imprimir_entorno():
    """Imprime el entorno en la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la consola
    for fila in entorno:
        print(" ".join(fila))
    print("\n")

while True:
    imprimir_entorno()
    time.sleep(0.5)

    # Encontrar direcciones válidas (sin obstáculos y no visitadas)
    movimientos_validos = []
    for dx, dy in direcciones:
        nueva_x, nueva_y = pos_x + dx, pos_y + dy
        if (0 <= nueva_x < len(entorno) and 
            0 <= nueva_y < len(entorno[0]) and 
            entorno[nueva_x][nueva_y] == '.' and 
            (nueva_x, nueva_y) not in visitadas):
            movimientos_validos.append((nueva_x, nueva_y))

    # Si hay movimientos válidos, elige uno aleatorio y avanza
    if movimientos_validos:
        entorno[pos_x][pos_y] = '.'  # Marcar como explorado
        pos_x, pos_y = random.choice(movimientos_validos)
        entorno[pos_x][pos_y] = 'A'
        visitadas.add((pos_x, pos_y))
    else:
        # Si no hay movimientos válidos, el agente se detiene
        print("No hay más caminos por explorar.")
        break
