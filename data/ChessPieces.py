class ChessPiece:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return ' '

    def is_valid_move(self, start, end, board):
        raise NotImplementedError("Этот метод должен быть реализован подклассами.")
