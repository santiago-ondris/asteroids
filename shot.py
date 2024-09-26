import pygame 
from constants import *  
from circleshape import CircleShape  

# Define la clase Shot que hereda de CircleShape
class Shot(CircleShape):
    def __init__(self, x, y):
        # Inicializa un disparo en la posición (x, y) con el radio definido para disparos
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        # Dibuja el disparo como un círculo blanco en la pantalla
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        # Actualiza la posición del disparo según su velocidad y el tiempo delta
        self.position += self.velocity * dt