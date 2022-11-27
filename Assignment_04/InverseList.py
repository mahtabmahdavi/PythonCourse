print("Enter an array of numbers and press # at the end.")

input_list = [] 
inverse_list = []  

while True:
    num = input("--> ")

    if num == "#":
        break
    else:
        input_list.append(int(num))

for i in range(len(input_list)-1, -1, -1):
    inverse_list.append(input_list[i])

print("Inverse List =", inverse_list)