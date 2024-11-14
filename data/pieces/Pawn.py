from data.ChessPieces import ChessPiece


class Pawn(ChessPiece):
    def __str__(self):
        return 'P' if self.color == 'white' else 'p'

    def is_valid_move(self, start, end, board):
        direction = -1 if self.color == 'white' else 1
        start_row, start_col = start
        end_row, end_col = end
        if end_col == start_col:
            if board[end_row][end_col] == '.':
                if (end_row - start_row) == direction:
                    return True
                if (end_row - start_row) == 2 * direction and start_row in [1, 6]:
                    return board[start_row + direction][start_col] == '.'
        elif abs(end_col - start_col) == 1 and (end_row - start_row) == direction:
            if board[end_row][end_col] != '.':
                return True
        return False
