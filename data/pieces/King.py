from data.ChessPieces import ChessPiece


class King(ChessPiece):
    def __str__(self):
        return 'K' if self.color == 'white' else 'k'

    def is_valid_move(self, start, end, board):
        return max(abs(start[0] - end[0]), abs(start[1] - end[1])) == 1
