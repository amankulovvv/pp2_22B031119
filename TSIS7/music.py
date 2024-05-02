# Импорт библиотеки Pygame
import pygame

# Инициализация Pygame
pygame.init()

# Создание объекта Clock для управления частотой кадров
FPS = pygame.time.Clock()

# Создание окна размером 600x500 пикселей
sc = pygame.display.set_mode((600, 500))

# Установка заголовка окна
pygame.display.set_caption("Song")

# Список песен
Playlist = ['first.mp3', 'second.mp3', 'third.mp3', 'fourth.mp3']

# Список фоновых изображений для каждой песни
background_images = ['back1.jpg', 'back2.jpg', 'back3.jpg', 'back4.jpg']

# Индекс текущей песни
curm = 0

# Загрузка и воспроизведение первой песни
pygame.mixer.music.load(Playlist[curm])
pygame.mixer.music.play()

# Флаг для отслеживания статуса паузы музыки
music_paused = False

# Основной игровой цикл
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        # Если пользователь закрывает окно
        if event.type == pygame.QUIT:
            running = False

        # Если нажата клавиша
        elif event.type == pygame.KEYDOWN:
            # Если нажат Enter
            if event.key == pygame.K_RETURN:
                # Если музыка была на паузе
                if music_paused:
                    # Возобновление воспроизведения музыки
                    pygame.mixer.music.unpause()
                    music_paused = False
                # Если музыка не была на паузе
                else:
                    # Пауза воспроизведения музыки
                    pygame.mixer.music.pause()
                    music_paused = True

            # Если нажата стрелка вправо
            elif event.key == pygame.K_RIGHT:
                # Переход к следующей песне в плейлисте
                curm = (curm + 1) % len(Playlist) #
                # Загрузка следующей песни
                pygame.mixer.music.load(Playlist[curm])
                # Воспроизведение следующей песни
                pygame.mixer.music.play()
                # Отображение соответствующего фонового изображения
                sc.blit(pygame.image.load(background_images[curm]).convert(), (0, 0))
                music_paused = False

            # Если нажата стрелка влево
            elif event.key == pygame.K_LEFT:
                # Переход к предыдущей песне в плейлисте
                curm = (curm - 1) % len(Playlist)
                # Загрузка предыдущей песни
                pygame.mixer.music.load(Playlist[curm])
                # Воспроизведение предыдущей песни
                pygame.mixer.music.play()
                # Отображение соответствующего фонового изображения
                sc.blit(pygame.image.load(background_images[curm]).convert(), (0, 0))
                music_paused = False #sc.blit() - это функция Pygame, которая используется для отображения изображения на экране. В данном случае она используется для отображения фонового изображения на экране sc (игровом окне) в соответствии с текущей песней в плейлисте. Функция принимает два аргумента: изображение, которое нужно отобразить, и координаты верхнего левого угла, где изображение должно быть отображено на экране.





    # Обновление экрана
    pygame.display.update()
    # Ограничение частоты кадров до 60 кадров в секунду
    FPS.tick(60)
