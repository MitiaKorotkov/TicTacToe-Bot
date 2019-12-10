import pygame


class Board:
    """
    Класс игровой доски
    """
    def __init__(self, number_of_cells, size, x, y, color):
        self.number_of_cells = number_of_cells
        self.size = size
        self.x = x
        self.y = y
        self.color = color

    def draw(self, surface):
        for i in range(self.number_of_cells + 1):
            pygame.draw.line(surface, self.color, (self.x + i * self.size / self.number_of_cells, self.y),
                             (self.x + i * self.size / self.number_of_cells, self.y + self.size), 3)
        for i in range(self.number_of_cells + 1):
            pygame.draw.line(surface, self.color, (self.x, self.y + i * self.size / self.number_of_cells),
                             (self.x + self.size, self.y + i * self.size / self.number_of_cells), 3)



class Cross:
    """
    Класс крестика
    """
    def __init__(self, size, color):
        self.size = size
        self.x = 0
        self.y = 0
        self.color = color

    def draw(self, surface):
        pygame.draw.line(surface, self.color, (self.x - self.size, self.y - self.size),
                         (self.x + self.size, self.y + self.size), 4)
        pygame.draw.line(surface, self.color, (self.x - self.size, self.y + self.size),
                         (self.x + self.size, self.y - self.size), 4)


class Dot:
    """
    Класс нолика
    """
    def __init__(self, size, color):
        self.size = size
        self.x = 0
        self.y = 0
        self.color = color

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.size, int(0.2 * self.size))


if __name__ == '__main__':
    print('This module is not to run the program')
