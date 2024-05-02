import pygame  # Импорт модуля Pygame для создания игры

def main():
    pygame.init()  # Инициализация Pygame
    screen = pygame.display.set_mode((640, 480))  # Создание окна игры размером 640x480 пикселей
    clock = pygame.time.Clock()  # Создание объекта Clock для управления FPS
    
    radius = 15  # Начальный радиус точек
    x = 0  # Начальные координаты x точки
    y = 0  # Начальные координаты y точки
    mode = 'blue'  # Начальный цвет точек
    points = []  # Список для хранения координат точек
    
    while True:
        
        pressed = pygame.key.get_pressed()  # Получение нажатых клавиш
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]  # Проверка, удерживается ли клавиша Alt
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]  # Проверка, удерживается ли клавиша Ctrl
        
        for event in pygame.event.get():  # Обработка событий
            
            # Определение закрытия окна
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:  # Ctrl+W
                    return
                if event.key == pygame.K_F4 and alt_held:  # Alt+F4
                    return
                if event.key == pygame.K_ESCAPE:  # Escape
                    return
                
                # Определение нажатия клавиш для смены цвета
                if event.key == pygame.K_r:  # R - красный
                    mode = 'red'
                elif event.key == pygame.K_g:  # G - зеленый
                    mode = 'green'
                elif event.key == pygame.K_b:  # B - синий
                    mode = 'blue'
            
            # Обработка события нажатия кнопки мыши
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Левая кнопка мыши
                    radius = min(200, radius + 1)  # Увеличение радиуса точек
                elif event.button == 3:  # Правая кнопка мыши
                    radius = max(1, radius - 1)  # Уменьшение радиуса точек
            
            # Обработка движения мыши
            if event.type == pygame.MOUSEMOTION:
                position = event.pos  # Получение координат мыши
                points = points + [position]  # Добавление координат в список точек
                points = points[-256:]  # Ограничение списка до 256 последних точек
                
        screen.fill((0, 0, 0))  # Заполнение экрана черным цветом
        
        # Отрисовка всех точек
        i = 0
        while i < len(points) - 1:
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)  # Отрисовка линии между точками
            i += 1
        
        pygame.display.flip()  # Обновление экрана
        
        clock.tick(60)  # Ограничение FPS

# Функция для отрисовки линии между точками
def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':  # Если выбран синий цвет
        color = (c1, c1, c2)
    elif color_mode == 'red':  # Если выбран красный цвет
        color = (c2, c1, c1)
    elif color_mode == 'green':  # Если выбран зеленый цвет
        color = (c1, c2, c1)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

main()  # Запуск главной функции игры
