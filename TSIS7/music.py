import pygame

pygame.init()
FPS = pygame.time.Clock()

sc = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Song")

# Загрузка фонового изображения
background = pygame.image.load("back.jpg").convert()
background = pygame.transform.scale(background, (600, 500))

Playlist = ['first.mp3', 'second.mp3', 'third.mp3', 'fourth.mp3']
curm = 0
pygame.mixer.music.load(Playlist[curm])
pygame.mixer.music.play()
music_paused = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  
                if music_paused:
                    pygame.mixer.music.unpause() 
                    music_paused = False
                else:
                    pygame.mixer.music.pause() 
                    music_paused = True
            elif event.key == pygame.K_RIGHT:  
                curm = (curm + 1) % len(Playlist) 
                pygame.mixer.music.load(Playlist[curm]) 
                pygame.mixer.music.play()  
                music_paused = False  
            elif event.key == pygame.K_LEFT:  
                curm = (curm - 1) % len(Playlist)  
                pygame.mixer.music.load(Playlist[curm])  
                pygame.mixer.music.play()  
                music_paused = False  

   
    sc.blit(background, (0, 0))
    pygame.display.update()
    FPS.tick(60)

pygame.quit()
