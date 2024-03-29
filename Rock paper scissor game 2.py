import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def get_user_choice():
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").strip().lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper or scissors.")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 3) or \
         (user_choice == 'scissors' and computer_choice == 1) or \
         (user_choice == 'paper' and computer_choice == 2):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
        while True:
            computer_choice = get_computer_choice()
            user_choice = get_user_choice()

            print(f'Computer chose {computer_choice}')
            print(f'You chose {user_choice}')

            result = determine_winner(user_choice, computer_choice)
            print (result)

            play_again = input("Do you want to play again? (yes/no): ").strip().lower()
            if play_again != 'yes':
                break

if __name__ == "__main__":
    play_game()
