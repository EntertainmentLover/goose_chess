from data.Board import *


def main():

    game = ChessBoard()
    game.display_board()

    while True:
        print(f"Ход: {game.current_turn}")
        action = input("Введите 'move' для хода, 'undo' для отмены, 'exit' для выхода: ").strip().lower()

        if action == 'move':
            try:
                start = parse_position(input("Введите начальную позицию (например, 'e2'): "))
                end = parse_position(input("Введите конечную позицию (например, 'e4'): "))
                game.move_piece(start, end)
                game.display_board()
                game_status = game.is_game_over()
                if game_status != "ongoing":
                    print(f"Игра завершена: {game_status}")
                    break
            except ValueError as e:
                print(e)

        elif action == 'undo':
            game.undo_move()
            game.display_board()

        elif action == 'exit':
            print("Игра завершена.")
            break


if __name__ == "__main__":
    main()
