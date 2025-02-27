# agentes-inteligentes-luis
Repositorio de agentes de IA

# Problema 1 
El código crea un semáforo inteligente que:
    Cambia de estado entre rojo, verde y amarillo.
    Simula la detección de vehículos y ajusta el tiempo de espera del verde según el tráfico.
    Imprime el estado actual del semáforo en cada cambio.

# Problema 2
El código en Python implementa un agente buscador de objetos en una cuadrícula 5x5:
    Representa el entorno con una matriz.
    Mueve al agente en cada iteración hasta que alcance el objeto.
    Muestra la cuadrícula en cada movimiento para visualizar el proceso.

# Problema 3 
El codigo Muestra una lisgit sta de síntomas disponibles (Ej: fiebre, tos, dolor de cabeza, etc.).
    El usuario elige síntomas ingresando los números correspondientes separados por comas.
    El sistema evalúa la selección usando reglas predefinidas.
    Devuelve un posible diagnóstico basado en los síntomas ingresados.
    Si no encuentra coincidencias, recomienda visitar a un médico.

# Problema 4 
El código en Python implementa un agente de recomendación de películas basado en el género favorito del usuario.
    Define un diccionario con películas organizadas por género.
    Muestra una lista de géneros disponibles para que el usuario seleccione uno.
    El usuario elige un número correspondiente a su género favorito.
    El sistema selecciona aleatoriamente una película del género elegido y la muestra como recomendación.

## Agentes Inteligentes Parte 2

## Agente de Patrullaje (Reflejo Simple)
# Problema 1 
El código en Python implementa un agente de patrullaje reflejo simple que se mueve por un entorno predefinido y reacciona ante obstáculos cambiando su dirección.
    Define un entorno en una matriz con caminos (.), obstáculos (#) y el agente (A).
    El agente se mueve en una dirección fija, siguiendo una ruta predefinida.
    Si detecta un obstáculo, cambia de dirección aleatoriamente.
    Muestra el entorno en la consola y actualiza la posición del agente en un bucle continuo.

## Agente Explorador de Mapas (Con Estado Interno)
# Problema 2 
El código en Python implementa un agente explorador de mapas con estado interno que navega por un entorno representado como una cuadrícula, evitando repetir caminos ya visitados.
    Define un entorno como una matriz con caminos (.) y obstáculos (#).
    El agente se mueve evitando obstáculos y posiciones ya exploradas, almacenando su historial en una lista.
    Busca nuevas rutas disponibles y avanza aleatoriamente, evitando retroceder innecesariamente.
    Muestra el entorno en la consola en cada paso y se detiene cuando no hay más caminos por explorar.

# Agente de Navegación Autónoma (Basado en Metas)
# Problema 3 
El código en Python implementa un agente de navegación autónoma que encuentra la ruta más corta en un laberinto usando búsqueda en anchura (BFS).
    Define un laberinto con paredes (#) y una meta (M).
    Usa BFS para calcular el camino más corto hasta la salida.
    Muestra la ruta encontrada (*) en la consola paso a paso.

# Agente de Selección de Rutas (Basado en Utilidad)
# Problema 4 
El código en Python implementa un agente de selección de rutas basado en utilidad que encuentra el camino con la mayor recompensa acumulada.
    Define una cuadrícula con valores de recompensa en cada celda.
    Usa búsqueda en profundidad (DFS) para evaluar caminos posibles.
    Selecciona y muestra la ruta óptima en la consola.