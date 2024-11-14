from data.pieces.Gravedigger import *
from data.pieces.Bishop import *
from data.pieces.Goose import *
from data.pieces.King import *
from data.pieces.Knight import *
from data.pieces.Rook import *
from data.pieces.Queen import *
from data.pieces.Pawn import *


# noinspection PyTypeChecker
def create_board():
    board = [['.' for _ in range(8)] for _ in range(8)]
    board[0] = [Rook('black'),
                Knight('black'),
                Goose('black'),
                Queen('black'),
                King('black'),
                Bishop('black'),
                Gravedigger('black'),
                Rook('black')]
    board[1] = [Pawn('black')] * 8
    board[6] = [Pawn('white')] * 8
    board[7] = [Rook('white'),
                Knight('white'),
                Goose('white'),
                Queen('white'),
                King('white'),
                Bishop('white'),
                Gravedigger('white'),
                Rook('white')]
    return board


def parse_position(pos):
    if len(pos) != 2 or pos[0] not in "abcdefgh" or pos[1] not in "12345678":
        raise ValueError("Неверный формат позиции. Используйте 'a1' - 'h8'.")
    return 8 - int(pos[1]), ord(pos[0]) - ord('a')


class ChessBoard:
    def __init__(self):
        self.white_king_pos = None
        self.black_king_pos = None
        self.board = create_board()
        self.current_turn = 'white'
        self.move_history = []
        self.undo_stack = []

    def display_board(self):
        print("   a b c d e f g h")
        print(" +-----------------+")
        for i, row in enumerate(self.board):
            print(f"{8 - i}|", end=' ')
            for cell in row:
                if cell == '+':
                    print('+', end=' ')
                else:
                    print(str(cell), end=' ')
            print("|")
        print(" +-----------------+\n")

    def move_piece(self, start, end):
        start_row, start_col = start
        end_row, end_col = end
        piece = self.board[start_row][start_col]
        if isinstance(piece, ChessPiece) and piece.color == self.current_turn:
            target_piece = self.board[end_row][end_col]
            if isinstance(target_piece, ChessPiece) and target_piece.color == piece.color:
                print("Тупой, не ешь свои фигуры")
                return False
            elif isinstance(piece, Goose):
                piece.move(start, end, self.board)
                self.move_history.append(f"{piece} from {start} to {end}")
                self.undo_stack.append((start, end, piece))
                self.current_turn = 'black' if self.current_turn == 'white' else 'white'
            elif isinstance(piece, Gravedigger):
                if piece.is_valid_move(start, end, self.board):
                    piece.move(start, end, self.board)
                    self.move_history.append(f"{piece} from {start} to {end}")
                    self.undo_stack.append((start, end, piece))
                    self.current_turn = 'black' if self.current_turn == 'white' else 'white'
                    block = parse_position(input("Введите позицию для блокировки (например, 'c5'): "))
                    self.block_pos(self.current_turn, block)
                    self.display_board()
                    self.current_turn = 'black' if self.current_turn == 'white' else 'white'
            else:
                if piece.is_valid_move(start, end, self.board):
                    self.undo_stack.append((start, end, piece))
                    self.move_history.append(f"{piece} from {start} to {end}")

                    # noinspection PyTypeChecker

                    self.board[end[0]][end[1]] = piece
                    self.board[start[0]][start[1]] = '.'
                    if isinstance(piece, King):
                        if piece.color == 'white':
                            self.white_king_pos = end
                        else:
                            self.black_king_pos = end
                    self.current_turn = 'black' if self.current_turn == 'white' else 'white'
                else:
                    print("Неверный ход!")
        else:
            print("Нет фигуры в стартовой позиции или неверный игрок.")

    def is_valid_move(self, piece, start, end):
        if piece == '.':
            print("Нет фигуры в стартовой позиции.")
            return False
        if (self.current_turn == 'white' and piece.color == 'black') or (
                self.current_turn == 'black' and piece.color == 'white'):
            print("Неверный игрок для этой фигуры.")
            return False
        if not piece.is_valid_move(start, end, self.board):
            print(f"Неверный ход для {piece} с {start} на {end}.")
            return False
        if self.is_king_in_check_after_move(start, end, piece):
            print("Ход приводит к шаху королю!")
            return False
        return True

    def undo_move(self):
        if self.undo_stack:
            start, end, piece = self.undo_stack.pop()
            self.board[start[0]][start[1]] = piece
            self.board[end[0]][end[1]] = '.'
            self.current_turn = 'black' if self.current_turn == 'white' else 'white'
            print(f"Ход отменен: {piece.__class__.__name__} с {end} на {start}")
        else:
            print("Нет ходов для отмены.")

    def is_king_in_check(self, king_pos, king_color):
        enemy_color = 'black' if king_color == 'white' else 'white'
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if isinstance(piece, ChessPiece) and piece.color == enemy_color:
                    if piece.is_valid_move((row, col), king_pos, self.board):
                        return True
        return False

    def is_game_over(self):
        if self.is_king_in_check(self.get_king_position('white'), 'white'):
            if not self.has_legal_moves('white'):
                return "checkmate"
            return "check"
        if self.is_king_in_check(self.get_king_position('black'), 'black'):
            if not self.has_legal_moves('black'):
                return "checkmate"
            return "check"
        if not self.has_legal_moves('white') and not self.has_legal_moves('black'):
            return "draw"
        return "ongoing"

    def get_king_position(self, color):
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if isinstance(piece, King) and piece.color == color:
                    return row, col
        return None

    def has_legal_moves(self, color):
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if isinstance(piece, ChessPiece) and piece.color == color:
                    for target_row in range(8):
                        for target_col in range(8):
                            if piece.is_valid_move((row, col), (target_row, target_col), self.board):
                                return True
        return False

    def block_pos(self, color, pos):
        pos_row, pos_col = pos
        piece = self.board[pos_row][pos_col]
        if piece == '.':
            self.board[pos_row][pos_col] = '+'
            print(f"Клетка {pos} заблокирована Могильщиком.")
            self.current_turn = 'black' if self.current_turn == 'white' else 'white'
        else:
            print(f"Невозможно заблокировать клетку {pos}, так как она занята фигурой.")

    def is_king_in_check_after_move(self, start, end, piece):
        pass
