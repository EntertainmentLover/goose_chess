from data.ChessPieces import ChessPiece


class Gravedigger(ChessPiece):
    def __str__(self):
        return 'M' if self.color == 'white' else 'm'

    @staticmethod
    def is_valid_move(start, end, board, **kwargs):
        return max(abs(start[0] - end[0]), abs(start[1] - end[1])) == 1

    def move(self, start, end, board):
        start_row, start_col = start
        end_row, end_col = end
        board[start_row][start_col] = '.'
        board[end_row][end_col] = self
