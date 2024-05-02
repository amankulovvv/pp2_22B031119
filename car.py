import random, time

# Инициализация Pygame
pygame.init()

# Установка FPS (количество кадров в секунду) и создание экрана
FPS = 60
FramePerSec = pygame.time.Clock()
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game")

# Определение цветов
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Загрузка изображений и создание объектов для игры
background = pygame.image.load("Road.png")
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)


# Класс для врагов
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        # Движение врага вниз по экрану
        self.rect.move_ip(0, SPEED)
        # Если враг достигает нижней границы экрана, он появляется сверху
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


# Класс для обычной монеты
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Coin2.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        # Движение монеты вниз по экрану
        self.rect.move_ip(0, SPEED)
        # Если монета достигает нижней границы экрана, она появляется сверху
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


# Класс для серебряной монеты
class SilverCoin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("SilverCoin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        # Движение монеты вниз по экрану
        self.rect.move_ip(0, SPEED)
        # Если монета достигает нижней границы экрана, она появляется сверху
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


# Класс для игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        # Обработка нажатий клавиш: влево и вправо
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)


# Создание объектов игры
P1 = Player()
E1 = Enemy()
C1 = Coin()
C2 = SilverCoin()

# Создание групп спрайтов
enemies = pygame.sprite.Group()
enemies.add(E1)
coin = pygame.sprite.Group()
coin.add(C1)
silvcoin = pygame.sprite.Group()
silvcoin.add(C2)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
all_sprites.add(C2)

# Установка событий и таймеров
INC_SPEED = pygame.USEREVENT + 1
SPAWN_COIN = pygame.USEREVENT + 2
SPAWN_COIN2 = pygame.USEREVENT + 3
pygame.time.set_timer(INC_SPEED, 1000)
pygame.time.set_timer(SPAWN_COIN, 2000)
pygame.time.set_timer(SPAWN_COIN2, 2000)

# Основной игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.2
        if event.type == SPAWN_COIN:
            coin.add(C1)
            all_sprites.add(C1)
        if event.type == SPAWN_COIN2:
            silvcoin.add(C2)
            all_sprites.add(C2)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Отображение фона и счета
    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render("Coins: " + str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (300, 10))

    # Обновление и движение всех спрайтов
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # Обработка столкновений с монетами и врагами
    if pygame.sprite.spritecollideany(P1, coin):
        entity.kill()
        SCORE += 2
    if pygame.sprite.spritecollideany(P1, silvcoin):
        entity.kill()
        SCORE += 1
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
