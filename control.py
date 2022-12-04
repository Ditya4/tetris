
def rotate_stick(stick, table):
    stick_model = stick.model.stick_model

    erase_stick(stick, table)
    stick_model.rotation_index = stick_model.next_rotation_index()
    stick_model.shape = stick_model.rotations[stick_model.rotation_index]
    place_stick(stick, table)


def rotate(stick, table):
    '''
    we check is there a possibility to place on table stick at
    next rotation index. If so we rotate in.
    '''
    print("Call control.rotate.")
    if can_rotate(stick, table):
        erase_stick(stick, table)
        rotate_stick(stick, table)


def could_place(field, to_table_offset_y, to_table_offset_x,
                rows, columns, stick, table, offset=(0, 0)):
    '''
    #stick is our stick, in case we are called from rotation or None if we
    called from add_new.
    lets try to change input parameters from stick to subfield as array,
    subfield y, subfield x, subfield.rows, subfield.columns,
    offset gonna be not required parameter with default value (0, 0)
    old version
    we find a cells in stick subfield, which are not zero and
    cells in direction, where we want to move are boards or zero
    if our move direction is _same_pos(0, 0) we add same cells in
    which are not zero values

    '''
    # stick_model = stick.model.stick_model
    offset_y, offset_x = offset
    cells_to_check = []
    for y in range(rows):
        for x in range(columns):
            if field[y][x]:
                if offset_y == 0 and offset_x == 0:
                    cells_to_check.append((y, x))
                else:
                    if (y + offset_y == rows or
                            y + offset_y == -1 or
                            x + offset_x == columns or
                            x + offset_x == -1):
                        cells_to_check.append((y + offset_y, x + offset_x))
                    elif field[y + offset_y][x + offset_x] == 0:
                        cells_to_check.append((y + offset_y, x + offset_x))
                    else:
                        "Not do anything. We find not zero and not border."
    print(field, cells_to_check)
    if not check_cells_on_table(cells_to_check, to_table_offset_y,
                                to_table_offset_x, stick, table):
        "No we can't move/place"
        return False
    else:
        "Yes we can move/place"
        return True


def can_rotate(stick, table):
    stick_model = stick.model.stick_model
    if could_place(stick_model.rotations[stick_model.next_rotation_index()],
                   stick_model.table_y, stick_model.table_x,
                   stick_model.rows, stick_model.columns, stick, table):
        print("Can rotate.")
        return True
    else:
        print("Can't rotate.")
        return False


def move(stick, table, direction):
    '''
    we get a direction like tuple of 2 (offset_y, offset_x) and send
    it to could_place function if we could place stick at that
    position we erase old stick, and "draw"(place on table correspondent
    colors_id) it at new position.
    '''
    # could_place(field, to_table_offset_y, to_table_offset_x,
    #                 rows, columns, table, offset=(0, 0))
    stick_model = stick.model.stick_model
    if could_place(stick_model.shape, stick_model.table_y,
                   stick_model.table_x, stick_model.rows,
                   stick_model.columns, None, table, direction):
        erase_stick(stick, table)
        place_stick(stick, table, direction)
        return 1
    else:
        return 0


def put_down(stick, table, direction):
    '''
    we call move function with down direction while it not return 0
    '''
    while move(stick, table, direction):
        pass


def erase_stick(stick, table):
    '''
    we paint in black color(color which has index 0 at our table model)
    all cells, which are not zero once at our subfield model.
    '''
    black = 0
    stick_model = stick.model.stick_model
    to_table_y_offset = stick_model.table_y
    to_table_x_offset = stick_model.table_x

    for y in range(stick_model.rows):
        for x in range(stick_model.columns):
            if stick_model.shape[y][x]:
                (table.table[y + to_table_y_offset]
                            [x + to_table_x_offset]) = black


