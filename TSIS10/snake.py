import sqlite3  # Импорт модуля для работы с базой данных SQLite
import random  # Импорт модуля для генерации случайных чисел
import pygame  # Импорт модуля для создания графического интерфейса игры
import sys  # Импорт модуля для завершения программы

pygame.init()  # Инициализация Pygame
pygame.font.init()  # Инициализация модуля для работы с шрифтами Pygame

# Установка заголовка окна игры, определение размеров окна и создание окна
pygame.display.set_caption("Змейка")
SW, SH = 520, 520  # Задание ширины и высоты окна
BLOCK_SIZE = 40  # Задание размера блока
SCREEN = pygame.display.set_mode((SW, SH + 40))  # Создание окна игры

CLOCK = pygame.time.Clock()  # Создание объекта для отслеживания времени
FONT = pygame.font.Font("font.ttf", BLOCK_SIZE)  # Загрузка шрифта для отображения текста

# Определение цветов в формате RGB
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

class SnakeST:  # Создание класса для отдельного сегмента змеи
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:  # Создание класса для змеи
    def __init__(self):
        self.body = [
            SnakeST(
                x = SW // BLOCK_SIZE // 2,
                y = SH // BLOCK_SIZE // 2,
            ),
        ]

    def draw(self):  # Метод для отрисовки змеи на экране
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

    def move(self, dx, dy):  # Метод для движения змеи
        for idx in range(len(self.body) - 1, 0, -1):
            self.body[idx].x = self.body[idx - 1].x
            self.body[idx].y = self.body[idx - 1].y

        self.body[0].x += dx
        self.body[0].y += dy

        for idx in range(len(self.body) - 1, 0, -1):
            if self.body[idx].x == self.body[0].x and self.body[idx].y == self.body[0].y:
                game_over()

        if self.body[0].x > SW // BLOCK_SIZE:
            game_over()
        elif self.body[0].x < 0:
            game_over()
        elif self.body[0].y < 0:
            game_over()
        elif self.body[0].y >= SH // BLOCK_SIZE:
            game_over()

    def check_collision(self, food):  # Метод для проверки столкновения с едой
        if food.location.x != self.body[0].x:
            return False
        if food.location.y != self.body[0].y:
            return False
        return True

class Apple:  # Создание класса для яблока
    def __init__(self, x, y):
        self.location = SnakeST(x, y)

    def draw(self):  # Метод для отрисовки яблока на экране
        pygame.draw.rect(
            SCREEN,
            RED,
            pygame.Rect(
                self.location.x * BLOCK_SIZE,
                self.location.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )

    def generate_new(self, snake_body):  # Метод для генерации нового яблока
        self.location.x = random.randint(0, SW // BLOCK_SIZE - 1)
        self.location.y = random.randint(0, SH // BLOCK_SIZE - 1)
        for idx in range(len(snake_body) - 1, 0, -1):
            if self.location.x == snake_body[idx].x and self.location.y == snake_body[idx].y:
                self.location.x = random.randint(0, SW // BLOCK_SIZE - 1)
                self.location.y = random.randint(0, SH // BLOCK_SIZE - 1)
                idx = len(snake_body) - 1

def draw_grid():  # Функция для отрисовки сетки на экране
    for x in range(0, SW, BLOCK_SIZE):
        pygame.draw.line(SCREEN, WHITE, start_pos=(x, 0), end_pos=(x, SH), width=1)
    for y in range(0, SH, BLOCK_SIZE):
        pygame.draw.line(SCREEN, WHITE, start_pos=(0, y), end_pos=(SW, y), width=1)

    pygame.draw.line(SCREEN, WHITE, start_pos=(0, SH - 1), end_pos=(SW - 1, SH - 1), width=1)  # bottom border
    pygame.draw.line(SCREEN, WHITE, start_pos=(0, 0), end_pos=(0, SH), width=1)  # left border
    pygame.draw.line(SCREEN, WHITE, start_pos=(SW - 1, 0), end_pos=(SW - 1, SH - 1), width=1)  # right border
    pygame.draw.line(SCREEN, WHITE, start_pos=(0, 0), end_pos=(SW, 0), width=1)  # top border

def game_over():  # Функция для завершения игры
    sys.exit()

conn = sqlite3.connect('snake_game.db')  # Инициализация подключения к базе данных SQLite
c = conn.cursor()  # Создание объекта курсора для работы с базой данных

# Создание таблицы пользователей и таблицы счетов пользователей, если они не существуют
c.execute('''CREATE TABLE IF NOT EXISTS User (
             id INTEGER PRIMARY KEY,
             username TEXT UNIQUE)''')

c.execute('''CREATE TABLE IF NOT EXISTS User_Score (
             user_id INTEGER,
             level INTEGER,
             score INTEGER,
             FOREIGN KEY(user_id) REFERENCES User(id))''')

conn.commit()  # Сохранение изменений в базе данных

def get_user_level(user_id):  # Функция для получения текущего уровня пользователя
    c.execute("SELECT level FROM User_Score WHERE user_id=?", (user_id,))
    level = c.fetchone()
    return level[0] if level else None

def create_user(username):  # Функция для создания нового пользователя
    c.execute("INSERT INTO User (username) VALUES (?)", (username,))
    conn.commit()
    return c.lastrowid

def get_user_id(username):  # Функция для получения ID пользователя
    c.execute("SELECT id FROM User WHERE username=?", (username,))
    user = c.fetchone()
    return user[0] if user else None

def save_score(user_id, level, score):  # Функция для сохранения счета пользователя
    c.execute("INSERT INTO User_Score (user_id, level, score) VALUES (?, ?, ?)", (user_id, level, score))
    conn.commit()

def check_existing_user(username):  # Функция для проверки существующего пользователя
    user_id = get_user_id(username)
    if user_id:
        level = get_user_level(user_id)
        print(f"Добро пожаловать, {username}! Ваш текущий уровень: {level}.")
        return user_id
    else:
        print(f"Добро пожаловать, {username}!")
        return create_user(username)

def main():  # Основная функция игры
    username = input("Введите ваше имя пользователя: ")  # Запрос имени пользователя
    user_id = check_existing_user(username)  # Проверка существующего пользователя и получение его ID

    snake = Snake()  # Создание змеи
    apple = Apple(5, 5)  # Создание яблока
    dx = 0
    dy = 0
    movin = ''
    score = 0
    LVL = 0

    while True:
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
                elif event.key == pygame.K_p:  # Пауза и сохранение
                    save_score(user_id, LVL, score)
                    print("Игра приостановлена. Счет сохранен.")
                    sys.exit()

        snake.move(dx, dy)

        if snake.check_collision(apple):
            score += 1
            LVL = score // 5

            apple.generate_new(snake.body)
            snake.body.append(
                SnakeST(snake.body[-1].x, snake.body[-1].y)
            )

        if len(snake.body) == 1: movin = ''

        score_show = FONT.render('Счет: ' + str(score), True, WHITE)
        level_show = FONT.render('УРОВЕНЬ: ' + str(LVL), True, WHITE)

        SCREEN.fill(BLACK)
        SCREEN.blit(score_show, (280, SH))
        SCREEN.blit(level_show, (70, SH))

        snake.draw()
        apple.draw()
        draw_grid()

        pygame.display.update()
        CLOCK.tick(4 + LVL*1.5)

if __name__ == "__main__":
    main()
