# import random  # Импорт модуля random для генерации случайных чисел
# import pygame  # Импорт библиотеки Pygame для создания игр
# import sys  # Импорт модуля sys для работы с системными функциями

# pygame.init()  # Инициализация Pygame
# pygame.font.init()  # Инициализация модуля Pygame для работы с шрифтами

# pygame.display.set_caption("Snake Game")  # Установка заголовка окна игры
# SW, SH = 520, 520  # Ширина и высота окна игры
# BLOCK_SIZE = 40  # Размер блока
# SCREEN = pygame.display.set_mode((SW, SH + 40))  # Создание окна игры с учетом высоты строки состояния

# CLOCK = pygame.time.Clock()  # Создание объекта Clock для управления FPS
# FONT = pygame.font.Font("TSIS9/font.ttf", BLOCK_SIZE)  # Загрузка шрифта для отображения текста на экране

# RED = (255, 0, 0)  # Красный цвет
# BLACK = (0, 0, 0)  # Черный цвет
# BLUE = (0, 0, 255)  # Синий цвет
# GREEN = (0, 255, 0)  # Зеленый цвет
# WHITE = (255, 255, 255)  # Белый цвет

# class SnakeST:  # Класс для создания элемента змеи
#     def __init__(self, x, y):
#         self.x = x  # Координата x
#         self.y = y  # Координата y

# class Snake():  # Класс для создания змеи
#     def __init__(self):
#         self.body = [
#             SnakeST(
#                 x = SW // BLOCK_SIZE // 2,  # Начальная координата x головы змеи
#                 y = SH // BLOCK_SIZE // 2,  # Начальная координата y головы змеи
#             ),
#         ]

#     def draw(self):  # Метод для отрисовки змеи на экране
#         head = self.body[0]  # Голова змеи

#         pygame.draw.rect(  # Отрисовка головы змеи
#             SCREEN,
#             GREEN,
#             pygame.Rect(
#                 head.x * BLOCK_SIZE,
#                 head.y * BLOCK_SIZE,
#                 BLOCK_SIZE,
#                 BLOCK_SIZE,
#             )
#         )

#         for body in self.body[1:]:  # Отрисовка остальной части змеи
#             pygame.draw.rect(
#                 SCREEN,
#                 GREEN,
#                 pygame.Rect(
#                     body.x * BLOCK_SIZE,
#                     body.y * BLOCK_SIZE,
#                     BLOCK_SIZE,
#                     BLOCK_SIZE,
#                 )
#             )

#     def move(self, dx, dy):  # Метод для перемещения змеи
#         for idx in range(len(self.body) - 1, 0, -1):  # Перебор частей тела змеи с конца
#             self.body[idx].x = self.body[idx - 1].x  # Каждая часть змеи занимает позицию предыдущей
#             self.body[idx].y = self.body[idx - 1].y

#         self.body[0].x += dx  # Изменение координаты x головы змеи
#         self.body[0].y += dy  # Изменение координаты y головы змеи

#         for idx in range(len(self.body) - 1, 0, -1):  # Перебор частей тела змеи с конца
#             if self.body[idx].x == self.body[0].x and self.body[idx].y == self.body[0].y:  # Если голова змеи столкнулась с телом
#                 game_over()  # Завершение игры

#         if self.body[0].x > SW // BLOCK_SIZE:  # Если голова змеи вышла за пределы правой границы
#             game_over()  # Завершение игры
#         elif self.body[0].x < 0:  # Если голова змеи вышла за пределы левой границы
#             game_over()  # Завершение игры
#         elif self.body[0].y < 0:  # Если голова змеи вышла за пределы верхней границы
#             game_over()  # Завершение игры
#         elif self.body[0].y >= SH // BLOCK_SIZE:  # Если голова змеи вышла за пределы нижней границы
#             game_over()  # Завершение игры

#     def check_collision(self, food):  # Метод для проверки столкновения змеи с яблоком
#         if food.location.x != self.body[0].x:  # Если координата x яблока не равна координате x головы змеи
#             return False  # Столкновения нет
#         if food.location.y != self.body[0].y:  # Если координата y яблока не равна координате y головы змеи
#             return False  # Столкновения нет
#         return True  # Иначе - столкновение произошло


# class Apple:  # Класс для создания яблока
#     def __init__(self, x, y):
#         self.location = SnakeST(x, y)  # Координаты яблока

#     def draw(self):  # Метод для отрисовки яблока на экране
#         pygame.draw.rect(
#             SCREEN,
#             RED,
#             pygame.Rect(
#                 self.location.x * BLOCK_SIZE,
#                 self.location.y * BLOCK_SIZE,
#                 BLOCK_SIZE,
#                 BLOCK_SIZE,
#             )
#         )

