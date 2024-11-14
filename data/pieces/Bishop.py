from data.ChessPieces import ChessPiece
from data.Validate_move import validate_diagonal_move


class Bishop(ChessPiece):
    def __str__(self):
        return 'B' if self.color == 'white' else 'b'

    def is_valid_move(self, start, end, board):
        return validate_diagonal_move(start, end, board)
