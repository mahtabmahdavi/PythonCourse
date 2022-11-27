print("Enter an array of numbers and press # at the end.")

numbers = []
temp_list = []

while True:
    number = input("--> ")

    if number == "#":
        break
    else:
        numbers.append(int(number))

for element in numbers:
    if element not in temp_list:
        temp_list.append(element)

numbers = temp_list
print("Non-repetitive List =", numbers)