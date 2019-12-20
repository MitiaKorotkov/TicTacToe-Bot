import pygame
from Classes import *
import Bot

def main():
    global d, number_of_cells, boardsize, screen, clock, data,\
        win_trigger, xcoord, ycoord, black, blue, red, chip_size, moves
    pygame.init()
    number_of_cells = 20
    xcoord = 100
    ycoord = 100
    win_trigger = 0
    moves = 0
    boardsize = 600
    black = (0, 0, 0)
    blue = (0, 0, 255)
    red = (255, 0, 0)
    chip_size = int(boardsize / number_of_cells / 2)
    screen = pygame.display.set_mode((1200, 780))
    clock = pygame.time.Clock()
    data = []
    d = []
    for i in range(number_of_cells+20):
        small_data = []
        for j in range(number_of_cells+20):
            if i>=10 and j>=10 and i<=number_of_cells + 10 and j<=number_of_cells+10:
                small_data.append(0)
            else:
                small_data.append('b')
        data.append(small_data)
    start()


def win_check(array, x, y, obj):
    global win_trigger, moves, number_of_cells
    draw_check = 1
    win_diagonal1 = 0
    win_vertical = 0
    win_horizontal = 0
    win_diagonal2 = 0
    for i in range(-3, 4):
        if array[x + i][y + i] == array[x + i - 1][y + i - 1] == array[x + i + 1][y + i + 1] == obj:
            win_diagonal1 += 1
    for i in range(-3, 4):
        if array[x + i][y - i] == array[x + i - 1][y - i + 1] == array[x + i + 1][y - i - 1] == obj:
            win_diagonal2 += 1
    for i in range(-3, 4):
        if array[x][y + i] == array[x][y + i - 1] == array[x][y + i + 1] == obj:
            win_vertical += 1
    for i in range(-3, 4):
        if array[x + i][y] == array[x + i - 1][y] == array[x + i + 1][y] == obj:
            win_horizontal += 1
    if win_diagonal1 >= 3 or win_horizontal >= 3 or win_diagonal2 >= 3 or win_vertical >= 3:
        win_trigger = 1
        draw_check = 0
        if obj == 1:
            f = pygame.font.SysFont('serif', 50)
            text = f.render('Crosses win!', 1, red)
            screen.blit(text, (800, 370))
        if obj == -1:
            f = pygame.font.SysFont('serif', 50)
            text = f.render('Dots win!', 1, blue)
            screen.blit(text, (800, 370))
    moves += 1
    if moves == number_of_cells*number_of_cells and draw_check == 1:
        f = pygame.font.SysFont('serif', 50)
        text = f.render('Draw!', 1, black)
        screen.blit(text, (800, 370))


def start():
    global number_of_cells
    screen.fill((192, 192, 192))
    board = Board(number_of_cells, boardsize, xcoord, ycoord, black)
    check = 1
    board.draw(screen)
    while True:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                exit()
            if i.type == pygame.MOUSEBUTTONDOWN:
                click_x = 10 + ((i.pos[0] - board.x) // (boardsize / number_of_cells))
                click_y = 10 + ((i.pos[1] - board.y) // (boardsize / number_of_cells))
                if i.button == 1 and 100 < i.pos[0] < (100 + boardsize) and 100 < i.pos[1] < (100 + boardsize) and \
                        data[int(click_x)][int(click_y)] == 0 and win_trigger == 0:
                    obj = Cross(chip_size, red)
                    data[int(click_x)][int(click_y)] = check
                    check = -1
                    obj.x = (click_x - 10) * (boardsize / number_of_cells) + (boardsize / number_of_cells) / 2 + 100
                    obj.y = (click_y - 10) * (boardsize / number_of_cells) + (boardsize / number_of_cells) / 2 + 100
                    obj.draw(screen)
                    win_check(data, int(click_x), int(click_y), -check)
                    obj = Dot(chip_size, blue)
                    mas = Bot.bot(data)
                    bot_x = mas[0]
                    bot_y = mas[1]
                    data[bot_x][bot_y] = check
                    check = 1
                    obj.x = (bot_x - 10) * (boardsize / number_of_cells) + (boardsize / number_of_cells) / 2 + 100
                    obj.y = (bot_y - 10) * (boardsize / number_of_cells) + (boardsize / number_of_cells) / 2 + 100
                    obj.draw(screen)
                    win_check(data, bot_x, bot_y, -check)
        pygame.display.update()
        clock.tick(60)


main()
