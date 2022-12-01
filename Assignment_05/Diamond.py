def printDiamond(height: int):
    for i in range(height):
        print(" " * (height - i), "*" * (2 * i + 1))

    for i in range(height - 2, -1, -1):
        print(" " * (height - i), "*" * (2 * i + 1))


n = int(input("Enter diamond's height: "))
printDiamond(n)