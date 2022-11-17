import random

computer_number = random.randint(1, 100)
print("Our number is between 1 to 100.")

guess_counter = 0

while True:
    guess_counter += 1
    user_guess = int(input("Enter your guess: "))

    if user_guess == computer_number:
        print("You win 🎉")
        print("Number of your guesses =", guess_counter)
        print(f"Our number is '{computer_number}'.")
        break

    elif user_guess < computer_number:
        print("Go up ⬆")

    else:
        print("Go down ⬇")