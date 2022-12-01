def calculatePascalTriangle(height: int):
    triangle = []
    for row in range(1, height + 1):  
        temp = 1
        triangle.append([])
        for i in range(1, row + 1):
            triangle[row - 1].append(temp) 
            temp = int(temp * (row - i) / i)
    return triangle


def printPascalTriangle(triangle: int):
    for row in triangle:
        for elm in row:
            print("{:5}".format(elm), end = "")
        print()


n = int(input("Enter \'n\' as the height of Pascal triangle: "))
printPascalTriangle(calculatePascalTriangle(n))