#     def generate_new(self, snake_body):  # Метод для генерации нового яблока
#         self.location.x = random.randint(0, SW // BLOCK_SIZE - 1)  # Случайная координата x
#         self.location.y = random.randint(0, SH // BLOCK_SIZE - 1)  # Случайная координата y
#         for idx in range(len(snake_body) - 1, 0, -1):  # Перебор частей тела змеи с конца
#             if self.location.x == snake_body[idx].x and self.location.y == snake_body[idx].y:  # Если яблоко появилось на теле змеи
#                 self.location.x = random.randint(0, SW // BLOCK_SIZE - 1)  # Генерация новой координаты x
#                 self.location.y = random.randint(0, SH // BLOCK_SIZE - 1)  # Генерация новой координаты y
#                 idx = len(snake_body) - 1  # Сброс индекса

# def draw_grid():  # Функция для отрисовки сетки на экране
#     for x in range(0, SW, BLOCK_SIZE):  # Перебор горизонтальных линий
#         pygame.draw.line(SCREEN, WHITE, start_pos=(x, 0), end_pos=(x, SH), width=1)  # Отрисовка линии
#     for y in range(0, SH, BLOCK_SIZE):  # Перебор вертикальных линий
#         pygame.draw.line(SCREEN, WHITE, start_pos=(0, y), end_pos=(SW, y), width=1)  # Отрисовка линии

#     pygame.draw.line(SCREEN, WHITE, start_pos=(0, SH - 1), end_pos=(SW - 1, SH - 1), width=1)  # Нижняя граница
#     pygame.draw.line(SCREEN, WHITE, start_pos=(0, 0), end_pos=(0, SH), width=1)  # Левая граница
#     pygame.draw.line(SCREEN, WHITE, start_pos=(SW - 1, 0), end_pos=(SW - 1, SH - 1), width=1)  # Правая граница
#     pygame.draw.line(SCREEN, WHITE, start_pos=(0, 0), end_pos=(SW, 0), width=1)  # Верхняя граница


# def game_over():  # Функция для завершения игры
#     sys.exit()  # Выход из программы


# def main():  # Главная функция игры
#     snake = Snake()  # Создание змеи
#     apple = Apple(5, 5)  # Создание яблока
#     dx = 0  # Изменение координаты x
#     dy = 0  # Изменение координаты y
#     movin = ''  # Направление движения змеи
#     score = 0  # Очки игрока
#     LVL = 0  # Уровень игры

#     while True:  # Основной цикл игры

#         for event in pygame.event.get():  # Обработка событий
#             if event.type == pygame.QUIT:  # Если произошло событие закрытия окна
#                 pygame.quit()  # Выход из Pygame
#                 sys.exit()  # Выход из программы

#             if event.type == pygame.KEYDOWN:  # Если была нажата клавиша
#                 if event.key == pygame.K_UP and movin != 'down':  # Если нажата клавиша Вверх и змея не двигается вниз
#                     movin = 'up'  # Задать направление движения вверх
#                     dx, dy = 0, -1  # Установить изменение координаты y на -1
#                 elif event.key == pygame.K_DOWN and movin != 'up':  # Если нажата клавиша Вниз и змея не двигается вверх
#                     movin = 'down'  # Задать направление движения вниз
#                     dx, dy = 0, 1  # Установить изменение координаты y на 1
#                 elif event.key == pygame.K_RIGHT and movin != 'left':  # Если нажата клавиша Вправо и змея не двигается влево
#                     movin = 'right'  # Задать направление движения вправо
#                     dx, dy = +1, 0  # Установить изменение координаты x на 1
#                 elif event.key == pygame.K_LEFT and movin != 'right':  # Если нажата клавиша Влево и змея не двигается вправо
#                     movin = 'left'  # Задать направление движения влево
#                     dx, dy = -1, 0  # Установить изменение координаты x на -1
#                 elif event.key == pygame.K_q:  # Если нажата клавиша Q
#                     False  # Выход из игры

#         snake.move(dx, dy)  # Движение змеи

#         if snake.check_collision(apple):  # Если змея столкнулась с яблоком
#             score += 1  # Увеличение счета
#             LVL = score // 5  # Проверка уровня игры

#             apple.generate_new(snake.body)  # Генерация нового яблока
#             snake.body.append(  # Добавление новой части тела змеи
#                 SnakeST(snake.body[-1].x, snake.body[-1].y)
#             )

#         if len(snake.body) == 1: movin = ''  # Если длина тела змеи равна 1, сброс направления движения

#         score_show = FONT.render('Score: ' + str(score), True, WHITE)  # Отображение счета на экране
#         level_show = FONT.render('LVL: ' + str(LVL), True, WHITE)  # Отображение уровня на экране

#         SCREEN.fill(BLACK)  # Заполнение экрана черным цветом
#         SCREEN.blit(score_show, (280, SH))  # Отображение счета на экране
#         SCREEN.blit(level_show, (70, SH))  # Отображение уровня на экране

#         snake.draw()  # Отрисовка змеи на экране
#         apple.draw()  # Отрисовка яблока на экране
#         draw_grid()  # Отрисовка сетки на экране

#         pygame.display.update()  # Обновление экрана
#         CLOCK.tick(4 + LVL * 1.5)  # Управление FPS в зависимости от уровня игры

# if True == True:  # Запуск игры
#     main()  # Вызов главной функции игры

# "Commenting my code, A.M." с более подробным описанием
