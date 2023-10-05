def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(row[col] == player for row in board):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def get_player_move(board, player):
    while True:
        try:
            row = int(input(f" {player}: Enter Row (0, 1, or 2): "))
            col = int(input(f" {player}: Enter Column (0, 1, or 2): "))

            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                return row, col
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a valid row and column (0, 1, or 2).")

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = {"X": "Player 1", "O": "Player 2"}
    current_player = "X"

    while True:
        print_board(board)
        row, col = get_player_move(board, players[current_player])
        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"{players[current_player]} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe()
