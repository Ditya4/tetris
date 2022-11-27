import pygame
from time import time, sleep
from model import Table, Stick
from view import  Render
import control


rows = 15
columns = 11
size = 40
delta_t = 1
time_delay = 1
button_press_delta = 0.2
done = False
stick_count = 0
start = time()

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
        print("\ntable before collapse\n", table)
        # comment next line
        # table.collapse_similar()
        stick = Stick()
        print("\nnext stick colors =", stick.color)
        '''
        if not control.add_stick(stick, table):
            print("Game Over.")
            done = True
        stick_count = 1
        '''
    if time() - start > delta_t:
        # stick_count = control.move_down(stick, table)
        start = time()

    keys = pygame.key.get_pressed()

    # pause simulation
    if keys[pygame.K_p]:
        # sleep(12000)
        input()

    render(table.table)
    pygame.time.delay(time_delay)

pygame.quit()
