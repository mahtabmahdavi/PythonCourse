def multiplicationTable(rows: int, cols: int):
    for num1 in range(1, rows + 1):
        for num2 in range(1, cols + 1):
            print("{:5}".format(num1 * num2), end = "")
        print()


n = int(input("Enter n: "))
m = int(input("Enter m: "))

multiplicationTable(n, m)