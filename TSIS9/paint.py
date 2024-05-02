import pygame  # Импорт модуля pygame для создания игрового интерфейса
import math  # Импорт модуля math для математических операций

# Инициализация Pygame и создание экрана
pygame.init()  # Инициализация Pygame
clock = pygame.time.Clock()  # Создание объекта Clock для управления временем
WIDTH, HEIGHT = 800, 700  # Установка размеров экрана
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))  # Создание окна заданных размеров

# Определение цветов
BLACK = pygame.Color(0, 0, 0)  # Чёрный цвет
WHITE = pygame.Color(255, 255, 255)  # Белый цвет
GRAY = pygame.Color(127, 127, 127)  # Серый цвет

# Определение базового класса для объектов игры
class GameObject:
    def draw(self):  # Абстрактный метод для отрисовки объекта
        raise NotImplementedError

    def handle(self):  # Абстрактный метод для обработки событий
        raise NotImplementedError

# Определение класса для кнопки
class Button(pygame.sprite.Sprite):
    def __init__(self, points, width=0, color=GRAY):  # Инициализация кнопки
        super().__init__()  # Вызов конструктора родительского класса
        self.points = points  # Координаты вершин кнопки
        self.width = width  # Ширина линии кнопки
        self.color = color  # Цвет кнопки
        # Создание прямоугольника для кнопки с помощью метода pygame.draw.polygon
        self.rect = pygame.draw.polygon(SCREEN, self.color, self.points, self.width)

    def draw(self):  # Метод для отрисовки кнопки
        pygame.draw.polygon(SCREEN, self.color, self.points, self.width)

# Определение класса для ручки
class Pen(GameObject):
    def __init__(self, start_pos, thickness=5, color=WHITE):  # Инициализация ручки
        self.thickness = thickness  # Толщина линии ручки
        self.color = color  # Цвет ручки
        self.points = []  # Список точек для рисования

    def draw(self):  # Метод для отрисовки ручки
        for idx, point in enumerate(self.points[:-1]):
            pygame.draw.line(
                SCREEN,
                self.color,
                start_pos=point,
                end_pos=self.points[idx + 1],
                width=self.thickness,
            )

    def handle(self, mouse_pos):  # Метод для обработки событий ручки
        self.points.append(mouse_pos)  # Добавление текущей позиции мыши в список точек

# Определение класса для прямоугольника
class Rectangle(GameObject):
    def __init__(self, start_pos, thickness=5, color=WHITE):  # Инициализация прямоугольника
        self.thickness = thickness  # Толщина линии прямоугольника
        self.color = color  # Цвет прямоугольника
        self.start_pos = start_pos  # Начальная позиция прямоугольника
        self.end_pos = start_pos  # Конечная позиция прямоугольника

    def draw(self):  # Метод для отрисовки прямоугольника
        # Вычисление координат вершин прямоугольника
        x1 = min(self.start_pos[0], self.end_pos[0])
        y1 = min(self.start_pos[1], self.end_pos[1])
        x2 = max(self.start_pos[0], self.end_pos[0])
        y2 = max(self.start_pos[1], self.end_pos[1])
        # Отрисовка прямоугольника с использованием метода pygame.draw.rect
        pygame.draw.rect(SCREEN, self.color, (x1, y1, x2 - x1, y2 - y1), width=self.thickness)

    def handle(self, mouse_pos):  # Метод для обработки событий прямоугольника
        self.end_pos = mouse_pos  # Обновление конечной позиции прямоугольника

# Определение класса для прямоугольного треугольника
class RightTriangle(GameObject):
    def __init__(self, start_pos, thickness=5, color=WHITE):  # Инициализация треугольника
        self.thickness = thickness  # Толщина линии треугольника
        self.color = color  # Цвет треугольника
        self.start_pos = start_pos  # Начальная позиция треугольника
        self.end_pos = start_pos  # Конечная позиция треугольника

    def draw(self):  # Метод для отрисовки треугольника
        x1, y1 = self.start_pos
        x2, y2 = self.end_pos
        # Вычисление координат вершин треугольника
        side_len = x2 - x1  
        h = math.pow(side_len ** 2 * 0.75, 0.5)  
        if side_len < 0: h *= -1  
        vertex_1 = (x1, y1)
        vertex_2 = (x2, y1)
        vertex_3 = (x1 + side_len / 2, y1 - h)
        vertices = [vertex_1, vertex_2, vertex_3]
        # Отрисовка треугольника с помощью метода pygame.draw.polygon
        pygame.draw.polygon(SCREEN, self.color, vertices, width=self.thickness)

    def handle(self, mouse_pos):  # Метод для обработки событий треугольника
        self.end_pos = mouse_pos  # Обновление конечной позиции треугольника

