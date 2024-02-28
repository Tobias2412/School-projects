import random
from My_import import read_answers

answers = read_answers()

user_menu = ["1. Ask your fortune", "2. Add new sentence to file", "3. Quit"]
print("Welcome to the magic 8-ball!")

while True:
    for option in user_menu:
        print(option)
    menu_choice = input("What do you want to do?\n")

    if menu_choice == "1":
        wisdom = random.randint(0, len(answers)-1)
        question = input("What is your question?\n")
        if len(question) == 0:
            print('Please state your question.')
        elif question[len(question) - 1] == "?":
            print(answers[wisdom])
        else:
            print("That is not a question.")
    elif menu_choice == "2":
        new_wisdom = input("what is your new wisdom?\n")
        Magic_responses_opened = open(r'8_ball_responses.txt', 'a+')
        Magic_responses_opened.write("\n" + new_wisdom)
        Magic_responses_opened.close()
        answers.append(new_wisdom)
    elif menu_choice == "3":
        print("\nThank you for playing!")
        exit()
    else:
        print("Please choose between the 3 options.")