import pygame, sys  # Импорт модулей pygame и sys
from pygame.locals import *  # Импорт всех констант и классов из pygame.locals
import random, time  # Импорт модулей random и time

pygame.init()  # Инициализация Pygame

FPS = 60  # Частота кадров в секунду
FramePerSec = pygame.time.Clock()  # Создание объекта Clock для управления частотой кадров

BLUE = (0, 0, 255)  # Определение цветов
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 400  # Ширина и высота экрана
SCREEN_HEIGHT = 600

SPEED = 5  # Скорость объектов в игре
SCORE = 0  # Текущее количество очков
level = 1  # Начальный уровень игрока

font = pygame.font.SysFont("Verdana", 60)  # Загрузка шрифтов для отображения текста
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)  # Создание текстовой надписи "Game Over"
level_up_text = font.render("Level Up!", True, GREEN)  # Текст для сообщения о переходе на следующий уровень
level_up_time = 0  # Время отображения сообщения о переходе на следующий уровень
level_up_duration = 2000  # Продолжительность отображения сообщения о переходе на следующий уровень (в миллисекундах)

background = pygame.image.load("Road.png")  # Загрузка изображения фона

DISPLAYSURF = pygame.display.set_mode((400, 600))  # Создание окна игры
DISPLAYSURF.fill(WHITE)  # Заливка фона белым цветом
pygame.display.set_caption("Game")  # Установка заголовка окна

# Определение классов для объектов в игре
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")  # Загрузка изображения врага
        self.rect = self.image.get_rect()  # Получение прямоугольника, ограничивающего изображение
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  # Установка начальной позиции врага

    def move(self):  # Метод для движения врага
        self.rect.move_ip(0, SPEED)  # Изменение координат для движения вниз
        if (self.rect.top > 600):  # Если враг выходит за нижнюю границу экрана
            self.rect.top = 0  # Перемещаем его вверх
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  # И устанавливаем новую позицию

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Coin2.png")  # Загрузка изображения монеты
        self.rect = self.image.get_rect()  # Получение прямоугольника, ограничивающего изображение
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  # Установка начальной позиции монеты

    def move(self):  # Метод для движения монеты
        global SCORE  # Объявление глобальной переменной SCORE
        self.rect.move_ip(0, SPEED)  # Изменение координат для движения вниз
        if (self.rect.top > 600):  # Если монета выходит за нижнюю границу экрана
            self.rect.top = 0  # Перемещаем её вверх
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  # И устанавливаем новую позицию

class SilverCoin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("SilverCoin.png")  # Загрузка изображения серебряной монеты
        self.rect = self.image.get_rect()  # Получение прямоугольника, ограничивающего изображение
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  # Установка начальной позиции серебряной монеты

    def move(self):  # Метод для движения серебряной монеты
        global SCORE  # Объявление глобальной переменной SCORE
        self.rect.move_ip(0, SPEED)  # Изменение координат для движения вниз
        if (self.rect.top > 600):  # Если монета выходит за нижнюю границу экрана
            self.rect.top = 0  # Перемещаем её вверх
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  # И устанавливаем новую позицию

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")  # Загрузка изображения игрока
        self.rect = self.image.get_rect()  # Получение прямоугольника, ограничивающего изображение
        self.rect.center = (160, 520)  # Установка начальной позиции игрока

    def move(self):  # Метод для движения игрока
        pressed_keys = pygame.key.get_pressed()  # Получение списка нажатых клавиш

        if self.rect.left > 0:  # Если игрок не находится слева от экрана
            if pressed_keys[K_LEFT]:  # Если нажата клавиша влево
                self.rect.move_ip(-5, 0)  # Перемещаем игрока влево на 5 пикселей
        if self.rect.right < SCREEN_WIDTH:  # Если игрок не находится справа от экрана
            if pressed_keys[K_RIGHT]:  # Если нажата клавиша вправо
                self.rect.move_ip(5, 0)  # Перемещаем игрока вправо на 5 пикселей

P1 = Player()  # Создание экземпляра класса Player (игрока)
E1 = Enemy()  # Создание экземпляра класса Enemy (врага)
C1 = Coin()  # Создание экземпляра класса Coin (монеты)
C2 = SilverCoin()  # Создание экземпляра класса SilverCoin (серебряной монеты)

