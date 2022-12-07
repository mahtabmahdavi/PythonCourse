import datetime
import random
import pyfiglet
from colorama import Fore


def menu():
    tittle = pyfiglet.figlet_format("Tic Tac Toe", font = "slant")
    print("Welcome to")
    print(tittle)
    print("Select one of the following options:")
    print("1. Single player(Your competitor is the computer)")
    print("2. Double player")


def gameType():
    choice = int(input("--> "))
    return choice


def showBoard():
    for row in gameBoard:
        for cell in row:
            if cell == "X":
                print(Fore.RED + "X", end = " ")
            elif cell == "O":
                print(Fore.BLUE + "O", end = " ")
            else:
                print(Fore.RESET + cell, end = " ")
        print(Fore.RESET)


def getInput(role: str, sign: str):
    while True:
        print(f"\n{role}")

        if role == "Computer":
            row = random.randint(0, 2)
            col = random.randint(0, 2)
            
            if gameBoard[row][col] == "-":
                gameBoard[row][col] = "O"
                print("row:", row + 1)
                print("col:", col + 1)
                break
        else:
            row = int(input("row (1 - 3): "))
            col = int(input("col (1 - 3): "))

            if 1 <= row <= 3 and 1 <= col <= 3:
                if gameBoard[row - 1][col - 1] == "-":
                    gameBoard[row - 1][col - 1] = sign
                    break
                else:
                    print("This cell is NOT empty! Please try again.")
            else:
                print("Row and Column must be between 1 and 3!")
            

def checkGame(role: str, sign: str, startTime: int):
    if checkWin(sign) == True:
        print(f"\n{role} wins!")
        endTime = datetime.datetime.now().replace(microsecond =0 )
        print("Game Duration:", endTime - startTime)
        exit()
    else:
        if checkDraw() == True:
            print("\nDraw!")
            endTime = datetime.datetime.now().replace(microsecond = 0)
            print("Game Duration:", endTime - startTime)
            exit()
            
            
def checkWin(sign: str):
    win = False

    for i in range(3):
        if (gameBoard[i][0] == gameBoard[i][1] == gameBoard[i][2] == sign) or (gameBoard[0][i] == gameBoard[1][i] == gameBoard[2][i] == sign):
            win = True
            break
    if (gameBoard[0][0] == gameBoard[1][1] == gameBoard[2][2] == sign) or (gameBoard[0][2] == gameBoard[1][1] == gameBoard[2][0] == sign):
        win = True
    
    return win


def checkDraw():
    if not any("-" in i for i in gameBoard):
        return True
    else:
        return False


def gamePlay(choice: int):
    showBoard()
    startTime = datetime.datetime.now().replace(microsecond = 0)

    if choice == 1:
        while True:
            getInput("Player", "X")
            showBoard()
            checkGame("Player", "X", startTime)
            
            getInput("Computer", "O")
            showBoard()
            checkGame("Computer", "O", startTime)

    elif choice == 2:
        while True:
            getInput("Player 1", "X")
            showBoard()
            checkGame("Player 1", "X", startTime)

            getInput("Player 2", "O")
            showBoard()
            checkGame("Player 2", "O", startTime)

    else:
        while True:
            print("The input is not valid!")
            choice = gameType()

            if choice == 1:
                break
            elif choice == 2:
                break
            
        gamePlay(choice)
               

gameBoard = [["-", "-", "-"],
             ["-", "-", "-"],
             ["-", "-", "-"]]

menu()
gamePlay(gameType())