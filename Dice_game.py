from random import randint
import Dice

roll_dice = (randint(1,6))

playerscore = 0
opponentscore = 0

game_over = False

while game_over == False:
    player = randint(1,6)
    opponent = randint(1,6)

    input("Roll the dice!\n")

    print("Player rolls")
    Terning.Dice(player)

    print("Opponent rolls")
    Terning.Dice(opponent)
    if player > opponent:

        print("Player scores 1 point")
        playerscore = playerscore+1

    elif player < opponent:
        print("Opponent scores 1 point")
        opponentscore = opponentscore+1

    else:
        print("It´s a tie. Go again!")

    print(f"playerscore= {playerscore} opponentscore= {opponentscore}")

    if playerscore == 6:
        print("Player wins! Fatality!")
        game_over = True
    elif opponentscore == 6:
        print("Opponent wins! Fatality!")
        game_over = True

print("Game over!")