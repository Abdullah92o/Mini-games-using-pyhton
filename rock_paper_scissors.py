import random

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    print("Enter your choice: ")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    choices = ['rock', 'paper', 'scissors']
    player_choice = int(input("Your choice (1-3): ")) - 1

    if player_choice < 0 or player_choice >= 3:
        print("Invalid choice. Please try again.")
        return

    computer_choice = random.randint(0, 2)

    print("You chose:", choices[player_choice])
    print("Computer chose:", choices[computer_choice])

    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == 0 and computer_choice == 2) or \
         (player_choice == 1 and computer_choice == 0) or \
         (player_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("Computer wins!")

play_game()
