import random
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

# Constants for players
PLAYER_X = 'X'  # Human player
PLAYER_O = 'O'  # AI player

# Function to print the Tic-Tac-Toe board with colors
def print_board(board):
    for row in board:
        for cell in row:
            if cell == PLAYER_X:
                print(Fore.YELLOW + cell, end=" | ")
            elif cell == PLAYER_O:
                print(Fore.RED + cell, end=" | ")
            else:
                print(cell, end=" | ")
        print("\n" + "-" * 9)

# Check if the current player has won
def check_win(board, player):
    for row in range(3):
        if all([cell == player for cell in board[row]]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]):
        return True
    if all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

# Check if the game board is full
def is_board_full(board):
    return all([cell != ' ' for row in board for cell in row])

# Find the best possible move using heuristic search
def best_move(board):
    # Check for a winning move for AI
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = PLAYER_O
                if check_win(board, PLAYER_O):
                    return (i, j)
                board[i][j] = ' '  # Undo move

    # Check for a blocking move for the human player
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = PLAYER_X
                if check_win(board, PLAYER_X):
                    board[i][j] = PLAYER_O
                    return (i, j)  # Block the winning move
                board[i][j] = ' '  # Undo move

    # Otherwise, pick a random available move
    available_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    return random.choice(available_moves)

# Function to play Tic-Tac-Toe
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]  # Empty board
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Human move (X)
        print("Your move (X): ")
        x, y = map(int, input("Enter row and column (0, 1, 2) separated by space: ").split())
        if board[x][y] == ' ':
            board[x][y] = PLAYER_X
        else:
            print("Invalid move. Try again.")
            continue

        print_board(board)

        if check_win(board, PLAYER_X):
            print(Fore.YELLOW + "You win!")
            break
        elif is_board_full(board):
            print("It's a draw!")
            break

        # AI move (O)
        print("AI's move (O): ")
        ai_move = best_move(board)
        board[ai_move[0]][ai_move[1]] = PLAYER_O
        print_board(board)

        if check_win(board, PLAYER_O):
            print(Fore.RED + "AI wins!")
            break
        elif is_board_full(board):
            print("It's a draw!")
            break

# Run the game
play_game()
