"""
This is milestone project -1 for Tic Tac Toe Game.
Author:; Soumya Das
"""
def print_board(matrix):
    """
    Prints the board in stdout
    :param matrix: matrix having values and separators.
    :return: Returns nothing.
    """
    """
    :param matrix:
    :return:
    """
    print(''.join(matrix[0]))
    print(matrix[1])
    print(''.join(matrix[2]))
    print(matrix[3])
    print(''.join(matrix[4]))


def check_result():
    """
    Validates the matrix, if there is a winner.
    Rules -
    Horizontal symmetry.
    Vertical symmetry.
    Diagonal symmetry left to right.
    Diagonal symmetry right to left.
    :return:
    """
    """
    :return:
    """
    global matrix
    global winner

    #print(matrix)
    #print('Check horizontal matches')
    for i in range(0,5,2):
        hs=set([matrix[i][0], matrix[i][2], matrix[i][4]])
        if len(hs)==1:
            c=hs.pop()
            if c=='X':
                winner=1
            elif c=='O':
                winner=2
        else:
            pass
        #print(hs)

    #print('Check vertical matches')
    for j in range(0,5,2):
        vs=set([matrix[0][j],matrix[2][j],matrix[4][j]])
        if len(vs)==1:
            c=vs.pop()
            if c=='X':
                winner=1
            elif c=='O':
                winner=2
        else:
            pass
        #print(vs)

    #print('Check diagonal matches')
    ds_lr=set([matrix[0][0],matrix[2][2],matrix[4][4]])
    if len(ds_lr)==1:
        c=ds_lr.pop()
        if c=='X':
            winner=1
        elif c=='O':
            winner=2
    else:
        pass
    #print(ds_lr)

    ds_rl=set([matrix[0][-1],matrix[2][2],matrix[4][0]])
    if len(ds_rl)==1:
        c=ds_rl.pop()
        if c=='X':
            winner=1
        elif c=='O':
            winner=2
    else:
        pass
    #print(ds_rl)



    if winner in (1,2):
        return('Result')
    else:
        return('inProgress')


def is_empty_cell(x,y):
    """
    This function checks if a cell is empty for user to block.
    :param x: row in board.
    :param y: column in board.
    :return: True if empty False if already used.
    """
    global matrix
    global row_col_map
    list_element=row_col_map[x]
    list_val_element=row_col_map[y]
    if matrix[list_element][list_val_element]=='*':
        return(True)
    else:
        return (False)

def change_matrix_val(x,y,val):
    """
    This function puts a value X or O on the board as a result of user input.
    :param x: Row on the board.
    :param y: Column on the board.
    :param val: Value to be printed (X for first user, O for second user).
    :return: Returns nothing.
    """
    global matrix
    global row_col_map
    list_element=row_col_map[x]
    list_val_element=row_col_map[y]
    #print(matrix)
    #print(list_element)
    #print(list_val_element)
    #print(val)
    #print(matrix[list_element][list_val_element])
    matrix[list_element][list_val_element]=val
    #print(matrix)

def user_input():
    """
    This function asks for user input [row and column].
    It also calls a function to change the value in matrix board.
    :return: Returns nothing.
    """
    global matrix
    global num_user
    global cell_left
    if num_user==1:
        iden_char='X'
        next_user=2
    else:
        iden_char='O'
        next_user=1
    input_ready=False
    while(input_ready==False):
        while(True):
            x=input('Player {} enter row:'.format(num_user))
            if x.isnumeric()==True and int(x)<=3 and int(x)>=1:
                break
            else:
                print('Invalid value of row, re-enter')
                continue
        while(True):
            y=input('Player {} enter column:'.format(num_user))
            if y.isnumeric()==True and int(y)<=3 and int(y)>=1:
                break
            else:
                print('Invalid value of column, re-enter')
                continue
        x=int(x)
        y=int(y)
        correct=input('Press Y or y if correct, otherwise press any other character:')
        if correct=='y' or correct=='Y':
            if is_empty_cell(x,y):
                input_ready=True
            else:
                print('Cell {},{} is already used'.format(x,y))
                input_ready=False
        else:
            input_ready=False

    change_matrix_val(x,y,iden_char)
    print_board(matrix)
    cell_left-=1
    num_user=next_user


if __name__ == '__main__':
    line_sep='--------'
    matrix=[['*','|','*','|','*'],line_sep,['*','|','*','|','*'],line_sep,['*','|','*','|','*']]
    row_col_map={1:0,2:2,3:4}
    winner=-1
    print_board(matrix)
    result='inProgress'
    cell_left=9
    num_user=1
    while(check_result()=='inProgress' and cell_left>0):
        user_input()
    if winner == -1 and cell_left==0:
        print('Match drawn')
    elif winner != -1:
        print('Winner is player -{}'.format(winner))
    else:
        print("Can't determine status")
        print(matrix)
        print(check_result())
        print('Cell left - {}'.format(cell_left))

