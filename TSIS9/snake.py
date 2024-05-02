import random
import pygame
import sys
import time

# Инициализация Pygame
pygame.init()
pygame.font.init()

# Установка заголовка окна
pygame.display.set_caption("Snake Game")
# Ширина и высота игрового окна
SW, SH = 520, 520
# Размер блока игрового поля
BLOCK_SIZE = 40
# Создание игрового окна
SCREEN = pygame.display.set_mode((SW, SH + 40))

# Создание объекта Clock для управления временем
CLOCK = pygame.time.Clock()
# Создание объекта Font для отображения текста
FONT = pygame.font.Font("font.ttf", BLOCK_SIZE)

# Определение цветов в формате RGB
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# Класс, представляющий сегмент змеи
class SnakeST:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Класс, представляющий змею
class Snake:
    def __init__(self):
        self.body = [
            SnakeST(
                x=SW // BLOCK_SIZE // 2,
                y=SH // BLOCK_SIZE // 2,
            ),
        ]

    # Метод для отрисовки змеи
    def draw(self):
        head = self.body[0]

        pygame.draw.rect(
            SCREEN,
            GREEN,
            pygame.Rect(
                head.x * BLOCK_SIZE,
                head.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )

        for body in self.body[1:]:
            pygame.draw.rect(
                SCREEN,
                GREEN,
                pygame.Rect(
                    body.x * BLOCK_SIZE,
                    body.y * BLOCK_SIZE,
                    BLOCK_SIZE,
                    BLOCK_SIZE,
                )
            )

# Функция для отрисовки сетки на игровом поле
def draw_grid():
    for x in range(0, SW, BLOCK_SIZE):
        pygame.draw.line(SCREEN, WHITE, start_pos=(x, 0), end_pos=(x, SH), width=1)
    for y in range(0, SH, BLOCK_SIZE):
        pygame.draw.line(SCREEN, WHITE, start_pos=(0, y), end_pos=(SW, y), width=1)

    pygame.draw.line(SCREEN, WHITE, start_pos=(0, SH - 1), end_pos=(SW - 1, SH - 1), width=1)
    pygame.draw.line(SCREEN, WHITE, start_pos=(0, 0), end_pos=(0, SH), width=1)
    pygame.draw.line(SCREEN, WHITE, start_pos=(SW - 1, 0), end_pos=(SW - 1, SH - 1), width=1)
    pygame.draw.line(SCREEN, WHITE, start_pos=(0, 0), end_pos=(SW, 0), width=1)

# Функция завершения игры
def game_over():
    sys.exit()

# Главная функция игры
def main():
    # Создание объектов змеи и яблока
    snake = Snake()
    apple = Apple(5, 5)
    # Начальные параметры движения змеи
    dx = 0
    dy = 0
    movin = ''
    # Начальные значения счета и уровня
    score = 0
    LVL = 0
    # Переменные для управления появлением и исчезновением яблока
    spawn = time.perf_counter()
    dispawn = 0

    # Главный игровой цикл
    while True:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and movin != 'down':
                    movin = 'up'
                    dx, dy = 0, -1
                elif event.key == pygame.K_DOWN and movin != 'up':
                    movin = 'down'
                    dx, dy = 0, 1
                elif event.key == pygame.K_RIGHT and movin != 'left':
                    movin = 'right'
                    dx, dy = +1, 0
                elif event.key == pygame.K_LEFT and movin != 'right':
                    movin = 'left'
                    dx, dy = -1, 0
                elif event.key == pygame.K_q:
                    False

        # Движение змеи
        snake.move(dx, dy)

        # Проверка столкновения со змеей
        if snake.check_collision(apple):
            spawn = time.perf_counter()
            score += 1
            LVL = score // 5
            dispawn += apple.weight
            apple.generate_new(snake.body)
            snake.body.append(SnakeST(snake.body[-1].x, snake.body[-1].y))
            dispawn -= 1
        elif dispawn > 0:
            snake.body.append(SnakeST(snake.body[-1].x, snake.body[-1].y))
            dispawn -= 1

            apple.generate_new(snake.body)
            snake.body.append(
                SnakeST(snake.body[-1].x, snake.body[-1].y)
            )

        # Появление нового яблока через определенное время
        if time.perf_counter() - spawn > 5:
            spawn = time.perf_counter()
            apple.generate_new(snake.body)

        # Отображение счета и уровня на экране
        score_show = FONT.render('Score: ' + str(score), True, WHITE)
        level_show = FONT.render('LVL: ' + str(LVL), True, WHITE)

        # Очистка экрана
        SCREEN.fill(BLACK)
        # Отображение счета и уровня
        SCREEN.blit(score_show, (280, SH))
        SCREEN.blit(level_show, (70, SH))

        # Отрисовка змеи и яблока
        snake.draw()
        apple.draw()
        # Отрисовка сетки на игровом поле
        draw_grid()

        # Обновление экрана
        pygame.display.update()
        # Управление частотой кадров
        CLOCK.tick(4 + LVL*1.5)

# Запуск главной функции игры
if __name__ == "__main__":
    main()
