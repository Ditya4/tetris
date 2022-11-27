from random import choice
import pygame
import numpy as np


class Table():
    '''
    also we create 3 invisible lines by adding +3 to rows at _init function,
    so we have enough space to rotate 4-th block stick
    We create an array for our game field, filled with integer values,
    every value is a color which is equivalent to number.
    0 - black
    1 - red
    2 - blue
    3 - yellow
    4 - green
    5 - pygame.Color(252, 2, 252) pink
    6 - pygame.Color(4, 255, 252) light blue
    '''

    def __init__(self, rows, columns):
        self.rows = rows + 3
        self.columns = columns
        self.table = self.create_table()

    def create_table(self):
        result = np.zeros(self.rows * self.columns, np.int32).reshape(
                        self.rows, self.columns)
        # result[self.rows - 1] = np.ones(self.columns, np.int32)
        return result

    def __str__(self):
        return str(self.table)




class Stick():
    '''
    we create a random stick and return it
    '''

    def __init__(self):
        colors_codes = range(1, 7)
        self.color = colors_codes


