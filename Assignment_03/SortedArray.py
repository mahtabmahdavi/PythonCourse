print("Enter the integers for your array and press # at the end.")

input_number = None
numbers = []   

while True:
    input_number = input("--> ")

    if input_number == "#":
        break
    else:
        numbers.append(int(input_number))


for i in range(len(numbers) - 1):
    if numbers[i] <= numbers[i + 1]:
        if i + 1 == len(numbers) - 1:
            print("Yes, They are sorted in ascending order.")
        else:
            continue
    else:
        print("No, They are NOT sorted in ascending order!")
        break