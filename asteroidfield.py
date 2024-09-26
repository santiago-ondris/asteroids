import pygame 
import random 
from asteroid import Asteroid  
from constants import *

# Define la clase AsteroidField que hereda de pygame.sprite.Sprite
class AsteroidField(pygame.sprite.Sprite):
    # Define los bordes de la pantalla desde donde los asteroides pueden emerger
    edges = [
        [
            pygame.Vector2(1, 0),  # Movimiento a la derecha
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),  # Movimiento a la izquierda
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),  # Movimiento hacia abajo
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),  # Movimiento hacia arriba
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ],
    ]

    def __init__(self):
        # Inicializa el sprite mediante la inicialización de la clase base
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0  # Temporizador para controlar la frecuencia de aparición de asteroides

    def spawn(self, radius, position, velocity):
        # Crea un nuevo asteroide en la posición y con la velocidad indicada
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity

    def update(self, dt):
        # Actualiza el temporizador de aparición basado en el tiempo delta
        self.spawn_timer += dt
        if self.spawn_timer > ASTEROID_SPAWN_RATE:
            self.spawn_timer = 0  # Resetea el temporizador cuando alcanza el umbral para crear un nuevo asteroide

            # Selecciona aleatoriamente un borde de la pantalla para crear un nuevo asteroide
            edge = random.choice(self.edges)
            speed = random.randint(40, 100)  # Velocidad aleatoria del asteroide
            velocity = edge[0] * speed  # Calcula la dirección de la velocidad basada en el borde seleccionado
            velocity = velocity.rotate(random.randint(-30, 30))  # Rotación aleatoria adicional
            position = edge[1](random.uniform(0, 1))  # Calcula la posición de inicio en el borde
            kind = random.randint(1, ASTEROID_KINDS)  # Determina el tipo de asteroide
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)  # Llama al método spawn para crear el asteroide
