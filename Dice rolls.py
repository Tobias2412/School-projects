from random import randint

def dice_roll():
    dice = randint(1, 6)
    dice_2 = randint(1, 6)
    print(f'dice roll: {dice} {dice_2}')
    if dice == dice_2:
        return 1

    return 0

print(dice_roll())
