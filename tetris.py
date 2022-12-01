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

directions = {"left": (0, -1),
              "right": (0, 1),
              "up": (-1, 0),
              "down": (1, 0)}
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
        # table.collapse_similar()
        stick_color = 1
        stick_type_id = 0
        stick = Stick(stick_color, stick_type_id, table)

        # print("\nnext stick colors =", stick.color)

        if not control.add_stick(stick, table):
            print("Game Over.")
            done = True
        stick_count = 1

    if time() - start > delta_t:
        stick_count = control.move(stick, table, directions["down"])
        start = time()

    keys = pygame.key.get_pressed()

    # pause simulation
    if keys[pygame.K_p]:
        input()

    if keys[pygame.K_LEFT]:
        if not left_button_pressed:
            control.move(stick, table, directions["left"])
            left_button_pressed = 1
            left_button_pressed_time_start = time()
        if left_button_pressed:
            left_button_pressed_time = (
                time() - left_button_pressed_time_start)
            if left_button_pressed_time > button_press_delta:
                control.move(stick, table, directions["left"])
                left_button_pressed_time_start = time()
    else:
        left_button_pressed = 0

    if keys[pygame.K_RIGHT]:
        if not right_button_pressed:
            control.move(stick, table, directions["right"])
            right_button_pressed = 1
            right_button_pressed_time_start = time()
        if right_button_pressed:
            right_button_pressed_time = (
                time() - right_button_pressed_time_start)
            if right_button_pressed_time > button_press_delta:
                control.move(stick, table, directions["right"])
                right_button_pressed_time_start = time()
    else:
        right_button_pressed = 0

    if keys[pygame.K_UP]:
        if not up_button_pressed:
            control.rotate(stick, table)
            up_button_pressed = 1
            up_button_pressed_time_start = time()
        if up_button_pressed:
            up_button_pressed_time = (
                time() - up_button_pressed_time_start)
            if up_button_pressed_time > button_press_delta:
                control.rotate(stick, table)
                up_button_pressed_time_start = time()
    else:
        up_button_pressed = 0

    if keys[pygame.K_SPACE] or keys[pygame.K_DOWN]:
        if not down_button_pressed:
            control.put_down(stick, table, directions["down"])
            down_button_pressed = 1
            down_button_pressed_time_start = time()
        if down_button_pressed:
            down_button_pressed_time = (
                time() - down_button_pressed_time_start)
            if down_button_pressed_time > button_press_delta * 3:
                control.put_down(stick, table, directions["down"])
                down_button_pressed_time_start = time()
    else:
        down_button_pressed = 0

    render(table.table)
    clock.tick(fps)

pygame.quit()
