import pygame, random


screen_width = 1080
screen_height = 720
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Resources/img/characters/airplane.png")
        self.rect = self.image.get_rect()

    def update(self,newX):
        self.rect.x = newX


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Resources/img/characters/enemy.png")
        self.rect = self.image.get_rect()

class Laser(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Resources/img/laser/laser.png")
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y -= 3

class Game(object):
    def __init__(self):
        self.score = 0

        self.enemies_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()
        self.lasers_list = pygame.sprite.Group()

        self.game_over = False
        self.start = False

        self.sound_laser = pygame.mixer.Sound("Resources/sound/laser_sound.wav")

        self.player = Player()

        self.all_sprites_list.add(self.player)
        # data player
        player_coor_x = 520
        player_coor_y = 620

        self.player.rect.x = player_coor_x
        self.player.rect.y = player_coor_y

        self.x = 50
        self.y = 0

        self.stars_white_coor_list = []
        self.stars_yellow_coor_list = []

        for i in range(30):
            x_star = random.randint(0, screen_width)
            y_star = random.randint(0, screen_height)
            self.stars_white_coor_list.append([x_star, y_star])

        for i in range(30):
            x_star = random.randint(0, screen_width)
            y_star = random.randint(0, screen_height)
            self.stars_yellow_coor_list.append([x_star, y_star])

        for j in range(3):
            for i in range(10):
                enemy = Enemy()
                enemy.rect.x = self.x
                self.x += 100
                enemy.rect.y = self.y
                self.enemies_list.add(enemy)
                self.all_sprites_list.add(enemy)
            self.y += 100
            self.x = 50
    def proccess_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                laser = Laser()
                laser.rect.x = self.player.rect.x + 1
                laser.rect.y = self.player.rect.y - 20
                self.sound_laser.play()

                self.all_sprites_list.add(laser)
                self.lasers_list.add(laser)

            if event.type == pygame.KEYDOWN:
                if not self.start:
                    self.start = True
                if self.game_over:
                    self.__init__()
        return False
    def run_controller(self):
        if not self.game_over:
            mouse_pos = pygame.mouse.get_pos()
            self.player.rect.x = mouse_pos[0]

            for i in self.lasers_list:
                i.update()
                enemie_hit_list = pygame.sprite.spritecollide(i, self.enemies_list,True)
                for enemy in enemie_hit_list:
                    self.all_sprites_list.remove(i)
                    self.lasers_list.remove(i)
                    self.score += 1
                if i.rect.y < -5:
                    self.all_sprites_list.remove(i)
                    self.lasers_list.remove(i)

            if len(self.enemies_list) == 0:
                self.game_over = True

    def display_frame(self, screen):
        screen.fill(BLACK)
        for coor in self.stars_white_coor_list:
            pygame.draw.circle(screen, WHITE, (coor[0], coor[1]), 2)
            coor[1] += 1
            if coor[1] > screen.get_height():
                coor[1] = 0

        for coor in self.stars_yellow_coor_list:
            pygame.draw.circle(screen, YELLOW, (coor[0], coor[1]), 2)
            coor[1] += 1
            if coor[1] > screen.get_height():
                coor[1] = 0
        if self.start:
            self.all_sprites_list.draw(screen)
        if not self.start:
            font = pygame.font.SysFont("arial", 30)
            text = font.render("PRESIONA CUALQUIER TECLA PARA EMPEZAR", True, WHITE)
            center_x = (screen_width // 2) - (text.get_width() // 2)
            center_y = (screen_height // 2) - (text.get_height() // 2)
            screen.blit(text, [center_x, center_y])
        if self.game_over:
            font = pygame.font.SysFont("arial", 25)
            text = font.render("VICTORIA (OBTUVISTE {} PUNTOS), PRESIONA CUALQUIER TECLA PARA CONTINUAR".format(self.score), True, WHITE)
            center_x = (screen_width//2)-(text.get_width()//2)
            center_y = (screen_height//2)-(text.get_height()//2)
            screen.blit(text,[center_x,center_y])
        if not self.game_over:
            pass

        pygame.display.flip()

def main():
    pygame.init()

    screen = pygame.display.set_mode([screen_width, screen_height])

    running = False
    clock = pygame.time.Clock()

    game = Game()
    speed = 1
    while not running:
        running = game.proccess_events()

        for j in game.enemies_list:
            j.rect.x += speed
            if j.rect.x > 1020 or j.rect.x < 0:
                speed *= -1

        game.run_controller()
        game.display_frame(screen)

        clock.tick(60)
    pygame.quit()
if __name__ == "__main__":
    main()