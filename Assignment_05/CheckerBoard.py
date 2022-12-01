def printCheckerBoard(row_length: int, column_length: int):
    for row in range(row_length):
        for col in range(column_length):
            if (row % 2 == 0 and col % 2 == 0) or (row % 2 == 1 and col % 2 == 1):
                print("#", end = "")
            else:
                print("*", end = "")
        print()


n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))

printCheckerBoard(n, m)