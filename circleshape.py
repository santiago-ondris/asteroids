import pygame 

# Define la clase CircleShape que hereda de pygame.sprite.Sprite
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # Verifica si el objeto tiene un atributo "containers", que es común en grupos de sprites
        if hasattr(self, "containers"):
            super().__init__(self.containers)  # Inicializa el sprite con sus contenedores
        else:
            super().__init__()  # Inicialización estándar si no hay contenedores

        # Establece la posición inicial del círculo como un vector bidimensional
        self.position = pygame.Vector2(x, y)
        # Inicializa la velocidad del círculo como un vector (dirigido inicialmente al origen)
        self.velocity = pygame.Vector2(0, 0)
        # Establece el radio del círculo
        self.radius = radius

    def draw(self, screen):
        # Método que debe ser sobrescrito en subclases para dibujar el círculo en la pantalla
        pass

    def update(self, dt):
        # Método que debe ser sobrescrito en subclases para actualizar el estado del círculo
        pass

    def collides_with(self, other):
        # Determina si el círculo actual colisiona con otro basado en la distancia entre sus posiciones
        return self.position.distance_to(other.position) <= self.radius + other.radius

