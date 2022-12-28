def generate_rug(n: int):
    if n % 2 == 0:
        return 1

    rug = [[0]]
    for i in range(1, n // 2 + 1):
        for row in rug:
            row.insert(0, i)
            row.append(i)  
        rug.insert(0, [i for j in range(2 * i + 1)])
        rug.append([i for j in range(2 * i + 1)])
    return rug


def print_rug(rug: int):
    for i in range(len(rug)):
        for j in range(len(rug[i])):
            print(rug[i][j], end = " ")
        print()


n = int(input("Enter N = "))
result = generate_rug(n)

if result == 1:
    print("Input cannot an odd number!")
else:
    print_rug(result)