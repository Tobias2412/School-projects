import random


def play_game():
    random_number = random.randint(1,3)
    user_choice = input("You choose 'rock', 'paper', 'scissors':").lower()
    computer_choice = random_choice(['sten', 'saks', 'papir'])

    print(f'You choose {user_choice}')
    print(f'f Computer chooses computer_choice')

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'paper' and computer_choice == 'rock') or (user_choice == 'scissors' and computer_choice == 'paper'):
         print("You win!")
    else:
        print ("Computer wins!")

play_game()