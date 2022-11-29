def move_down(stick, table):
    '''
    called when a tick of time is become
    '''
    print(table)

    print(stick.model.stick_model.y, stick.model.stick_model.x)
    input()
    # for i in range()


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
    if could_place(stick, table):
        pass
    '''
    for subfield_y in range(stick.model.stick_model.rows):
        for subfield_x in range(stick.model.stick_model.columns):
            if table[table_move_y(subfield_y, stick)][table_move_x(subfield_x, stick)] != 0:
                print("Game over. we cant create next stick.")
                
    
    for y_index in range(stick.model.stick_model.y,
                stick.model.stick_model.y + stick.model.stick_model.rows - 1):
        print(stick.model.stick_model.)
    '''















