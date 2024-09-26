import sys  # Importa el módulo sys para salir del programa si es necesario
import pygame  # Importa el módulo pygame para interactuar con gráficos y sonido
from constants import *  # Importa todas las constantes
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField 
from shot import Shot 


def main():
    pygame.init()  # Inicializa todos los módulos de pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Crea la ventana del juego con las dimensiones especificadas
    clock = pygame.time.Clock()  # Crea un objeto Clock para controlar el tiempo del juego

    # Define diferentes grupos de sprites para actualizar y dibujar
    updatable = pygame.sprite.Group()  # Grupo para objetos que necesitan ser actualizados
    drawable = pygame.sprite.Group()  # Grupo para objetos que necesitan ser dibujados
    asteroids = pygame.sprite.Group()  # Grupo específicamente para asteroides
    shots = pygame.sprite.Group()  # Grupo específicamente para disparos

    # Asigna contenedores de grupo a las clases correspondientes
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()  # Crea un campo de asteroides

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  # Crea un jugador en el centro de la pantalla

    dt = 0  # Delta time para medir el tiempo entre frames

    while True:  # Bucle principal del juego
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:  # Sale si la ventana se cierra
                return

        for obj in updatable:  # Actualiza cada objeto en el grupo updatable
            obj.update(dt)

        for asteroid in asteroids:  # Comprueba colisiones de asteroides
            if asteroid.collides_with(player):  # Colisión con el jugador
                print("Game over!")
                sys.exit()

            for shot in shots:  # Comprueba colisiones con disparos
                if asteroid.collides_with(shot):
                    shot.kill()  # Elimina el disparo
                    asteroid.split()  # Divide el asteroide

        screen.fill("black")  # Limpia la pantalla con color negro

        for obj in drawable:  # Dibuja cada objeto en el grupo drawable
            obj.draw(screen)

        pygame.display.flip()  # Actualiza la pantalla

        dt = clock.tick(60) / 1000  # Controla la velocidad de fotogramas a 60 FPS y calcula el tiempo delta


if __name__ == "__main__":  # Asegura que la función main se ejecute solo si el script se ejecuta directamente
    main()


