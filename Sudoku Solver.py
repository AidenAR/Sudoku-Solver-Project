## Sudoku Solver Using the Backtracking algorithm.


def sudoku_grid_display(board):
    '''
    Takes in a, 2D lists of Integers, returns None, but 
    prints the list as a valid sudoku board, with rows
    and columns separated by dashes (-)
    '''
    board_length = len(board)
    for row in range(board_length):
        if row % 3 == 0 and row != 0:
            print("- - - - - - - - - - - - - -")
        for column in range(len(board[0])):
            if column % 3 == 0 and column != 0 and column < 8:
                print(" | ", end="")
                
            if column == 8:
                print(board[row][column])
            else:
                print(str(board[row][column]) + " ", end="")


def find_empty_location(board, tracker):
    '''
    Locates an empty box (space) on a partially 
    complete sudoku board, and returns either None
    if no empty spot exists or returns the row 
    and column of the spot(box) as a 2 
    element list of Integers, in that order. 
    '''
    tracker = [0, 0]
    board_length = len(board)
    for row in range(board_length):
        for column in range(len(board[0])):
            if board[row][column] == 0:
                tracker[0] = row
                tracker[1] = column
                return tracker
    return None


def valid_move(board, pos, num):
    '''
    Returns True if a number entred in a particular box or 
    space  on a partially filled sudoku board is valid and
    conforms to the rules of Sudoku, else returns False. 
    '''
    board_length = len(board)
    
    # Check row of Board
    for num_row in range(len(board[0])):
        if (board[pos[0]][num_row] == num) and \
           (pos[1] != num_row):
            return False
        
    # Check Column of Board
    for num_col in range(board_length):
        if (board[num_col][pos[1]] == num) and \
           (pos[1] != num_col):
            return False
        
    # Check each 3 * 3 box
    box_horizontal = pos[1] // 3
    box_vertical = pos[0] // 3
    box_horizontal_range_begin = box_horizontal * 3
    box_horizontal_range_end = box_horizontal_range_begin + 3
    box_vertical_range_begin = box_vertical * 3
    box_vertical_range_end = box_vertical_range_begin + 3
    for vertical_num in \
            range(box_vertical_range_begin, box_vertical_range_end):
        for horizontal_num in \
                range(box_horizontal_range_begin, box_horizontal_range_end):
            if board[vertical_num][horizontal_num] == num \
               and [vertical_num, horizontal_num] != pos:
                return False
    return True


def sudoku_solve_bool(board):
    """
    Solves (mutates) a partially completed sudoku board
    using the backtracking algorithm, and returns True if 
    this was possible and False, otherwise. 
    """
    empty_box = find_empty_location(board, [])
    if empty_box != None:
        [row, column] = empty_box
    else:
        return True
    for i in range(1, 10):
        if valid_move(board, empty_box, i):
            board[row][column] = i
            if sudoku_solve_bool(board) == True:
                return True
            board[row][column] = 0
    return False


def sudoku_solver(board):
    '''
    Returns the solved sudoku board, of the passed 
    in partially completed one
    '''
    solved_board_indicator = sudoku_solve_bool(board)
    if solved_board_indicator == True:
        print("The solved Sudoku Board is shown below:")
        print("")
        return sudoku_grid_display(board)


#Example of a valid Board:
B = [[7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]]











