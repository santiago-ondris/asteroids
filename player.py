import pygame 
from constants import *  
from circleshape import CircleShape  
from shot import Shot 

# Define la clase Player que hereda de CircleShape
class Player(CircleShape):
    def __init__(self, x, y):
        # Inicializa el jugador usando el constructor de CircleShape con su posición y radio
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0  # Define la rotación inicial del jugador
        self.shoot_timer = 0  # Temporizador para controlar el tiempo entre disparos

    def draw(self, screen):
        # Dibuja el jugador como un polígono que representa una nave espacial triangular
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def triangle(self):
        # Calcula los vértices del triángulo que representa la nave
        forward = pygame.Vector2(0, 1).rotate(self.rotation)  # Vector delantero de la nave
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5  # Vector de la derecha multiplicado por el radio
        
        # Calcula las posiciones de los tres vértices del triángulo
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def update(self, dt):
        # Actualiza el temporizador de disparo, reduciéndolo en el tiempo delta
        self.shoot_timer -= dt
        keys = pygame.key.get_pressed()  # Obtiene el estado de todas las teclas del teclado

        # Controla el movimiento y rotación de la nave según las teclas presionadas
        if keys[pygame.K_w]:
            self.move(dt)  # Mueve hacia adelante
        if keys[pygame.K_s]:
            self.move(-dt)  # Mueve hacia atrás
        if keys[pygame.K_a]:
            self.rotate(-dt)  # Rota a la izquierda
        if keys[pygame.K_d]:
            self.rotate(dt)  # Rota a la derecha
        if keys[pygame.K_SPACE]:
            self.shoot()  # Dispara un tiro si se presiona la barra espaciadora

    def shoot(self):
        # Comprueba si el jugador puede disparar basado en el temporizador de disparo
        if self.shoot_timer > 0:
            return
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN  # Reinicia el temporizador de disparo
        shot = Shot(self.position.x, self.position.y)  # Crea un nuevo disparo en la posición actual del jugador
        # Establece la velocidad del tiro en una dirección basada en la rotación del jugador
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

    def rotate(self, dt):
        # Ajusta la rotación del jugador basado en la velocidad de giro y el tiempo delta
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        # Mueve al jugador en la dirección hacia adelante multiplicado por su velocidad y tiempo delta
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

