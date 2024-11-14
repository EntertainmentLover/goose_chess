from data.ChessPieces import ChessPiece


class Knight(ChessPiece):
    def __str__(self):
        return 'N' if self.color == 'white' else 'n'

    def is_valid_move(self, start, end, board):
        start_row, start_col = start
        end_row, end_col = end
        return (abs(start_row - end_row), abs(start_col - end_col)) in [(2, 1), (1, 2)]