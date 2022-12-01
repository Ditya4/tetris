
def rotate(stick, table):
    '''
    we check is there a possibility to place on table stick at
    next rotation index. If so we rotate in.
    '''
    if can_rotate(stick.rotation_index.next(), table):
        erase_stick(stick, table)
        rotate(stick.rotation_index.next(), table)


def can_rotate(stick_next, table):
    pass



def move(stick, table, direction):
    '''
    we get a direction like tuple of 2 (offset_y, offset_x) and send
    it to could_place function if we could place stick at that
    position we erase old stick, and "draw"(place on table correspondent
    colors_id) it at new position.
    '''

    if could_place(stick, table, direction):
        erase_stick(stick, table)
        place_stick(stick, table, direction)
        return 1
    else:
        return 0


def put_down(stick, table, direction):
    '''
    we call move function while it not return 0
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


def check_cells_on_table(cells_to_check, stick_model, table):
    '''
    to_table_y_offset and to_table_x_offset - are offsets from
    subfield to table.table.
    We check every cell in cells_to_check and find it's place on
    table. If corresponding cell on table is out of borders or has
    value different from zero we return False. If all corresponding
    cells are inside boards and every value is zero we return True.

    FIXME during move any direction in function below we didn't
    check if next cell is a cell of our stick, if so we should also
    move next. We should check no color of our stick, cause under(in direction)
    stick could be already placed on the bottom cell, with same color.
    or we throw out that case during previous check?
    '''
    to_table_y_offset = stick_model.table_y
    to_table_x_offset = stick_model.table_x
    for cell_y, cell_x in cells_to_check:
        '''
        in next if a change last and for or, mb cause some bags.
        '''
        if (0 < cell_y + to_table_y_offset < table.rows and
                0 <= cell_x + to_table_x_offset < table.columns and
                (table.table[cell_y + to_table_y_offset]
                            [cell_x + to_table_x_offset]) == 0):
            "we can put block inside this cell at the table"
        else:
            return False
    return True


def could_place(stick, table, offset):
    '''
    we find a cells in stick subfield, which are not zero and
    cells in direction, where we want to move are boards or zero
    if our move direction is _same_pos(0, 0) we add same cells in
    which are not zero values

    '''
    stick_model = stick.model.stick_model
    offset_y, offset_x = offset
    cells_to_check = []
    for y in range(stick_model.rows):
        for x in range(stick_model.columns):
            if stick_model.shape[y][x]:
                if offset_y == 0 and offset_x == 0:
                    cells_to_check.append((y, x))
                else:
                    if (y + offset_y == stick_model.rows or
                            y + offset_y == -1 or
                            x + offset_x == stick_model.columns or
                            x + offset_x == -1):
                        cells_to_check.append((y + offset_y, x + offset_x))
                    elif stick_model.shape[y + offset_y][x + offset_x] == 0:
                        cells_to_check.append((y + offset_y, x + offset_x))
                    else:
                        "Not do anything. We find not zero and not border."
    if not check_cells_on_table(cells_to_check, stick_model, table):
        "No we can't move/place"
        return False
    else:
        "Yes we can move/place"
        return True

        '''
        stick.model.stick_model.shape[y + offset_y][x + offset_x]
        cells_to_check.append((y + offset_y, x + offset_x))
        '''


def place_stick(stick, table, offset):
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
    same_pos = (0, 0)
    if could_place(stick, table, same_pos):
        # print("as;dfjlkdsjflk;dsajflkja asdflkjasdk;fljsad")
        place_stick(stick, table, same_pos)
        return True
    else:
        return False
    '''
    for subfield_y in range(stick.model.stick_model.rows):
        for subfield_x in range(stick.model.stick_model.columns):
            if table[table_move_y(subfield_y, stick)][table_move_x(subfield_x, stick)] != 0:
                print("Game over. we cant create next stick.")
                
    
    for y_index in range(stick.model.stick_model.y,
                stick.model.stick_model.y + stick.model.stick_model.rows - 1):
        print(stick.model.stick_model.)
    '''















