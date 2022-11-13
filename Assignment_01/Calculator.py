import math

print("Welcome to Mahtab's calculator")
print("1. summation")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Square Root")
print("6. Logarithm")
print("7. Sinus")
print("8. Cosine")
print("9. Tangent")
print("10. Cotangent")
print("11. Factorial")
print("12. exit")

while True:
    op = int(input("\nEnter your choice --> "))

    if op == 12:
        break

    elif op == 1 or op == 2 or op == 3 or op == 4:
        num_1 = float(input("Number 1: "))
        num_2 = float(input("Number 2: "))

        if op == 1:
            result = num_1 + num_2

        elif op == 2:
            result = num_1 - num_2

        elif op == 3:
            result = num_1 * num_2

        elif op == 4:
            if num_2 == 0:
                result = "Cannot divide by zero!"
            else:
                result = num_1 / num_2

    elif op == 6:
        num = float(input("Number: "))
        base = float(input("Base: "))
        result = math.log(num, base)

    elif op == 5 or op == 7 or op == 8 or op == 9 or op == 10 or op == 11:
        num = float(input("Number: "))

        if op == 5:
            if num >= 0:
                result = math.sqrt(num)
            else:
                result = "Negative numbers have no roots!"

        elif op == 7:
            result = math.sin(math.radians(num))

        elif op == 8:
            result = math.cos(math.radians(num))

        elif op == 9:
            result = math.tan(math.radians(num))

        elif op == 10:
            result = 1 / math.tan(math.radians(num))

        elif op == 11:
            fact = 1
            count = 1

            while count < num:
                fact *= (count + 1)
                count += 1

            result = fact

    else:
        result = "Command not found!"

    print(result)
        