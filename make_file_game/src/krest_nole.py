def print_b(board):
    for row in board:
        print(" | ".join(cell if cell else " " for cell in row))
        print("-" * 9)

def check_win(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def main():
    board = [["" for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0
    print("крестики-нолики \n игрок 1: X, игрок 2: O.")
    print("вводите координаты через пробел (x y),\n где x - строка, y - столбец (0-2).")

    while True:
        print(f"\nходит игрок {turn+1} ({players[turn]}).")
        try:
            x, y = map(int, input("Введите x y: ").split())
        except (ValueError, EOFError):
            print("ERRORE !!! PLEASE REPEAT AGAIN ^_^")
            continue
        if not (0 <= x < 3 and 0 <= y < 3) or board[x][y]:
            print("ERRORE !!! INCORRECT DANUE ^_^")
            continue

        board[x][y] = players[turn]
        print_b(board)

        if check_win(board, players[turn]):
            print(f"\nигрок {turn+1} ({players[turn]}) победил!")
            break
        if all(all(cell for cell in row) for row in board):
            print("\nничья!")
            break
        turn = 1 - turn

if __name__ == "__main__":
    main()