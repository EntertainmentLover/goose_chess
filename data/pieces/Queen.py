from data.ChessPieces import ChessPiece
from data.Validate_move import *


class Queen(ChessPiece):
    def __str__(self):
        return 'Q' if self.color == 'white' else 'q'

    def is_valid_move(self, start, end, board):
        return validate_line_move(start, end, board) or validate_diagonal_move(
            start, end, board)
