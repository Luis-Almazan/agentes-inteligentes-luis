import os

# Definir el entorno con valores de recompensa
entorno = [
    [1, 3, 1, 5],
    [2, 2, 4, 1],
    [5, 0, 2, 3],
    [0, 6, 1, 2]
]

# Posición inicial y meta
inicio = (0, 0)
meta = (3, 3)

# Direcciones posibles: Derecha, Abajo
direcciones = [(0, 1), (1, 0)]

def imprimir_entorno(camino):
    """Muestra el entorno con la ruta óptima"""
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar consola
    for i in range(len(entorno)):
        for j in range(len(entorno[0])):
            if (i, j) in camino:
                print("*", end=" ")  # Marcar la ruta óptima
            else:
                print(entorno[i][j], end=" ")
        print()
    print("\n")

def buscar_mejor_ruta(x, y, recompensa_actual, camino_actual):
    """Busca la ruta con mayor recompensa acumulada usando DFS"""
    if (x, y) == meta:
        return (recompensa_actual, camino_actual + [(x, y)])

    mejor_recompensa = float('-inf')
    mejor_camino = []

    for dx, dy in direcciones:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(entorno) and 0 <= ny < len(entorno[0]):
            recompensa, camino = buscar_mejor_ruta(nx, ny, recompensa_actual + entorno[nx][ny], camino_actual + [(x, y)])
            if recompensa > mejor_recompensa:
                mejor_recompensa = recompensa
                mejor_camino = camino

    return mejor_recompensa, mejor_camino

# Encontrar la mejor ruta
_, mejor_camino = buscar_mejor_ruta(inicio[0], inicio[1], entorno[inicio[0]][inicio[1]], [])

# Imprimir la ruta óptima en el entorno
imprimir_entorno(mejor_camino)

print("Ruta óptima encontrada con mayor utilidad:", mejor_camino)
