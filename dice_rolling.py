import random

def roll_dice():
    dice_drawing = {
        1: (
            "-----",
            "|   |",
            "| o |",
            "|   |",
            "-----",
        ),
        2: (
            "-----",
            "|o  |",
            "|   |",
            "|  o|",
            "-----",
        ),
        3: (
            "-----",
            "|o  |",
            "| o |",
            "|  o|",
            "-----",
        ),
        4: (
            "-----",
            "|o o|",
            "|   |",
            "|o o|",
            "-----",
        ),
        5: (
            "-----",
            "|o o|",
            "| o |",
            "|o o|",
            "-----",
        ),
        6: (
            "-----",
            "|o o|",
            "|o o|",
            "|o o|",
            "-----",
        ),

    }
    roll = input("Roll the dice? (Yes/No): ")

    while roll.lower() == "Yes".lower():
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)

        print(f"dice rolled: {dice_1} and {dice_2}")
        print("\n".join(dice_drawing[dice_1]), end="")
        print("\n".join(dice_drawing[dice_2]))

        roll = input("Roll again? (Yes/No): ")


roll_dice()