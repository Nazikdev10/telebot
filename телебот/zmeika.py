
import pygame
import time
import random

pygame.init()

# Определение цветов
white = (255, 255, 255)
yellow = (255, 255, 102)  # Цвет счёта
black = (0, 0, 0)          # Цвет змейки
red = (213, 50, 80)        # Цвет сообщения о проигрыше
green = (0, 255, 0)       # Цвет пищи
blue = (50, 153, 213)     # Цвет фона

# Размеры экрана
dis_width = 700
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Змейка ')
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Загрузка звуков
eat_sound = pygame.mixer.Sound('zvuk-zmeya.mp3')  # Звук поедания
game_over_sound = pygame.mixer.Sound('fail-wha-wha-version.mp3')  # Звук проигрыша

# Загрузка изображения
menu_image = pygame.image.load('HD-wallpaper-classic-snake-adventures-snake-game.jpg')
menu_image = pygame.transform.scale(menu_image, (dis_width, dis_height))  # Масштабируем изображение
lose_image = pygame.image.load('green-grass-field-background-soccer-football-sports-lawn-pattern-texture-close-up-image-140438262.webp')
lose_image = pygame.transform.scale(lose_image, (900, 900))  # Масштабируем изображение

def Your_score(score):
    value = score_font.render("Ваш счёт: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def buttons(msg, x, y, w, h, inactive_color, active_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x + w > mouse[0] > x and y + h > mouse[1] > y:  # Если мышь над кнопкой
        pygame.draw.rect(dis, active_color, (x, y, w, h))
        if click[0] == 1 and action is not None:  # Если нажато ЛКМ
            action()
    else:
        pygame.draw.rect(dis, inactive_color, (x, y, w, h))
        
    small_text = pygame.font.SysFont("bahnschrift", 20)
    textSurf = small_text.render(msg, True, black)
    dis.blit(textSurf, (x + (w / 2 - textSurf.get_width() / 2), y + (h / 2 - textSurf.get_height() / 2)))

def gameLoop():
    game_over = False
    game_close = False
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0
    snake_List = []
    Length_of_snake = 1
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:
        while game_close:
            dis.fill(blue)  # Фон при проигрыше
            message("Ты проиграл", red)  # Сообщение о проигрыше
            Your_score(Length_of_snake - 1)
            dis.blit(lose_image, (dis_width / 2 - 100, dis_height / 2 - 100))  # Отображение изображения
            buttons("Играть снова", dis_width / 3, dis_height / 2 + 100, 120, 50, green, (0, 200, 0), gameLoop)
            buttons("Выйти", dis_width / 2, dis_height / 2 + 100, 120, 50, red, (200, 0, 0), pygame.quit)
            pygame.display.update()
            game_over_sound.play()  # Воспроизведение звука проигрыша
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)  # Фон игры
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])  # Пища
        snake_Head = [x1, y1]
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            eat_sound.play()  # Воспроизведение звука при поедании пищи
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
        
        clock.tick(snake_speed)

    pygame.quit()
    quit()

def menu():
    while True:
        dis.blit(menu_image, (0, 0))  # Отображаем фоновое изображение меню
        buttons("Играть", dis_width / 3, dis_height / 2, 120, 50, green, (0, 200, 0), gameLoop)
        buttons("Выйти", dis_width / 2, dis_height / 2, 120, 50, red, (200, 0, 0), pygame.quit)
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

menu()