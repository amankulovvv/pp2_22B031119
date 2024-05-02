import pygame, sys  # Импорт библиотек Pygame и sys для создания игры и работы с системными функциями
from pygame.locals import *  # Импорт всех констант и функций Pygame
import random, time  # Импорт модулей random и time для работы с рандомом и временем

pygame.init()  # Инициализация Pygame

FPS = 60  # Задание частоты кадров в секунду
FramePerSec = pygame.time.Clock()  # Создание объекта Clock для управления частотой кадров
SPEED = 5  # Задание начальной скорости движения объектов
SCORE = 0  # Задание начального количества очков

# Определение цветов
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Задание размеров экрана
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Загрузка фонового изображения и создание окна
background = pygame.image.load("Road.png")
DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

# Класс для создания вражеских объектов
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  # Вызов конструктора родительского класса
        self.image = pygame.image.load("Enemy.png")  # Загрузка изображения врага
        self.rect = self.image.get_rect()  # Получение прямоугольника, описывающего область изображения
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  # Задание начальной позиции врага

    # Метод для движения врага
    def move(self):
        self.rect.move_ip(0, SPEED)  # Изменение позиции врага вниз
        if (self.rect.top > 600):  # Если враг выходит за границы экрана внизу
            self.rect.top = 0  # Перемещаем его вверх экрана
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  # Задаем случайное положение вверху

# Класс для создания монет
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  # Вызов конструктора родительского класса
        self.image = pygame.image.load("Coin2.png")  # Загрузка изображения монеты
        self.rect = self.image.get_rect()  # Получение прямоугольника, описывающего область изображения
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  # Задание начальной позиции монеты

    # Метод для движения монеты
    def move(self):
        global SCORE  # Используем глобальную переменную SCORE
        self.rect.move_ip(0, SPEED)  # Изменение позиции монеты вниз
        if (self.rect.top > 600):  # Если монета выходит за границы экрана внизу
            self.rect.top = 0  # Перемещаем ее вверх экрана
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  # Задаем случайное положение вверху

# Класс для создания игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  # Вызов конструктора родительского класса
        self.image = pygame.image.load("Player.png")  # Загрузка изображения игрока
        self.rect = self.image.get_rect()  # Получение прямоугольника, описывающего область изображения
        self.rect.center = (160, 520)  # Задание начальной позиции игрока

    # Метод для движения игрока
    def move(self):
        pressed_keys = pygame.key.get_pressed()  # Получаем список нажатых клавиш
        if self.rect.left > 0:  # Если игрок не вышел за левую границу экрана
            if pressed_keys[K_LEFT]:  # Если нажата клавиша "влево"
                self.rect.move_ip(-5, 0)  # Двигаем игрока влево
        if self.rect.right < SCREEN_WIDTH:  # Если игрок не вышел за правую границу экрана
            if pressed_keys[K_RIGHT]:  # Если нажата клавиша "вправо"
                self.rect.move_ip(5, 0)  # Двигаем игрока вправо

# Создание экземпляров игрока и врагов
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Создание групп спрайтов
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

# Установка таймеров для увеличения скорости и создания монет
INC_SPEED = pygame.USEREVENT + 1
SPAWN_COIN = pygame.USEREVENT + 2
pygame.time.set_timer(INC_SPEED, 1000)
pygame.time.set_timer(SPAWN_COIN, 3000)

# Основной игровой цикл
while True:
    for event in pygame.event.get():  # Обработка событий
        if event.type == INC_SPEED:  # Если событие - увеличение скорости
            SPEED += 0.2  # Увеличиваем скорость движения объектов
        if event.type == SPAWN_COIN:  # Если событие - создание монеты
            coins.add(Coin())  # Добавляем монету в группу
            all_sprites.add(Coin())  # Добавляем монету в общую группу спрайтов
        if event.type == QUIT:  # Если событие - выход из игры
            pygame.quit()  # Завершаем Pygame
            sys.exit()  # Завершаем программу

    DISPLAYSURF.blit(background, (0, 0))  # Отображаем фоновое изображение

    scores = font_small.render("Coins: " + str(SCORE), True, BLACK)  # Создаем изображение счета
    DISPLAYSURF.blit(scores, (300, 10))  # Отображаем счет игрока на экране

    for entity in all_sprites:  # Обработка движения всех спрайтов и их отображение на экране
        DISPLAYSURF.blit(entity.image, entity.rect)  # Отображаем спрайт на экране
        entity.move()  # Двигаем спрайт

    # Обработка столкновений игрока с монетами
    if pygame.sprite.spritecollideany(P1, coins):  # Если игрок сталкивается с монетой
        entity.kill()  # Удаляем монету
        SCORE += 1  # Увеличиваем счет игрока

    # Обработка столкновений игрока с врагами
    if pygame.sprite.spritecollideany(P1, enemies):  # Если игрок сталкивается с врагом
        pygame.mixer.Sound('crash.wav').play()  # Проигрываем звук столкновения
        time.sleep(0.5)  # Пауза перед завершением игры
        DISPLAYSURF.fill(RED)  # Заливаем экран красным цветом
        DISPLAYSURF.blit(game_over, (30, 250))  # Отображаем надпись "Game Over"
        pygame.display.update()  # Обновляем экран
        for entity in all_sprites:  # Удаляем все спрайты
            entity.kill() 
        time.sleep(2)  # Пауза перед выходом из программы
        pygame.quit()  # Завершаем Pygame
        sys.exit()  # Завершаем программу

    pygame.display.update()  # Обновление экрана
    FramePerSec.tick(FPS)  # Ограничение частоты кадров
