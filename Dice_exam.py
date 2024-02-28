import random

def dice_throw():
    die1 = random.randint(1, 6)
    print(die1)         # Test
    die2 = random.randint(1, 6)
    print(die2)         # Test
    dice_sum = die1 + die2
    print(dice_sum)     # Test
    return dice_sum

user_dice_throw = dice_throw()
print(user_dice_throw)