import time
import random

class SemaforoInteligente:
    def __init__(self):
        self.estado = "Rojo"
        self.tiempo_verde_base = 5  # Tiempo base en segundos para el verde
        self.tiempo_amarillo = 2    # Tiempo fijo en amarillo
        self.tiempo_rojo = 5        # Tiempo fijo en rojo

    def detectar_vehiculos(self):
        # Simula la detección de vehículos (aleatorio entre 0 y 10)
        return random.randint(0, 10)
    
    def ajustar_tiempo_verde(self, cantidad_vehiculos):
        return max(3, min(10, self.tiempo_verde_base + cantidad_vehiculos // 2))
    
    def cambiar_estado(self):
        while True:
            if self.estado == "Rojo":
                print("\nSemáforo en ROJO. Esperando...")
                time.sleep(self.tiempo_rojo)
                self.estado = "Verde"
            elif self.estado == "Verde":
                vehiculos = self.detectar_vehiculos()
                tiempo_verde = self.ajustar_tiempo_verde(vehiculos)
                print(f"\nSemáforo en VERDE ({tiempo_verde} segundos). {vehiculos} vehículos detectados.")
                time.sleep(tiempo_verde)
                self.estado = "Amarillo"
            elif self.estado == "Amarillo":
                print(f"\nSemáforo en AMARILLO ({self.tiempo_amarillo} segundos). Preparando cambio a rojo.")
                time.sleep(self.tiempo_amarillo)
                self.estado = "Rojo"

if __name__ == "__main__":
    semaforo = SemaforoInteligente()
    semaforo.cambiar_estado()