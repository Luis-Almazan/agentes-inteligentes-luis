import random
import time
import os

# Definir el entorno
entorno = [
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '#', '.', '#', '.', '#', '.', '.'],
    ['.', '.', '.', '#', '.', '.', '.', '.'],
    ['.', '#', '.', '.', '.', '#', '.', '.'],
    ['.', '.', '.', '#', '.', '.', '.', '.'],
]

# Posición inicial del agente
pos_x, pos_y = 0, 0
entorno[pos_x][pos_y] = 'A'

# Direcciones posibles de movimiento
direcciones = [(0, 1), (1, 0), (0, -1), (-1, 0)]
direccion_actual = 0  # Inicia moviéndose a la derecha

def imprimir_entorno():
    """Imprime el entorno en la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la consola
    for fila in entorno:
        print(" ".join(fila))
    print("\n")

while True:
    # Imprimir el entorno
    imprimir_entorno()
    time.sleep(0.5)

    # Calcular la nueva posición
    nueva_x = pos_x + direcciones[direccion_actual][0]
    nueva_y = pos_y + direcciones[direccion_actual][1]

    # Verificar si la nueva posición es válida
    if 0 <= nueva_x < len(entorno) and 0 <= nueva_y < len(entorno[0]) and entorno[nueva_x][nueva_y] != '#':
        # Mover el agente
        entorno[pos_x][pos_y] = '.'
        pos_x, pos_y = nueva_x, nueva_y
        entorno[pos_x][pos_y] = 'A'
    else:
        # Si hay un obstáculo, cambiar dirección aleatoriamente
        direccion_actual = random.randint(0, 3)
