def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]) or all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_board_full(board):
    return all([cell != " " for row in board for cell in row])

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player_idx = 0

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        row = int(input("Enter the row (0, 1, or 2): "))
        col = int(input("Enter the column (0, 1, or 2): "))

        if board[row][col] != " ":
            print("That position is already taken. Try again.")
            continue

        board[row][col] = players[current_player_idx]
        print_board(board)

        if check_winner(board, players[current_player_idx]):
            print(f"Player {players[current_player_idx]} wins! Congratulations!")
            break

        if is_board_full(board):
            print("It's a draw! Good game!")
            break

        current_player_idx = 1 - current_player_idx  # Switch player

if __name__ == "__main__":
    main()
