from random import choice
import pygame
import numpy as np


class Table():
    '''
    also we create 3 invisible lines by adding +3 to rows at _init function,
    so we have enough space to rotate 4-th block stick
    also we create 3 invisible columns on the left to have possibility to
    move our 4 block vertical stick, while it's vertical to the left border of
    table
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
        self.invisible_columns = 3
        self.invisible_rows = 3
        self.columns = columns + self.invisible_columns
        self.rows = rows + self.invisible_rows
        self.table = self.create_table()

    def create_table(self):
        result = np.zeros(self.rows * self.columns, np.int32).reshape(
                        self.rows, self.columns)
        # result[self.rows - 1] = np.ones(self.columns, np.int32)
        return result

    def __str__(self):
        return str(self.table)


class ZShape():
    '''
    ...
    .OO
    OO.
    '''

    def __init__(self, color, table):
        '''
        self.table_y - row index of left top block of sub-table, for
        this type of stick
        self.table_x - column index of left top block of sub-table, for
        this type of stick and remember, what we have table.invisible_columns
        on the left of our visible table.
        '''
        self.table_y = table.invisible_rows - 2
        self.table_x = 3 + table.invisible_columns
        self.color = color
        self.rows = 3
        self.columns = 3
        print("Create class ZShape")
        # self.shape = np.once(self.rows * self.columns, np.int32).reshape(
        #                 self.rows, self.columns)
        self.shape = np.array([0, 0, 0, 0, 1, 1, 1, 1, 0],
                              np.int32).reshape(self.rows, self.columns)
        print(self.shape)
        self.rotations = self.rotation_list()
        self.rotation_index = 0
        # input()

    def rotation_list(self):
        first = list(self.shape)
        second = np.rot90(first)
        result_list = [first, second]
        return result_list

    def next_rotation_index(self):
        '''
        if rotation index is last in rotations list we change it to zero,
        else we return increment of rotation index.
        '''
        if self.rotation_index < len(self.rotations) - 1:
            return self.rotation_index + 1
        elif self.rotation_index == len(self.rotations) - 1:
            return 0
        else:
            print("Some error in model.next_rotation_index.")


class TShape():
    '''
    ...
    OOO
    .O.
    '''

    def __init__(self, color, table):
        '''
        self.table_y - row index of left top block of sub-table, for
        this type of stick
        self.table_x - column index of left top block of sub-table, for
        this type of stick and remember, what we have table.invisible_columns
        on the left of our visible table.
        '''
        self.table_y = table.invisible_rows - 2
        self.table_x = 3 + table.invisible_columns
        self.color = color
        self.rows = 3
        self.columns = 3
        print("Create class TShape")
        # self.shape = np.once(self.rows * self.columns, np.int32).reshape(
        #                 self.rows, self.columns)
        self.shape = np.array([0, 0, 0, 1, 1, 1, 0, 1, 0],
                              np.int32).reshape(self.rows, self.columns)
        print(self.shape)
        self.rotations = self.rotation_list()
        self.rotation_index = 0
        # input()

    def rotation_list(self):
        first = list(np.array([0, 0, 0, 1, 1, 1, 0, 1, 0],
                              np.int32).reshape(self.rows, self.columns))
        second = np.rot90(first)
        third = np.rot90(second)
        fourth = np.rot90(third)
        result_list = [first, second, third, fourth]
        return result_list

    def next_rotation_index(self):
        '''
        if rotation index is last in rotations list we change it to zero,
        else we return increment of rotation index.
        '''
        if self.rotation_index < len(self.rotations) - 1:
            return self.rotation_index + 1
        elif self.rotation_index == len(self.rotations) - 1:
            return 0
        else:
            print("Some error in model.next_rotation_index.")


class Square():
    '''
    OO
    OO
    '''

    def __init__(self, color, table):
        '''
        self.table_y - row index of left top block of sub-table, for
        this type of stick
        self.table_x - column index of left top block of sub-table, for
        this type of stick and remember, what we have table.invisible_columns
        on the left of our visible table.
        '''
        self.table_y = table.invisible_rows - 1
        self.table_x = 3 + table.invisible_columns
        self.color = color
        self.rows = 2
        self.columns = 2
        print("Create class Square")
        # self.shape = np.once(self.rows * self.columns, np.int32).reshape(
        #                 self.rows, self.columns)
        self.shape = np.array([self.color] * self.rows * self.columns,
                              np.int32).reshape(self.rows, self.columns)
        print(self.shape)
        self.rotations = self.rotation_list()
        self.rotation_index = 0
        # input()

    def rotation_list(self):
        result = [np.array([self.color] * self.rows * self.columns,
                           np.int32).reshape(self.rows, self.columns)]
        return result

    def next_rotation_index(self):
        return 0


class StickShape():
    ''' OOOO - what is stick look like
    ....
    ....
    ....
    1111
    1 - is the color, where the blocks placed and . is empty spaces
    '''

    def __init__(self, color, table):
        '''
        self.table_y - row index of left top block of sub-table, for
        this type of stick
        self.table_x - column index of left top block of sub-table, for
        this type of stick and remember, what we have table.invisible_columns
        on the left of our visible table.
        '''
        self.table_y = 0
        self.table_x = 3 + table.invisible_columns
        self.color = color
        self.rows = 4
        self.columns = 4
        print("Create class StickShape")
        self.shape = np.zeros(self.rows * self.columns, np.int32).reshape(
                        self.rows, self.columns)
        self.shape[3] = np.array([self.color] * self.columns, np.int32)
        print(self.shape)
        self.rotations = self.rotation_list()
        self.rotation_index = 0
        # input()

    def rotation_list(self):
        first = list(np.zeros(self.rows * self.columns, np.int32).reshape(
                        self.rows, self.columns))
        first[self.rows - 1] = np.array([self.color] * self.columns, np.int32)

        second = np.rot90(first)
        result_list = [first, second]
        return result_list

    def next_rotation_index(self):
        '''
        if rotation index is last in rotations list we change it to zero,
        else we return increment of rotation index.
        '''
        if self.rotation_index < len(self.rotations) - 1:
            return self.rotation_index + 1
        elif self.rotation_index == len(self.rotations) - 1:
            return 0
        else:
            print("Some error in model.next_rotation_index.")


class StickType():

    def __init__(self, type_id, color, table):
        print("Create class StickType")
        '''
        probably we will create a class for each stick type
        and each rotation position
        and each??(this could be in this class and different
        for 3x3 4x4 subfields) function to check
        is the rotation possible.

          0   1   2   3   4  5   6
             OOO OOO OO OO   OO  O
        OOOO O     O OO  OO OO  OOO
        we send to constructor type id = integer from 0 to 6
        and create a certain figure, which has it's own
        placement in subfield
        we will be have 3 +- types of subfields:
        and a few rotation positions
        for OOOO
            .... .... ...O
            .... .... ...O
            .... .... ...O
            .... OOOO ...O
        for OOO
            O
        ... ... .OO ... .O.
        ... OOO ..O O.. .O.
        ... O.. ..O OOO .OO

        rotation_index is current position of stick
        '''
        self.Models = {0: StickShape,
                       1: Square,
                       2: TShape,
                       3: ZShape
                       }
        '''
        1: "red",
        2: "blue",
        3: "yellow",
        4: "green",
        5: pygame.Color(252, 2, 252),
        6: pygame.Color(4, 255, 252),
        '''

        self.type_id = type_id
        # big letter in self.Models is because all models are classes
        self.stick_model = self.Models[type_id](color, table)
        self.rotation_index = 0

    def rotate(self, sub_field):
        pass
        '''
        We check is there a possibility to rotate stick at current
        position in subfield. If so we add 1 to rotation index or, if
        rotation index already equal to max rotation positions, we
        make it equal to zero.
        rotation point will be right top corner of the subfield
        '''
        '''
        if stick_can_rotate(self, subfield):
            if self.rotation_index >= self.stick_model.rotation_positions_count:
                self.rotation_index = 0
            else:
                self.rotation_index += 1
        '''


class Stick():
    '''
    we create a stick with type, which is second parameter of
    constructor and color, which is first parameter of constructor
    we need to give our class a table to know about invisible columns count
    '''

    def __init__(self, color_code, type_id, table):
        print("Create class Stick")
        # colors_codes = range(1, 7)
        self.table = table
        self.color = color_code
        self.type_id = type_id
        self.model = StickType(self.type_id, self.color, self.table)



