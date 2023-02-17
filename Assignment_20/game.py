import random
import pyfiglet


def menu():
    print("\nSelect one of them:")
    print("1. ✋")
    print("2. 🤚")

    choice = int(input("--> "))
    while True:
        if choice == 1 :
            return "✋"
        elif choice == 2:
            return "🤚"
        else:
            choice = int(input("Try again: "))

#--------------------------------------------------#

def play():
    user_win = 0
    computer1_win = 0
    computer2_win = 0

    for i in range(5):
        user_choice = menu()
        computer1_choice = random.choice(STATE)
        computer2_choice = random.choice(STATE)
            
        print(f"\nYou: {user_choice}")
        print(f"Computer 1: {computer1_choice}")
        print(f"Computer 2: {computer2_choice}")

        for j in range(len(STATE)):
            if user_choice != STATE[j] and computer1_choice == STATE[j] and computer2_choice == STATE[j]:
                user_win += 1
            elif user_choice == STATE[j] and computer1_choice != STATE[j] and computer2_choice == STATE[j]:
                computer1_win += 1
            elif user_choice == STATE[j] and computer1_choice == STATE[j] and computer2_choice != STATE[j]:
                computer2_win += 1

    return user_win, computer1_win, computer2_win

#--------------------------------------------------#

def find_winner(user_win: int, computer1_win: int, computer2_win: int):
    if user_win > computer1_win:
        if user_win > computer2_win:
            print("\nCongratulations! You win 🎉")
        elif user_win == computer2_win:
            print("\nYou & The computer2 win 🎉")
        else:
            print("\nThe computer2 wins!")

    elif user_win == computer1_win:
        if user_win > computer2_win:
            print("\nYou & The computer1 win 🎉")
        elif user_win == computer2_win:
            print("\nAll of you are equal.")
        else:
            print("\nThe computer2 wins!")
            
    else:
        if computer1_win > computer2_win:
            print("\nThe computer1 wins!")
        elif computer1_win == computer2_win:
            print("\nThe computer1 & The computer2 win!")
        else:
            print("\nThe computer2 wins!")

#--------------------------------------------------#
      
if __name__ == "__main__":
    tittle = pyfiglet.figlet_format("Palam Pooloum Pilish", font = "mini")
    print("Welcome to")
    print(tittle)

    STATE = ["✋", "🤚"]
    
    user_win, computer1_win, computer2_win = play()
    find_winner(user_win, computer1_win, computer2_win)