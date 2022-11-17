import random

print("Welcome to 'Rock Paper Scissors'")

user_win_counter = 0
computer_win_counter = 0

while user_win_counter < 5 and computer_win_counter < 5:
    print("Select one of them:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    user_choice = int(input("--> "))
    computer_choice = random.randint(1, 3)

    if user_choice == 1 and computer_choice == 1:
        print("You: Rock")
        print("Computer: Rock\n")

    elif user_choice == 1 and computer_choice == 2:
        print("You: Rock")
        print("Computer: Paper\n")
        computer_win_counter += 1

    elif user_choice == 1 and computer_choice == 3:
        print("You: Rock")
        print("Computer: Scissors\n")
        user_win_counter += 1

    elif user_choice == 2 and computer_choice == 1:
        print("You: Paper")
        print("Computer: Rock\n")
        user_win_counter += 1

    elif user_choice == 2 and computer_choice == 2:
        print("You: Paper")
        print("Computer: Paper\n")

    elif user_choice == 2 and computer_choice == 3:
        print("You: Paper")
        print("Computer: Scissors\n")
        computer_win_counter += 1

    elif user_choice == 3 and computer_choice == 1:
        print("You: Scissors")
        print("Computer: Rock\n")
        computer_win_counter += 1

    elif user_choice == 3 and computer_choice == 2:
        print("You: Scissors")
        print("Computer: Paper\n")
        user_win_counter += 1

    elif user_choice == 3 and computer_choice == 3:
        print("You: Scissors")
        print("Computer: Scissors\n")


if user_win_counter < computer_win_counter:
    print("The computer wins!")

elif user_win_counter > computer_win_counter:
    print("Congratulations! You win 🎉")