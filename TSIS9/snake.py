import random
import pygame
import sys
import time

pygame.init()
pygame.font.init()

pygame.display.set_caption("Snake Game")
SW, SH = 520, 520
BLOCK_SIZE = 40
SCREEN = pygame.display.set_mode((SW, SH + 40))

CLOCK = pygame.time.Clock()
FONT = pygame.font.Font("font.ttf", BLOCK_SIZE)

RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

class SnakeST:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Snake():
    def __init__(self):
        self.body = [
            SnakeST(
                x = SW // BLOCK_SIZE // 2,
                y = SH // BLOCK_SIZE // 2,
            ),
        ]

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

    def move(self, dx, dy):
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

    def check_collision(self, apple):
        if apple.location.x != self.body[0].x:
            return False
        if apple.location.y != self.body[0].y:
            return False
        return True


class Apple:
    def __init__(self, x, y):
        self.color = RED
        self.weight = 1
        self.location = SnakeST(x, y)

    def draw(self):
        pygame.draw.rect(
            SCREEN,
            self.color,
            pygame.Rect(
                self.location.x * BLOCK_SIZE,
                self.location.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )

    def generate_new(self, snake_body):
        self.location.x = random.randint(0, SW // BLOCK_SIZE - 1)
        self.location.y = random.randint(0, SH // BLOCK_SIZE - 1)
        self.weight = random.randint(1, 3)
        self.color = 200 - (self.weight - 1) * 100
        self.color = 200 - (self.weight - 1) * 100
        for idx in range(len(snake_body) - 1, 0, -1):
            if self.location.x == snake_body[idx].x and self.location.y == snake_body[idx].y:
                self.location.x = random.randint(0, SW // BLOCK_SIZE - 1)
                self.location.y = random.randint(0, SH // BLOCK_SIZE - 1)
                idx = len(snake_body) - 1


def draw_grid():
    for x in range(0, SW, BLOCK_SIZE):
        pygame.draw.line(SCREEN, WHITE, start_pos=(x, 0), end_pos=(x, SH), width=1)
    for y in range(0, SH, BLOCK_SIZE):
        pygame.draw.line(SCREEN, WHITE, start_pos=(0, y), end_pos=(SW, y), width=1)

    pygame.draw.line(SCREEN, WHITE, start_pos=(0, SH - 1), end_pos=(SW - 1, SH - 1), width=1)  # bottom border
    pygame.draw.line(SCREEN, WHITE, start_pos=(0, 0), end_pos=(0, SH), width=1)  # left border
    pygame.draw.line(SCREEN, WHITE, start_pos=(SW - 1, 0), end_pos=(SW - 1, SH - 1), width=1)  # right border
    pygame.draw.line(SCREEN, WHITE, start_pos=(0, 0), end_pos=(SW, 0), width=1)  # top border


def game_over():
    sys.exit()


def main():
    snake = Snake()
    apple = Apple(5, 5)
    dx = 0
    dy = 0
    movin = ''
    score = 0
    LVL = 0
    spawn = time.perf_counter()
    dispawn = 0

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
                elif event.key == pygame.K_q:
                    False

        snake.move(dx, dy)

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

        if time.perf_counter() - spawn > 5:
            spawn = time.perf_counter()
            apple.generate_new(snake.body)

        score_show = FONT.render('Score: ' + str(score), True, WHITE)
        level_show = FONT.render('LVL: ' + str(LVL), True, WHITE)

        SCREEN.fill(BLACK)
        SCREEN.blit(score_show, (280, SH))
        SCREEN.blit(level_show, (70, SH))

        snake.draw()
        apple.draw()
        draw_grid()

        pygame.display.update()
        CLOCK.tick(4 + LVL*1.5)

if True == True:
    main()