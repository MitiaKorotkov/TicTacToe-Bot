import pygame
import Classes


def win_check(array, x, y, obj):
    global moves_quantity, win_trigger
    """
    Функция проверяет наличия победной позиции

    :param array: Массив положений крестиков и ноликов
    :param x: координата проверяемой клетки поля по оси Х
    :param y: координата проверяемой клетки поля по оси У
    :param obj: Тип проверяемой фишки (Крестик/Нолик)
    """
    draw_check = 1
    win_diagonal1 = 0
    win_vertical = 0
    win_horizontal = 0
    win_diagonal2 = 0
    for I in range(-3, 4):
        if array[x + I][y + I] == array[x + I - 1][y + I - 1] == array[x + I + 1][y + I + 1] == obj:
            win_diagonal1 += 1
    for I in range(-3, 4):
        if array[x + I][y - I] == array[x + I - 1][y - I + 1] == array[x + I + 1][y - I - 1] == obj:
            win_diagonal2 += 1
    for I in range(-3, 4):
        if array[x][y + I] == array[x][y + I - 1] == array[x][y + I + 1] == obj:
            win_vertical += 1
    for I in range(-3, 4):
        if array[x + I][y] == array[x + I - 1][y] == array[x + I + 1][y] == obj:
            win_horizontal += 1
    if win_diagonal1 >= 3 or win_horizontal >= 3 or win_diagonal2 >= 3 or win_vertical >= 3:
        win_trigger = 1
        draw_check = 0
        if obj == 1:
            f = pygame.font.SysFont('serif', 50)
            text = f.render('Crosses win!', 1, RED)
            screen.blit(text, (800, 370))
        if obj == -1:
            f = pygame.font.SysFont('serif', 50)
            text = f.render('Dots win!', 1, BLUE)
            screen.blit(text, (800, 370))
    moves_quantity += 1
    if moves_quantity == number_of_cells * number_of_cells and draw_check == 1:
        f = pygame.font.SysFont('serif', 50)
        text = f.render('Draw!', 1, BLACK)
        screen.blit(text, (800, 370))


def start():
    """
    Главный цикл отрисовки
    """
    screen.fill((192, 192, 192))
    board = Classes.Board(number_of_cells, board_size, x_coord, y_coord, BLACK)
    check = 1
    board.draw(screen)
    while True:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                exit()
            if i.type == pygame.MOUSEBUTTONDOWN:
                click_x = 10 + ((i.pos[0] - board.x) // (board_size / number_of_cells))
                click_y = 10 + ((i.pos[1] - board.y) // (board_size / number_of_cells))
                if i.button == 1 and 100 < i.pos[0] < (100 + board_size) and 100 < i.pos[1] < (100 + board_size) and \
                        data[int(click_x)][int(click_y)] == 0 and win_trigger == 0:
                    if check == 1:
                        obj = Classes.Cross(chip_size, RED)
                        data[int(click_x)][int(click_y)] = check
                        check = -1
                    else:
                        obj = Classes.Dot(chip_size, BLUE)
                        data[int(click_x)][int(click_y)] = check
                        check = 1
                    obj.x = (click_x - 10) * (board_size / number_of_cells) + (board_size / number_of_cells) / 2 + 100
                    obj.y = (click_y - 10) * (board_size / number_of_cells) + (board_size / number_of_cells) / 2 + 100
                    obj.draw(screen)
                    win_check(data, int(click_x), int(click_y), -check)
        pygame.display.update()
        clock.tick(60)


def main():
    """
    Функция координирующая работу пограммы в целом
    """
    global number_of_cells, board_size, screen, clock, data, \
        win_trigger, x_coord, y_coord, BLACK, BLUE, RED, moves_quantity, chip_size
    pygame.init()
    number_of_cells = 20  # Количество клеток
    x_coord = 100  # Координата левого верхнего угла по оси Х
    y_coord = 100  # Координата левого верхнего угла по оси У
    win_trigger = 0  # Проверка наличия на поле выигрышной комбинации
    board_size = 600  # Визуальный размер доски
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)
    moves_quantity = 0  # Число сделанных ходов
    chip_size = int(board_size / number_of_cells / 2)  # Размер(радиус) фишки
    screen = pygame.display.set_mode((1200, 780))  # Инициализация окна
    clock = pygame.time.Clock()  # Таймер
    data = []  # Массив данных о расположении фигур
    for i in range(number_of_cells + 25):
        small_data = []
        for j in range(number_of_cells + 25):
            small_data.append(0)
        data.append(small_data)
    start()


if __name__ == '__main__':
    main()
