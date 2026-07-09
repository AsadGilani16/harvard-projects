"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = 0
    o_count = 0
    empty_count = 0

    for rows in board:
        for item in rows:
            if (item == X):
                x_count += 1
            elif (item == O):
                o_count += 1
            elif (item == EMPTY):
                empty_count += 1
    if (empty_count == 9):
        return X
    elif ( x_count > o_count):
        return O
    elif (x_count < o_count):
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range (3):
        for j in range (3):
            if (board[i][j] == EMPTY):
                actions.add((i,j))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    row, column = action

    if ( row > 2 or row < 0 ):
        raise IndexError("Row number invalid")
    if ( column > 2 or column < 0 ):
        raise IndexError("Column number invalid")

    board_copy = copy.deepcopy(board)
    current = player(board_copy)
    board_copy[row][column] = current
    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    "horizaontal check"
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not EMPTY:
            return board[i][0]
        
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not EMPTY:
            return board[0][i]
        
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
            return board[0][0]

    if board[2][0] == board[1][1] == board[0][2] and board[2][0] is not EMPTY:
            return board[2][0]

    return None

   


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    current_winner = winner(board)
    if current_winner is not None:
        return True
    for i in range(3):
        for j in range (3):
            if board[i][j] == EMPTY:
                return False

    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    current_winner = winner(board)
    if current_winner is X:
        return 1
    elif current_winner is O:
        return -1
    else:
        return 0



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    currentTurn = player(board)
    if currentTurn == X:
        best_val = -float('inf')
        best_move = None
        for action in actions(board):
            move_val = min_value(result(board, action))
            if move_val > best_val:
                best_val = move_val
                best_move = action
        return best_move
    if currentTurn == O:
        best_val = float('inf')
        best_move = None
        for action in actions(board):
            move_val = max_value(result(board, action))
            if move_val < best_val:
                best_val = move_val
                best_move = action

        return best_move


def max_value(board):
    if terminal(board):
        return utility(board)
    
    v = -float('inf')
    possible_actions = actions(board)

    for action in possible_actions:
        v = max(v, min_value(result(board, action)))

    return v

def min_value(board):
    if terminal(board):
        return utility(board)

    v = float('inf')
    possible_actions = actions(board)

    for action in possible_actions:
        v = min(v, max_value(result(board, action)))
    return v