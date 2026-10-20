
def print_board(board):
    print()
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("--+---+--")
    print()


def check_winner(board, player):
    win_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in win_positions:
        if board[a] == board[b] == board[c] == player:
            return True
    return False


def minimax(board, is_maximizing):
    if check_winner(board, "O"):
        return 1

    if check_winner(board, "X"):
        return -1

    if " " not in board:
        return 0

    if is_maximizing:
        best_score = -float("inf")

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, False)
                board[i] = " "
                best_score = max(score, best_score)

        return best_score

    else:
        best_score = float("inf")

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, True)
                board[i] = " "
                best_score = min(score, best_score)

        return best_score


def computer_move(board):
    best_score = -float("inf")
    move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    if move is not None:
        board[move] = "O"


def play_game():
    board = [" "] * 9
    print("TIC-TAC-TOE AI")
    print("You are X. Computer is O.")
    print("Enter positions from 1 to 9.")

    while True:
        print_board([str(i + 1) if cell == " " else cell
                     for i, cell in enumerate(board)])

        try:
            position = int(input("Enter your position (1-9): ")) - 1
        except ValueError:
            print("Please enter a valid number.")
            continue

        if position < 0 or position > 8 or board[position] != " ":
            print("Invalid position. Try again.")
            continue

        board[position] = "X"

        if check_winner(board, "X"):
            print_board(board)
            print("Congratulations! You win!")
            break

        if " " not in board:
            print_board(board)
            print("It's a draw!")
            break

        computer_move(board)

        if check_winner(board, "O"):
            print_board(board)
            print("Computer wins!")
            break

        if " " not in board:
            print_board(board)
            print("It's a draw!")
            break


play_game()
