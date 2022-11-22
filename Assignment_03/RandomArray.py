import random

n = int(input("Enter the size of the array (Maximum 100 elements): "))
numbers = []

for i in range(n):
    random_number = random.randint(0, 100)
    
    while random_number in numbers:
        random_number = random.randint(0, 100)
    
    numbers.append(random_number)

print("Array =", numbers)