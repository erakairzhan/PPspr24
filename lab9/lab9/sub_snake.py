import pygame, sys, random
from pygame.math import Vector2

cnt = 0
class SNAKE:
    def __init__(self):
        # Инициализация змеи
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]  # Начальное положение змеи
        self.direction = Vector2(0, 0)  # Начальное направление движения
        self.new_block = False  # Флаг для добавления нового блока (фрукта)

        # Загрузка графики для головы змеи и хвоста
        self.head_up = pygame.image.load("/Users/erakairzhan/Desktop/images/snake/head_up.png")
        self.head_down = pygame.image.load("/Users/erakairzhan/Desktop/images/snake/head_down.png")
        self.head_right = pygame.image.load("/Users/erakairzhan/Desktop/images/snake/head_right.png")
        self.head_left = pygame.image.load("/Users/erakairzhan/Desktop/images/snake/head_left.png")
        self.tail_up = pygame.image.load("/Users/erakairzhan/Desktop/images/snake/tail_up.png")
        self.tail_down = pygame.image.load("/Users/erakairzhan/Desktop/images/snake/tail_down.png")
        self.tail_right = pygame.image.load("/Users/erakairzhan/Desktop/images/snake/tail_right.png")
        self.tail_left = pygame.image.load("/Users/erakairzhan/Desktop/images/snake/tail_left.png")

        # Загрузка графики для тела змеи
        self.body_vertical = pygame.image.load("/Users/erakairzhan/Desktop/images/snake/body_vertical.png")
        self.body_horizontal = pygame.image.load("/Users/erakairzhan/Desktop/images/snake/body_horizontal.png")
        self.body_tr = pygame.image.load("/Users/erakairzhan/Desktop/images/snake/body_tr.png")
        self.body_tl = pygame.image.load("/Users/erakairzhan/Desktop/images/snake/body_tl.png")
        self.body_br = pygame.image.load("/Users/erakairzhan/Desktop/images/snake/body_br.png")
        self.body_bl = pygame.image.load("/Users/erakairzhan/Desktop/images/snake/body_bl.png")

        # Звук при поедании фрукта
        self.crunch_sound = pygame.mixer.Sound("/Users/erakairzhan/Desktop/images/snake/sounds/crunch.wav")

    def draw_snake(self):
        # Отрисовка змеи
        self.update_head_graphics()
        self.update_tail_graphics()

        for index, block in enumerate(self.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)

            if index == 0:
                screen.blit(self.head, block_rect)  # Отрисовка головы змеи
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)  # Отрисовка хвоста змеи
            else:
                # Отрисовка тела змеи
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br, block_rect)

    def update_head_graphics(self):
        # Обновление графики головы змеи в зависимости от направления
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0):
            self.head = self.head_left
        elif head_relation == Vector2(-1, 0):
            self.head = self.head_right
        elif head_relation == Vector2(0, 1):
            self.head = self.head_up
        elif head_relation == Vector2(0, -1):
            self.head = self.head_down

    def update_tail_graphics(self):
        # Обновление графики хвоста змеи в зависимости от направления
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0):
            self.tail = self.tail_left
        elif tail_relation == Vector2(-1, 0):
            self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1):
            self.tail = self.tail_up
        elif tail_relation == Vector2(0, -1):
            self.tail = self.tail_down

    def move_snake(self):
        global cnt
        if self.new_block == True:
            if(cnt == 5):  # Счетчик для анимации поедания фрукта
                cnt = 0
                body_copy = self.body[:]
                body_copy.insert(0, body_copy[0] + self.direction)
                self.body = body_copy[:]
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        # Добавление нового блока (фрукта)
        self.new_block = True

    def play_crunch_sound(self):
        # Воспроизведение звука при поедании фрукта
        self.crunch_sound.play()

    def reset(self):
        # Сброс змеи
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)

class FRUIT:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        global cnt
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)

        if(cnt == 0):  # Анимация поедания фрукта
            screen.blit(apple_second, fruit_rect)
        else:
            screen.blit(apple, fruit_rect)

    def randomize(self):
        global cnt
        cnt += 1
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self):
        # Обновление игровых элементов
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        # Отрисовка игровых элементов
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def check_collision(self):
        # Проверка столкновений
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
            self.snake.play_crunch_sound()

        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()

    def check_fail(self):
        # Проверка поражения
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        # Обработка поражения
        self.snake.reset()

    def draw_grass(self):
        # Отрисовка травы на поле
        grass_color = (167, 209, 61)
        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)

    def draw_score(self):
        # Отрисовка счета игрока
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text, True, (56, 74, 12))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        apple_rect = apple.get_rect(midright=(score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left, apple_rect.top, apple_rect.width + score_rect.width + 6,
                              apple_rect.height)

        pygame.draw.rect(screen, (167, 209, 61), bg_rect)
        screen.blit(score_surface, score_rect)
        screen.blit(apple, apple_rect)
        pygame.draw.rect(screen, (56, 74, 12), bg_rect, 2)


pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()
apple = pygame.image.load("/Users/erakairzhan/Desktop/images/snake/apple.png")
apple_second = pygame.image.load("/Users/erakairzhan/Desktop/images/snake/apple_second.png")
game_font = pygame.font.Font("/Users/erakairzhan/Desktop/images/snake/font/PoetsenOne-Regular.ttf", 25)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = MAIN()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_d:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_s:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_a:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)

    screen.fill((175, 215, 70))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)
