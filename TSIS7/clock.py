import pygame
import sys
import math
from datetime import datetime

pygame.init()  # Инициализация Pygame

WIDTH, HEIGHT = 400, 400  # Ширина и высота окна
CENTER = (WIDTH // 2, HEIGHT // 2)  # Координаты центра окна

screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Создание окна
pygame.display.set_caption("Analog Clock")  # Установка заголовка окна

# Загрузка изображений стрелок и фона часов
minute_hand_image = pygame.image.load("rhand.png")
minute_hand_image = pygame.transform.scale(minute_hand_image, (500, 500))

second_hand_image = pygame.image.load("lhand.png")
second_hand_image = pygame.transform.scale(second_hand_image, (500, 500))

background_image = pygame.image.load("sc.png")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Функция для отрисовки стрелки
def draw_hand(image, angle, length):
    if image is not None:  # Если передано изображение стрелки
        rotated_image = pygame.transform.rotate(image, -angle)  # Поворачиваем изображение
        rect = rotated_image.get_rect(center=CENTER)  # Получаем прямоугольник, описывающий изображение
        screen.blit(rotated_image, rect)  # Отображаем изображение на экране
    else:  # Если изображение не передано
        # Вычисляем конечные координаты стрелки
        end_x = CENTER[0] + length * math.cos(math.radians(angle - 90))
        end_y = CENTER[1] + length * math.sin(math.radians(angle - 90))
        # Рисуем линию (стрелку) на экране
        pygame.draw.line(screen, (0, 0, 0), CENTER, (end_x, end_y), 4)

while True:  # Основной игровой цикл
    for event in pygame.event.get():  # Обработка событий
        if event.type == pygame.QUIT:  # Если пользователь закрыл окно
            pygame.quit()  # Завершаем работу Pygame
            sys.exit()  # Завершаем программу

    screen.blit(background_image, (0, 0))  # Отображаем фон часов

    # Получаем текущее время
    current_time = datetime.now()
    hour = current_time.hour % 12
    minute = current_time.minute + 8
    second = current_time.second - 8

    # Отрисовка стрелок на часах
    draw_hand(None, (hour * 30) + (0.5 * minute), 80)  # Часовая стрелка
    draw_hand(minute_hand_image, minute * 6, 120)  # Минутная стрелка
    draw_hand(second_hand_image, second * 6, 140)  # Секундная стрелка

    pygame.display.flip()  # Обновляем экран
    pygame.time.Clock().tick(60)  # Ограничение частоты кадров
