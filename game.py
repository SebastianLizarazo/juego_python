import pygame
import random

# Dimensiones de la ventana del juego
screen_width = 1080
screen_height = 720

# Definición de colores en formato RGB
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

# Clase Player: representa el jugador en el juego


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Carga la imagen del avión desde la carpeta Resources
        self.image = pygame.image.load("Resources/img/characters/airplane.png")
        # Obtiene el rectángulo delimitador para manejar la posición y colisiones
        self.rect = self.image.get_rect()

    def update(self, newX):
        # Actualiza la posición horizontal del jugador según el valor recibido
        self.rect.x = newX

# Clase Enemy: representa un enemigo en el juego


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Carga la imagen del enemigo
        self.image = pygame.image.load("Resources/img/characters/enemy.png")
        # Obtiene el rectángulo delimitador del enemigo
        self.rect = self.image.get_rect()

# Clase Laser: representa un proyectil disparado por el jugador


class Laser(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Carga la imagen del láser
        self.image = pygame.image.load("Resources/img/laser/laser.png")
        # Obtiene el rectángulo delimitador del láser
        self.rect = self.image.get_rect()

    def update(self):
        # Mueve el láser hacia arriba disminuyendo la coordenada y
        self.rect.y -= 3

# Clase Game: maneja la lógica y estados del juego


class Game(object):
    def __init__(self):
        # Inicializa el puntaje
        self.score = 0

        # Grupos de sprites para enemigos, láseres y todos los elementos del juego
        self.enemies_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()
        self.lasers_list = pygame.sprite.Group()

        # Estados del juego: 'game_over' indica si el juego terminó y 'start' si ha iniciado
        self.game_over = False
        self.start = False

        # Carga el sonido del láser
        self.sound_laser = pygame.mixer.Sound(
            "Resources/sound/laser_sound.wav")

        # Crea el jugador y lo posiciona en la pantalla
        self.player = Player()
        self.all_sprites_list.add(self.player)
        player_coor_x = 520
        player_coor_y = 620
        self.player.rect.x = player_coor_x
        self.player.rect.y = player_coor_y

        # Variables para posicionar a los enemigos
        self.x = 50
        self.y = 0

        # Listas para almacenar coordenadas de estrellas que se muestran en el fondo
        self.stars_white_coor_list = []
        self.stars_yellow_coor_list = []

        # Genera 30 estrellas blancas en posiciones aleatorias
        for i in range(30):
            x_star = random.randint(0, screen_width)
            y_star = random.randint(0, screen_height)
            self.stars_white_coor_list.append([x_star, y_star])

        # Genera 30 estrellas amarillas en posiciones aleatorias
        for i in range(30):
            x_star = random.randint(0, screen_width)
            y_star = random.randint(0, screen_height)
            self.stars_yellow_coor_list.append([x_star, y_star])

        # Crea una formación de enemigos: 3 filas de 10 enemigos cada una
        for j in range(3):
            for i in range(10):
                enemy = Enemy()
                enemy.rect.x = self.x
                self.x += 100  # Espacio horizontal entre enemigos
                enemy.rect.y = self.y
                self.enemies_list.add(enemy)
                self.all_sprites_list.add(enemy)
            self.y += 100  # Moverse a la siguiente fila verticalmente
            self.x = 50    # Reiniciar la posición horizontal para la nueva fila

    def proccess_events(self):
        # Procesa los eventos de entrada del usuario
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Finaliza el juego si se cierra la ventana
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:  # pylint: disable=no-member
                # Al hacer clic, dispara un láser y reproduce el sonido correspondiente
                laser = Laser()
                laser.rect.x = self.player.rect.x + 1
                laser.rect.y = self.player.rect.y - 20
                self.sound_laser.play()
                self.all_sprites_list.add(laser)
                self.lasers_list.add(laser)
            if event.type == pygame.KEYDOWN:
                # Inicia el juego si no ha comenzado y reinicia si ya terminó
                if not self.start:
                    self.start = True
                if self.game_over:
                    self.__init__()
        return False

    def run_controller(self):
        # Controla la lógica principal del juego (movimientos y colisiones)
        if not self.game_over:
            # Actualiza la posición del jugador según la posición del mouse
            mouse_pos = pygame.mouse.get_pos()
            self.player.rect.x = mouse_pos[0]

            # Actualiza la posición de los láseres y verifica colisiones con enemigos
            for i in self.lasers_list:
                i.update()
                enemie_hit_list = pygame.sprite.spritecollide(
                    i, self.enemies_list, True)
                for enemy in enemie_hit_list:
                    # Elimina el láser al impactar y suma puntos
                    self.all_sprites_list.remove(i)
                    self.lasers_list.remove(i)
                    self.score += 1
                # Elimina el láser si sale de la pantalla
                if i.rect.y < -5:
                    self.all_sprites_list.remove(i)
                    self.lasers_list.remove(i)

            # Si se han eliminado todos los enemigos, se marca el juego como terminado
            if len(self.enemies_list) == 0:
                self.game_over = True

    def display_frame(self, screen):
        # Renderiza cada cuadro del juego
        screen.fill(BLACK)

        # Dibuja y mueve las estrellas blancas en el fondo
        for coor in self.stars_white_coor_list:
            pygame.draw.circle(screen, WHITE, (coor[0], coor[1]), 2)
            coor[1] += 1
            if coor[1] > screen.get_height():
                coor[1] = 0

        # Dibuja y mueve las estrellas amarillas en el fondo
        for coor in self.stars_yellow_coor_list:
            pygame.draw.circle(screen, YELLOW, (coor[0], coor[1]), 2)
            coor[1] += 1
            if coor[1] > screen.get_height():
                coor[1] = 0

        # Si el juego ha iniciado, dibuja todos los sprites
        if self.start:
            self.all_sprites_list.draw(screen)
        # Si el juego no ha iniciado, muestra un mensaje de inicio
        if not self.start:
            font = pygame.font.SysFont("arial", 30)
            text = font.render(
                "PRESIONA CUALQUIER TECLA PARA EMPEZAR", True, WHITE)
            center_x = (screen_width // 2) - (text.get_width() // 2)
            center_y = (screen_height // 2) - (text.get_height() // 2)
            screen.blit(text, [center_x, center_y])
        # Si el juego ha terminado, muestra el puntaje y un mensaje de victoria
        if self.game_over:
            font = pygame.font.SysFont("arial", 25)
            text = font.render("VICTORIA (OBTUVISTE {} PUNTOS), PRESIONA CUALQUIER TECLA PARA CONTINUAR".format(
                self.score), True, WHITE)
            center_x = (screen_width // 2) - (text.get_width() // 2)
            center_y = (screen_height // 2) - (text.get_height() // 2)
            screen.blit(text, [center_x, center_y])

        pygame.display.flip()

# Función principal: inicializa y ejecuta el bucle del juego


def main():
    pygame.init()
    # Configura la ventana del juego
    screen = pygame.display.set_mode([screen_width, screen_height])
    clock = pygame.time.Clock()

    game = Game()
    speed = 1
    running = False
    # Bucle principal del juego
    while not running:
        running = game.proccess_events()

        # Mueve los enemigos de lado a lado, invirtiendo la dirección al llegar a los bordes
        for j in game.enemies_list:
            j.rect.x += speed
            if j.rect.x > 1020 or j.rect.x < 0:
                speed *= -1

        game.run_controller()
        game.display_frame(screen)
        clock.tick(60)  # Limita la velocidad a 60 FPS

    pygame.quit()


if __name__ == "__main__":
    main()