# Определение класса для равностороннего треугольника
class EquilateralTriangle(GameObject):
    def __init__(self, start_pos, thickness=5, color=WHITE):  # Инициализация треугольника
        self.thickness = thickness  # Толщина линии треугольника
        self.color = color  # Цвет треугольника
        self.start_pos = start_pos  # Начальная позиция треугольника
        self.end_pos = start_pos  # Конечная позиция треугольника

    def draw(self):  # Метод для отрисовки треугольника
        x1, y1 = self.start_pos
        x2, y2 = self.end_pos
        w = (x2 - x1) * 2
        vertex_1 = (x1, y1)
        vertex_2 = (x2, y2)
        vertex_3 = (x2 - w, y2)
        vertices = [vertex_1, vertex_2, vertex_3]
        # Отрисовка треугольника с помощью метода pygame.draw.polygon
        pygame.draw.polygon(SCREEN, self.color, vertices, width=self.thickness)

    def handle(self, mouse_pos):  # Метод для обработки событий треугольника
        self.end_pos = mouse_pos  # Обновление конечной позиции треугольника

# Определение класса для ромба
class Rhombus(GameObject):
    def __init__(self, start_pos, thickness=5, color=WHITE):  # Инициализация ромба
        self.thickness = thickness  # Толщина линии ромба
        self.color = color  # Цвет ромба
        self.start_pos = start_pos  # Начальная позиция ромба
        self.end_pos = start_pos  # Конечная позиция ромба

    def draw(self):  # Метод для отрисовки ромба
        x1, y1 = self.start_pos
        x2, y2 = self.end_pos
        side_len = math.pow((x2 - x1) ** 2 + (y2 - y1) ** 2, 0.5)
        vertex_1 = (x1, y1)
        vertex_2 = (x2, y2)
        vertex_3 = (x2 + side_len, y2)
        vertex_4 = (x1 + side_len, y1)
        vertices = [vertex_1, vertex_2, vertex_3, vertex_4]
        # Отрисовка ромба с помощью метода pygame.draw.polygon
        pygame.draw.polygon(SCREEN, self.color, vertices, width=self.thickness)

    def handle(self, mouse_pos):  # Метод для обработки событий ромба
        self.end_pos = mouse_pos  # Обновление конечной позиции ромба

# Определение класса для эллипса
class Ellipse(GameObject):
    def __init__(self, start_pos, thickness=5, color=WHITE):  # Инициализация эллипса
        self.thickness = thickness  # Толщина линии эллипса
        self.color = color  # Цвет эллипса
        self.start_pos = start_pos  # Начальная позиция эллипса
        self.end_pos = start_pos  # Конечная позиция эллипса

    def draw(self):  # Метод для отрисовки эллипса
        x1, y1 = self.start_pos
        x2, y2 = self.end_pos
        # Вычисление координат и размеров прямоугольника, описывающего эллипс
        x = min(x1, x2)
        y = min(y1, y2)
        width = abs(x2 - x1)
        height = abs(y2 - y1)
        # Отрисовка эллипса с помощью метода pygame.draw.ellipse
        pygame.draw.ellipse(SCREEN, self.color, (x, y, width, height), self.thickness)

    def handle(self, mouse_pos):  # Метод для обработки событий эллипса
        self.end_pos = mouse_pos  # Обновление конечной позиции эллипса

# Определение класса для ластика
class Eraser(GameObject):
    def __init__(self, start_pos, thickness=20, color=BLACK):  # Инициализация ластика
        self.thickness = thickness  # Толщина линии ластика
        self.color = color  # Цвет ластика (чёрный)
        self.start_pos = start_pos  # Начальная позиция ластика
        self.end_pos = start_pos  # Конечная позиция ластика

    def draw(self):  # Метод для отрисовки прямоугольника, удаляющего пиксели нарисованных объектов
        x1, y1 = self.start_pos
        x2, y2 = self.end_pos
        # Вычисление координат и размеров прямоугольника
        x = min(x1, x2)
        y = min(y1, y2)
        width = abs(x2 - x1)
        height = abs(y2 - y1)
        # Заливка прямоугольника фоновым цветом (чёрным)
        pygame.draw.rect(SCREEN, self.color, (x, y, width, height), self.thickness)

    def handle(self, mouse_pos):  # Метод для обработки событий ластика
        self.end_pos = mouse_pos  # Обновление конечной позиции ластика

