from data.ChessPieces import ChessPiece


def validate_line_move(start, end, board):
    start_row, start_col = start
    end_row, end_col = end
    if start_row == end_row:
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


class Rook(ChessPiece):
    def __str__(self):
        return 'R' if self.color == 'white' else 'r'

    def is_valid_move(self, start, end, board):
        return validate_line_move(start, end, board)