enemies = pygame.sprite.Group()  # Создание группы для врагов
enemies.add(E1)  # Добавление врага в группу
coin = pygame.sprite.Group()  # Создание группы для монет
coin.add(C1)  # Добавление монеты в группу
silvcoin = pygame.sprite.Group()  # Создание группы для серебряных монет
silvcoin.add(C2)  # Добавление серебряной монеты в группу
all_sprites = pygame.sprite.Group()  # Создание общей группы для всех спрайтов
all_sprites.add(P1)  # Добавление игрока в общую группу
all_sprites.add(E1)  # Добавление врага в общую группу
all_sprites.add(C1)  # Добавление монеты в общую группу
all_sprites.add(C2)  # Добавление серебряной монеты в общую группу

INC_SPEED = pygame.USEREVENT + 1  # Создание пользовательского события для увеличения скорости
SPAWN_COIN = pygame.USEREVENT + 2  # Создание пользовательского события для появления монеты
SPAWN_COIN2 = pygame.USEREVENT + 3  # Создание пользовательского события для появления серебряной монеты
pygame.time.set_timer(INC_SPEED, 1000)  # Установка таймера для пользовательского события увеличения скорости
pygame.time.set_timer(SPAWN_COIN, 2000)  # Установка таймера для пользовательского события появления монеты
pygame.time.set_timer(SPAWN_COIN2, 2000)  # Установка таймера для пользовательского события появления серебряной монеты

while True:  # Основной игровой цикл
    for event in pygame.event.get():  # Обработка событий
        if event.type == INC_SPEED:  # Если произошло событие увеличения скорости
            SPEED += 0.2  # Увеличение скорости
        if event.type == SPAWN_COIN:  # Если произошло событие появления монеты
            coin.add(C1)  # Добавление монеты в группу
            all_sprites.add(C1)  # Добавление монеты в общую группу
        if event.type == SPAWN_COIN2:  # Если произошло событие появления серебряной монеты
            silvcoin.add(C2)  # Добавление серебряной монеты в группу
            all_sprites.add(C2)  # Добавление серебряной монеты в общую группу
        if event.type == pygame.QUIT:  # Если пользователь закрыл окно
            pygame.quit()  # Выход из Pygame
            sys.exit()  # Выход из программы

    DISPLAYSURF.blit(background, (0, 0))  # Отображение фона игры

    scores = font_small.render("Coins: " + str(SCORE), True, BLACK)  # Создание текста для отображения количества монет
    DISPLAYSURF.blit(scores, (300, 10))  # Отображение текста на экране

    for entity in all_sprites:  # Перебор всех спрайтов
        DISPLAYSURF.blit(entity.image, entity.rect)  # Отображение изображения спрайта на экране
        entity.move()  # Вызов метода move() для движения спрайта

    if pygame.sprite.spritecollideany(P1, coin):  # Если игрок столкнулся с монетой
        entity.kill()  # Удаление монеты
        SCORE += 2  # Увеличение счёта на 2

        if SCORE % 10 == 0:  # Если счёт кратен 10
            level += 1  # Увеличение уровня на 1
            level_up_time = pygame.time.get_ticks()  # Запуск таймера для отображения сообщения о переходе на следующий уровень

    if pygame.sprite.spritecollideany(P1, silvcoin):  # Если игрок столкнулся с серебряной монетой
        entity.kill()  # Удаление монеты
        SCORE += 1  # Увеличение счёта на 1

        if SCORE % 10 == 0:  # Если счёт кратен 10
            level += 1  # Увеличение уровня на 1
            level_up_time = pygame.time.get_ticks()  # Запуск таймера для отображения сообщения о переходе на следующий уровень
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
    if pygame.sprite.spritecollideany(P1, enemies):  # Если игрок столкнулся с врагом
        pygame.mixer.Sound('crash.wav').play()  # Проигрывание звука столкновения
        time.sleep(0.5)  # Пауза 0.5 секунды

        DISPLAYSURF.fill(RED)  # Заливка экрана красным цветом
        DISPLAYSURF.blit(game_over, (30, 250))  # Отображение текста "Game Over" на экране

        pygame.display.update()  # Обновление экрана
        for entity in all_sprites:  # Перебор всех спрайтов
            entity.kill()  # Удаление всех спрайтов
        time.sleep(2)  # Пауза 2 секунды
        pygame.quit()  # Выход из Pygame
        sys.exit()  # Выход из программы

    level_display = font_small.render("Level: " + str(level), True, BLACK)  # Создание текста для отображения текущего уровня
    DISPLAYSURF.blit(level_display, (10, 10))  # Отображение текста на экране

    if pygame.time.get_ticks() - level_up_time < level_up_duration:  # Если прошло меньше времени, чем продолжительность отображения сообщения
        DISPLAYSURF.blit(level_up_text, (100, 250))  # Отображение текста о переходе на следующий уровень на экране

    pygame.display.update()  # Обновление экрана
    FramePerSec.tick(FPS)  # Управление частотой кадров
