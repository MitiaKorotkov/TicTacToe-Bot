import pygame
import Classes

number_of_cells = 5  # Количество клеток
x_coord = 100  # Координата левого верхнего угла по оси Х
y_coord = 100  # Координата левого верхнего угла по оси У
win_trigger = 0  # Требуемое колличество фигур в ряду для победы
board_size = 600  # Визуальный размер доски
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
chip_size = None  # Fixme что это
screen = None  # Fixme что это
clock = None  # Таймер
data = None  # Массив данных о расположении фигур


def win_check(array, x, y, obj):
    """
    Функция проверяет наличия победной позиции

    :param array: Массив положений крестиков и ноликов
    :param x: координата проверяемой клетки поля по оси Х
    :param y: координата проверяемой клетки поля по оси У
    :param obj: Fixme Что это такое
    """
    pass


def start():
    """
    Главный цикл отрисовки
    """
    pass


def main():
    """
    Функция координирующая работу пограммы в целом
    """
    pass


if __name__ == '__main__':
    main()
