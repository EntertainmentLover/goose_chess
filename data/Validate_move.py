def validate_line_move(start, end, board):
    start_row, start_col = start
    end_row, end_col = end
    if board[end[0]][end[1]] == '+':
        return False
    elif start_row == end_row:
        step = 1 if end_col > start_col else -1
        for col in range(start_col + step, end_col, step):
            if board[start_row][col] != '.':
                return False
        return True
    elif start_col == end_col:
        step = 1 if end_row > start_row else -1
        for row in range(start_row + step, end_row, step):
            if board[row][start_col] != '.':
                return False
        return True
    return False


def validate_diagonal_move(start, end, board):
    start_row, start_col = start
    end_row, end_col = end
    if board[end[0]][end[1]] == '+':
        return False
    elif abs(start_row - end_row) == abs(start_col - end_col):
        row_step = 1 if end_row > start_row else -1
        col_step = 1 if end_col > start_col else -1
        row, col = start_row + row_step, start_col + col_step
        while (row, col) != (end_row, end_col):
            if board[row][col] != '.':
                return False
            row += row_step
            col += col_step
        return True
    return False
