import pygame


class Render():
    '''
    Draw squares on canvas  for every not zero table object,
    all zeros fill with black color. from index row index = 3
    our array have +3 rows for rotation a 4-th block stick at zero level
    and we need to display only rows from index 3.
    We have an array for our game field, filled with integer(int32) values,
    every value is a number which is equivalent to color.
    0 - black
    1 - red
    2 - blue
    3 - yellow
    4 - green
    5 - pygame.Color(252, 2, 252) pink
    6 - pygame.Color(4, 255, 252) light blue
    '''

    def __init__(self, rows, columns, size):
        self.rows = rows
        self.invisible_rows = 3
        self.columns = columns
        self.size = size
        self.canvas = self.create_canvas()
        pygame.init()
        self.colors_decode = {0: "black",
                              1: "red",
                              2: "blue",
                              3: "yellow",
                              4: "green",
                              5: pygame.Color(252, 2, 252),
                              6: pygame.Color(4, 255, 252),
                              }

    def create_canvas(self):
        window_height = self.size * (self.rows - self.invisible_rows)
        window_width = self.size * self.columns
        canvas = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption("Tetris")
        return canvas

    def __call__(self, table):
        self.draw_table(table)

    def draw_table(self, table):
        self.canvas.fill((0, 0, 0))
        for i in range(self.rows):
            for j in range(self.columns):
                if table[i][j] and i >= self.invisible_rows:
                    '''
                    print((i - self.invisible_rows) * self.size,
                          j * self.size,
                          table[i][j],
                          self.colors_decode[
                              table[i][j]])
                    '''
                    pygame.draw.rect(
                        self.canvas,
                        self.colors_decode[table[i][j]],
                        (j * self.size, (i - self.invisible_rows) * self.size,
                         self.size, self.size))
                    pygame.draw.rect(
                        self.canvas,
                        self.colors_decode[0],
                        (j * self.size, (i - self.invisible_rows) * self.size,
                         self.size, self.size), 1)
        pygame.display.update()

