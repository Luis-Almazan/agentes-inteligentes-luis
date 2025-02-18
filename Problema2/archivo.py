import random
import time

class AgenteBuscador:
    def __init__(self, size=5):
        self.size = size
        self.grid = [['_' for _ in range(size)] for _ in range(size)]
        self.agente_pos = [0, 0]  # El agente empieza en la esquina superior izquierda
        self.objeto_pos = [random.randint(0, size-1), random.randint(0, size-1)]
        self.grid[self.objeto_pos[0]][self.objeto_pos[1]] = 'O'  # Colocar objeto

    def mostrar_grid(self):
        for fila in self.grid:
            print(' '.join(fila))
        print()

    def mover_agente(self):
        while self.agente_pos != self.objeto_pos:
            self.grid[self.agente_pos[0]][self.agente_pos[1]] = '_'
            if self.agente_pos[0] < self.objeto_pos[0]:
                self.agente_pos[0] += 1
            elif self.agente_pos[0] > self.objeto_pos[0]:
                self.agente_pos[0] -= 1
            elif self.agente_pos[1] < self.objeto_pos[1]:
                self.agente_pos[1] += 1
            elif self.agente_pos[1] > self.objeto_pos[1]:
                self.agente_pos[1] -= 1
            
            self.grid[self.agente_pos[0]][self.agente_pos[1]] = 'A'
            self.mostrar_grid()
            time.sleep(1)

        print("¡Objeto encontrado!")

if __name__ == "__main__":
    agente = AgenteBuscador()
    agente.mostrar_grid()
    agente.mover_agente()
