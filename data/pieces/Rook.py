from data.ChessPieces import ChessPiece
from data.Validate_move import validate_line_move


class Rook(ChessPiece):
    def __str__(self):
        return 'R' if self.color == 'white' else 'r'

    def is_valid_move(self, start, end, board):
        return validate_line_move(start, end, board)