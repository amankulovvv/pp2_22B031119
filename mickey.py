import pygame
import sys
import math
from datetime import datetime

pygame.init()

WIDTH, HEIGHT = 400, 400
CENTER = (WIDTH // 2, HEIGHT // 2)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Analog Clock")

minute_hand_image = pygame.image.load("rhand.png")
minute_hand_image = pygame.transform.scale(minute_hand_image, (500, 500))

second_hand_image = pygame.image.load("lhand.png")
second_hand_image = pygame.transform.scale(second_hand_image, (500, 500))

background_image = pygame.image.load("sc.png")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))


def draw_hand(image, angle, length):
    if image is not None:
        rotated_image = pygame.transform.rotate(image, -angle)
        rect = rotated_image.get_rect(center=CENTER)
        screen.blit(rotated_image, rect)
    else:
        end_x = CENTER[0] + length * math.cos(math.radians(angle - 90))
        end_y = CENTER[1] + length * math.sin(math.radians(angle - 90))
        pygame.draw.line(screen, (0, 0, 0), CENTER, (end_x, end_y), 4)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background_image, (0, 0))

    current_time = datetime.now()
    hour = current_time.hour % 12
    minute = current_time.minute + 8
    second = current_time.second - 8

    draw_hand(None, (hour * 30) + (0.5 * minute), 80)
    draw_hand(minute_hand_image, minute * 6, 120)
    draw_hand(second_hand_image, second * 6, 140)

    pygame.display.flip()
    pygame.time.Clock().tick(60)