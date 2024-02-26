# Tic-Tac-Toe Game

# Create the board
board = [' ' for _ in range(9)]

# Function to print the board
def print_board():
    print('-------------')
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print('-------------')
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print('-------------')
    print('|', board[6], '|', board[7], '|', board[8], '|')
    print('-------------')

# Function to check if someone has won
def check_win(player):
    winning_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]

    for condition in winning_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False
# Function to play the game
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board()
    turn = 1
    while True:
        if turn % 2 != 0:
            player = 'X'
        else:
            player = 'O'

        choice = int(input("Player {} ({}): Choose an empty space (1-9): ".format(turn % 2 + 1, player)))

        if board[choice - 1] == ' ':
            board[choice - 1] = player
            print_board()
            if check_win(player):
                print("Player {} wins!".format(turn % 2 + 1))
                break
            elif turn == 9:
                print("It's a draw!")
                break
            turn += 1
        else:
            print("Invalid move! Try again.")
# Start the game
play_game()
