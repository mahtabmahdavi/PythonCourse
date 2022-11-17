import random

print("Roll the dice...")
dice_number = random.randint(1, 6)

if dice_number == 6:
    print(f"Dice number: {dice_number}")

    while dice_number == 6:
        dice_number = random.randint(1, 6)
        print(f"Dice number: {dice_number}")

else:
    print(f"Dice number: {dice_number}")