def check_cells_on_table(cells_to_check, to_table_y_offset,
                         to_table_x_offset, stick, table):
    '''
    #stick is our stick, in case we are called from rotation or None if we
    called from add_new.
    to_table_y_offset and to_table_x_offset - are offsets from
    subfield to table.table.
    We check every cell in cells_to_check and find it's place on visible
    table for columns and on table for rows. If corresponding cell on table
    is out of borders(visual border for columns and all borders for rows)
    or has value different from zero we return False or we should pass the case
    if our cells to check are the same as cells of our stick - it happened
    during rotation, when result cells could be the same as our previous cells.
    If all corresponding
    cells are inside boards and every value is zero we return True and if old
    cells are the same as our cells to check.

    FIXED during move any direction in function below we didn't
    check if next cell is a cell of our stick, if so we should also
    move next. We should check no color of our stick, cause under(in direction)
    stick could be already placed on the bottom cell, with same color.
    or we throw out that case during previous check? - Yes, this case is
    operated in previous function.

    FIXME if we rotate a stick some cells could be replaced by other/same
    cells of this stick. we should throw out cases, when it happened.
    '''
    # to_table_y_offset = stick_model.table_y
    # to_table_x_offset = stick_model.table_x
    if stick is not None:
        list_of_stick_cells = get_list_of_stick_cells(stick)
    print("control.check_cells_on_table", table)

    for cell_y, cell_x in cells_to_check:
        '''
        in next if condition i change last and for or, mb cause some bags.
        '''
        if stick is None:
            if (0 < cell_y + to_table_y_offset < table.rows and
                    0 <= cell_x + to_table_x_offset < table.columns and
                    # probably we need to add
                    # and cell_y, cell_x not in stick.cells
                    (table.table[cell_y + to_table_y_offset]
                    [cell_x + to_table_x_offset]) == 0):
                "we can put block inside this cell at the table"
            else:
                return False
        else:
            if (0 <= cell_y + to_table_y_offset < table.rows and
                    0 <= cell_x + to_table_x_offset < table.columns and
                    ((cell_y, cell_x) in list_of_stick_cells or
                     (table.table[cell_y + to_table_y_offset]
                      [cell_x + to_table_x_offset]) == 0)):
                "we can put block inside this cell at the table"
            else:
                return False

    return True


def get_list_of_stick_cells(stick):
    '''
    return list of (y, x) coordinates if every not zero objects
    in stick subfield.
    '''
    stick_model = stick.model.stick_model
    result = []
    for y in range(stick_model.rows):
        for x in range(stick_model.columns):
            if stick_model.shape[y][x]:
                result.append((y, x))
    return result


def place_stick(stick, table, offset=(0, 0)):
    print("Call place_stick function.")

    stick_model = stick.model.stick_model
    print(stick_model.shape)
    offset_y, offset_x = offset

    to_table_y_offset = stick_model.table_y + offset_y
    to_table_x_offset = stick_model.table_x + offset_x

    for y in range(stick_model.rows):
        for x in range(stick_model.columns):
            if stick_model.shape[y][x]:
                (table.table[y + to_table_y_offset]
                            [x + to_table_x_offset]) = stick.color

    stick_model.table_y = to_table_y_offset
    stick_model.table_x = to_table_x_offset


def add_stick(stick, table):
    '''
    in this function we need to place a stick on the table.
    our stick:
    self.table_y = 0
    self.table_x = 3
    self.rows = 4
    self.columns = 4
    OOOO
    OOOO
    OOOO
    1111
    if table_move_y we transform our subfield coordinates to field coordinates
    we have stick.y and stick.x which are ours field coordinates of left top of
    subfield
    @@@ how we gonna move our stick to the left wall of field, while it's vertical?
    our subfield left top x coordinate is gonna be -3. Let's create also 3 invisible
    columns?! or we need some other idea about stick rotation.
    '''

    '''
    lets create function, which will return which exactly cells should we check
    to have possibility to move our stick(or not to move, if we add_stick for
    the first time. so we give this function a stick, a table and move(dict of
    {"left": (-1, 0)
     "right": (1, 0)
     "down": (0, 1)
     "same_pos": (0, 0)}
    if this function we running of all not zero items and if in the direction,
    in which we want to move is zero or border of subfield we all this cell
    into list of cells, which should be checked, this list we return.
    '''
    stick_model = stick.model.stick_model
    same_pos = (0, 0)
    if could_place(stick_model.shape, stick_model.table_y, stick_model.table_x,
                   stick_model.rows, stick_model.columns,
                   None, table, same_pos):
        place_stick(stick, table, same_pos)
        return True
    else:
        return False
