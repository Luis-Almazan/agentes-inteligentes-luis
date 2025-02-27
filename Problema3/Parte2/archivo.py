from collections import deque
import os
import time

# Definir el laberinto (5x5)
laberinto = [
    ['A', '.', '#', '.', '.'],
    ['#', '.', '#', '.', '#'],
    ['.', '.', '.', '#', '.'],
    ['#', '#', '.', '#', '.'],
    ['.', '.', '.', '#', 'M']
]

# Direcciones posibles: Derecha, Abajo, Izquierda, Arriba
direcciones = [(0,1), (1,0), (0,-1), (-1,0)]

# Encontrar la posición inicial y la meta
for i in range(5):
    for j in range(5):
        if laberinto[i][j] == 'A':
            inicio = (i, j)
        elif laberinto[i][j] == 'M':
            meta = (i, j)

def imprimir_laberinto():
    """Muestra el laberinto en la consola"""
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar pantalla
    for fila in laberinto:
        print(" ".join(fila))
    print("\n")

def bfs(inicio, meta):
    """Encuentra la ruta más corta usando BFS"""
    cola = deque([(inicio, [])])  # (posición_actual, ruta_tomada)
    visitados = set()

    while cola:
        (x, y), ruta = cola.popleft()
        if (x, y) == meta:
            return ruta + [(x, y)]  # Retorna la ruta completa
        
        if (x, y) in visitados:
            continue
        
        visitados.add((x, y))

        for dx, dy in direcciones:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 5 and 0 <= ny < 5 and laberinto[nx][ny] != '#' and (nx, ny) not in visitados:
                cola.append(((nx, ny), ruta + [(x, y)]))

    return []  # No se encontró ruta

# Obtener la ruta más corta
ruta_corta = bfs(inicio, meta)

# Mostrar la ruta encontrada en el laberinto
for x, y in ruta_corta:
    if laberinto[x][y] not in ['A', 'M']:  # No sobreescribir inicio y meta
        laberinto[x][y] = '*'

# Imprimir el laberinto final con la ruta marcada
imprimir_laberinto()

print("Ruta encontrada y mostrada en el laberinto!")