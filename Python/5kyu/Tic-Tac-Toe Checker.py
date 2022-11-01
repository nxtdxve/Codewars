# https://www.codewars.com/kata/525caa5c1bf619d28c000335/

def is_solved(board):
    # Check rows
    for row in board:
        if len(set(row)) == 1 and row[0] != 0:
            return row[0]
    # Check columns
    for i in range(3):
        if len(set([row[i] for row in board])) == 1 and board[0][i] != 0:
            return board[0][i]
    # Check diagonals
    if len(set([board[i][i] for i in range(3)])) == 1 and board[0][0] != 0:
        return board[0][0]
    if len(set([board[i][2-i] for i in range(3)])) == 1 and board[0][2] != 0:
        return board[0][2]
    # Check if there are any zeros
    for row in board:
        if 0 in row:
            return -1
    # If no zeros and no winner, it's a draw
    return 0