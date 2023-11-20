# HOMEWORK3
## Задача
Написать игру в “Крестики-нолики”. Можете использовать
любые парадигмы, которые посчитаете наиболее
подходящими. Можете реализовать доску как угодно - как
одномерный массив или двумерный массив (массив массивов).
Можете использовать как правила, так и хардкод, на своё
усмотрение. Главное, чтобы в игру можно было поиграть через
терминал с вашего компьютера.

## я использовал pygame c интерфейсом 

![Снимок экрана 2023-11-20 в 10.52.44.png](%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-11-20%20%D0%B2%2010.52.44.png)

![Снимок экрана 2023-11-20 в 10.52.51.png](%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-11-20%20%D0%B2%2010.52.51.png)
### код ниже
```python
import pygame
import sys
from pygame.color import THECOLORS


# pygame.mixer.init("Homework3/expl3.wav")
# Хотел прикрутить звук о не хватило времени!


def check_win(mas, sign):
    zrero = 0
    for row in mas:
        zrero += row.count(0)
        if row.count(sign) == 3:
            return sign
    for col in range(3):  # избегает одинаковые знаки
        if mas[0][col] == sign and mas[1][col] == sign and mas[2][col] == sign:
            return sign
    if mas[0][0] == sign and mas[1][1] == sign and mas[2][2] == sign:
        return sign
    if mas[0][2] == sign and mas[1][1] == sign and mas[2][0] == sign:
        return sign
    if zrero == 0:
        return "Ничья"
    return False


pygame.init()
size_block = 150
margin = 15  # Отступы
width = heigth = size_block * 3 + margin * 4  # Размер окна 3 блока 4 отступа

size_window = (width, heigth)
screan = pygame.display.set_mode(size_window)
pygame.display.set_caption('Крестики-нолики')

# значение цветов
# Цвета (R, G, B)
black = (0, 0, 0)
read = (255, 0, 0)
green = (0, 255, 0)
# green = (THECOLORS['orange'])
white = (255, 255, 255)
# Пустой массив
mas = [[0] * 3 for i in range(3)]

qwery = 0  # множества чисел
game_over = False

pob = 'Победил'

# Цикл обработки событий
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x_mous, y_mous = pygame.mouse.get_pos()
            col = x_mous // (size_block + margin)
            row = y_mous // (size_block + margin)
            if mas[row][col] == 0:
                if qwery % 2 == 0:  # Проверка на четность
                    mas[row][col] = 'Победил\n крестик'
                else:
                    mas[row][col] = 'Победил\n нолик'
                qwery += 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:  # блок для перезапуска игры
            game_over = False
            mas = [[0] * 3 for i in range(3)]
            qwery = 0
            screan.fill(black)

    # вложений цикл - обходит количество строк и столбцов  3 строки и 4 столбца
    if not game_over:
        for row in range(3):
            for col in range(3):
                if mas[row][col] == 'Победил\n крестик':
                    color = read
                elif mas[row][col] == 'Победил\n нолик':
                    color = green
                else:  # Col - колонка row - ряд
                    color = white
                x = col * size_block + (col + 1) * margin  # координаты для верхнего левого угла
                y = row * size_block + (row + 1) * margin
                pygame.draw.rect(screan, color, (x, y, size_block, size_block))  # координаты для верхнего правого угла
                if color == read:  # прорисовка крестика
                    pygame.draw.line(screan, black, (x, y), (x + size_block, y + size_block), 10)
                    pygame.draw.line(screan, black, (x + size_block, y), (x, y + size_block), 10)
                elif color == green:  # прорисовка нолика
                    pygame.draw.circle(screan, black, (x + size_block // 2, y + size_block // 2), size_block // 2 - 3,
                                       10)

    if (qwery - 1) % 2 == 0:
        game_over = check_win(mas, "Победил\n крестик")
    else:
        game_over = check_win(mas, "Победил\n нолик")
    if game_over:
        screan.fill(black)
        font = pygame.font.SysFont('Tahoma.ttf', 80)  # Название шрифта
        text1 = font.render(game_over, True, white)
        # text1 = font.render("Конец игры", True, white)
        text_rect = text1.get_rect()
        text_x = screan.get_width() / 2 - text_rect.width / 2  # Находит центр экрана
        text_y = screan.get_height() / 2 - text_rect.height / 2  # Находит центр экрана
        screan.blit(text1, [text_x, text_y])  # Выводит текст на экран
    pygame.display.update()

```