import pygame 
import random  # Importa el módulo random para generar números aleatorios
from constants import *  
from circleshape import CircleShape 

# Define la clase Asteroid que hereda de CircleShape
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)  # Llama al constructor de la clase padre CircleShape

    def draw(self, screen):
        # Dibuja el asteroide como un círculo blanco en la pantalla
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        # Actualiza la posición del asteroide basándose en su velocidad y el tiempo delta
        self.position += self.velocity * dt

    def split(self):
        # Elimina el asteroide actual antes de dividirlo
        self.kill()

        # Si el radius del asteroide es menor o igual al radio mínimo permitido, no hace nada
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Genera un ángulo aleatorio para dividir el asteroide
        random_angle = random.uniform(20, 50)

        # Calcula los nuevos vectores de dirección para los asteroides resultantes
        angle_rad1 = pygame.math.Vector2(1, 0).rotate(random_angle)
        angle_rad2 = pygame.math.Vector2(1, 0).rotate(-random_angle)

        # Determina el nuevo radio de los asteroides resultantes
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Calcula las nuevas velocidades para los dos asteroides
        new_velocity1 = self.velocity.rotate(random_angle) * 1.2
        new_velocity2 = self.velocity.rotate(-random_angle) * 1.2

        # Crea dos nuevos asteroides en la posición actual del asteroide original
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        # Asigna las nuevas velocidades a los nuevos asteroides
        new_asteroid1.velocity = new_velocity1
        new_asteroid2.velocity = new_velocity2

