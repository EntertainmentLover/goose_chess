from data.ChessPieces import ChessPiece
import random


class Goose(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
        self.x = None
        self.y = None

    def __str__(self):
        return 'G' if self.color == 'white' else 'g'

    def is_valid_move(self, start, end, board):
        start_row, start_col = start
        end_row, end_col = end
        row_diff = abs(start_row - end_row)
        col_diff = abs(start_col - end_col)

        if (row_diff == 2 and col_diff == 0) or (row_diff == 0 and col_diff == 2):
            mid_row = (start_row + end_row) // 2
            mid_col = (start_col + end_col) // 2
            middle_square = board[mid_row][mid_col]
            if middle_square != '.':
                return True
            return False

        if (row_diff == 1 and col_diff == 1) or (row_diff == 1 and col_diff == 0) or (row_diff == 0 and col_diff == 1):
            return True

        return False

    def move(self, start, end, board):
        start_row, start_col = start
        end_row, end_col = end
        board[start_row][start_col] = '.'
        board[end_row][end_col] = self

        if abs(start_row - end_row) == 2 or abs(start_col - end_col) == 2:
            mid_row = (start_row + end_row) // 2
            mid_col = (start_col + end_col) // 2
            middle_square = board[mid_row][mid_col]

            if middle_square != '.':
                random_number = random.randint(1, 6)
                print(f"Гусь бросил кубик: {random_number}")
                if random_number % 2 == 0:
                    self.eat_piece(mid_row, mid_col, board)

        self.x, self.y = end
        return True

    def eat_piece(self, row, col, board):
        piece = board[row][col]
        if isinstance(piece, ChessPiece):
            board[row][col] = '.'
            print(f"{self} съел {piece}!")