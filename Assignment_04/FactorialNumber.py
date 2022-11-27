factorial_number = int(input("Enter an integer number: "))

fact, counter, result = 1, 1, 1

while result < factorial_number:
    fact *= (counter + 1)
    counter += 1
    result = fact

if result == factorial_number:
    print("Yes")
else:
    print("No")