# Главная функция программы
def main():
    # Определение координат вершин для каждой кнопки
    Points_P = [(28, 10), (12, 50)]
    Points_S = [(50, 10), (90, 10), (90, 50), (50, 50)]
    Points_RT = [(135, 10), (170, 50), (100, 50)]
    Points_EqT = [(195, 10), (210, 50), (180, 50)]
    Points_rh = [(240, 10), (260, 30), (240, 50), (220, 30)]
    Points_El = [(290, 10), (340, 10), (340, 50), (290, 50)]
    Points_Er = [(360, 10), (400, 10), (400, 50), (360, 50)]

    # Создание объектов кнопок
    switch_pen = Button(Points_P, 5)  # Создание кнопки для переключения на ручку
    switch_square = Button(Points_S)  # Создание кнопки для переключения на прямоугольник
    switch_triangleR = Button(Points_RT)  # Создание кнопки для переключения на прямоугольный треугольник
    switch_triangleW = Button(Points_EqT)  # Создание кнопки для переключения на равносторонний треугольник
    switch_rhombus = Button(Points_rh)  # Создание кнопки для переключения на ромб
    switch_ellipse = Button(Points_El)  # Создание кнопки для переключения на эллипс
    switch_eraser = Button(Points_Er)  # Создание кнопки для переключения на ластик
    buttons = [switch_pen, switch_square, switch_triangleR, switch_triangleW, switch_rhombus, switch_ellipse, switch_eraser]

    # Начальная форма - ручка
    current_shape = 'pen'  # Установка начальной формы - ручка
    objects = []  # Список для хранения созданных объектов
    active_obj = None  # Активный объект (объект, который сейчас создаётся)
    running = True  # Флаг для работы игрового цикла

    # Главный игровой цикл
    while running:
        SCREEN.fill(BLACK)  # Заполнение экрана чёрным цветом
        for event in pygame.event.get():  # Перебор всех событий в очереди событий
            if event.type == pygame.QUIT:  # Если событие - выход
                running = False  # Остановить цикл

            # Обработка нажатий кнопок
            if event.type == pygame.MOUSEBUTTONDOWN:
                buttons_dict = {
                    switch_pen: 'pen',
                    switch_square: 'square',
                    switch_triangleR: 'rightT',
                    switch_triangleW: 'wrongT',
                    switch_rhombus: 'rhombus',
                    switch_ellipse: 'ellipse',
                    switch_eraser: 'eraser',
                }
                for key in buttons_dict.keys():
                    if key.rect.collidepoint(pygame.mouse.get_pos()):
                        current_shape = buttons_dict[key]
                else:
                    # Создание активного объекта в соответствии с выбранной формой
                    shapes = {
                        'pen': Pen(start_pos=event.pos),
                        'square': Rectangle(start_pos=event.pos),
                        'rightT': RightTriangle(start_pos=event.pos),
                        'wrongT': EquilateralTriangle(start_pos=event.pos),
                        'rhombus': Rhombus(start_pos=event.pos),
                        'ellipse': Ellipse(start_pos=event.pos),
                        'eraser': Eraser(start_pos=event.pos),
                    }
                    active_obj = shapes[current_shape]

            # Обработка движения мыши и отрисовки активного объекта
            if event.type == pygame.MOUSEMOTION and active_obj is not None:
                active_obj.handle(mouse_pos=pygame.mouse.get_pos())
                active_obj.draw()

            # Обработка отпускания кнопки мыши и добавление активного объекта в список объектов
            if event.type == pygame.MOUSEBUTTONUP and active_obj is not None:
                objects.append(active_obj)
                active_obj = None

        # Отрисовка кнопок
        for button in buttons:
            button.draw()

        # Отрисовка всех объектов
        for obj in objects:
            obj.draw()

        clock.tick(30)  # Управление частотой обновления экрана
        pygame.display.flip()  # Отображение нарисованного на экране

# Запуск главной функции, если файл используется напрямую
if __name__ == '__main__':
    main()
