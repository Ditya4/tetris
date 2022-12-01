import pygame
from time import time
from model import Table, Stick
from view import Render
import control


rows = 15
columns = 12
size = 40
delta_t = 1
fps = 20
button_press_delta = 0.2
done = False
stick_count = 0
start = time()
clock = pygame.time.Clock()

table = Table(rows, columns)
render = Render(table.rows, table.columns, size)

left_button_pressed = 0
right_button_pressed = 0
up_button_pressed = 0
down_button_pressed = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if stick_count == 0:
        # print("\ntable before collapse\n", table)
        # comment next line
        # table.collapse_similar()
        stick_color = 1
        stick_type_id = 0
        stick = Stick(stick_color, stick_type_id, table)

        # print("\nnext stick colors =", stick.color)

        '''
        i am here, i want to draw stick to field and then add move down
        fuction.
        '''
        if not control.add_stick(stick, table):
            print("Game Over.")
            done = True
        stick_count = 1

    if time() - start > delta_t:
        stick_count = control.move_down(stick, table)
        start = time()

    keys = pygame.key.get_pressed()

    # pause simulation
    if keys[pygame.K_p]:
        input()

    render(table.table)
    clock.tick(fps)

pygame.quit()
