from data.ChessPieces import ChessPiece


def validate_diagonal_move(start, end, board):
    start_row, start_col = start
    end_row, end_col = end
    if abs(start_row - end_row) == abs(start_col - end_col):
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


class Bishop(ChessPiece):
    def __str__(self):
        return 'B' if self.color == 'white' else 'b'

    def is_valid_move(self, start, end, board):
        return validate_diagonal_move(start, end, board)
