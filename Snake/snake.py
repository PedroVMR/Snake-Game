import pygame as pg
from random import randrange
from sys import exit

# Constantes
WINDOW = 500
TILE_SIZE = 25
RANGE =  (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)

# Variavéis 
get_random_position = lambda: [randrange(*RANGE), randrange(*RANGE)]
snake = pg.rect.Rect([0,0, TILE_SIZE - 2, TILE_SIZE -2])
snake.center = get_random_position(),
length = 1
segments = [snake.copy()]
snake_dir = (0, 0)
time, time_step = 0, 110
food = snake.copy()
food.center = get_random_position()
screen = pg.display.set_mode([WINDOW]*2)
clock = pg.time.Clock()
dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}

# Score
score = 0
pg.font.init()

score_font = pg.font.Font('Bit5x5.ttf', 30)
score_surface = score_font.render('Score: 0', True, (255, 255, 255))
score_rect = score_surface.get_rect()

score_rect.x = 10
score_rect.y = 10

# Música Aleatoria
pg.init()
pg.mixer.music.load('Pearl Jam - Even Flow.mp3')
pg.mixer.music.play()

# Loop Principal
while True:
    screen.fill('black')    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        # Movimentação da Cobra
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                snake_dir = (0, -TILE_SIZE)
                dirs = {pg.K_w: 1, pg.K_s: 0, pg.K_a: 1, pg.K_d: 1}
            if event.key == pg.K_s:
                snake_dir = (0, TILE_SIZE)
                dirs = {pg.K_w: 0, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}
            if event.key == pg.K_a:
                snake_dir = (-TILE_SIZE, 0)
                dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 0}
            if event.key == pg.K_d:
                snake_dir = (TILE_SIZE, 0)
                dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 0, pg.K_d: 1}

    
    # Checar bordas e colisões
    self_eating = pg.Rect.collidelist(snake, segments[:-1]) != -1
    if snake.left < 0 or snake.right > WINDOW or snake.top < 0 or snake.bottom > WINDOW or self_eating:
        snake.center, food.center = get_random_position(), get_random_position()
        length, snake_dir, score = 1, (0, 0), 0
        segments = [snake.copy()]
        score_surface = score_font.render(f'Score: {score}', True, (255, 255, 255))
        
    # Checar a posição da comida
    if snake.colliderect(food):
        food.center = get_random_position()
        length += 1
        score += 1
        score_surface = score_font.render(f'Score: {score}', True, (255, 255, 255))
        
    # desenhe o score_surface na tela
    screen.blit(score_surface, score_rect)
            
    # Desenha a comida
    pg.draw.rect(screen, 'red', food)
    # Desenha a cobra
    [pg.draw.rect(screen, 'green', segment) for segment in segments] 
    # Mover a cobra e controle de velocidade
    time_now = pg.time.get_ticks()
    if time_now - time > time_step:
        time = time_now
        snake.move_ip(snake_dir)
        segments.append(snake.copy())
        segments  = segments[-length:]
    pg.display.flip()
    clock.tick(60)
    
