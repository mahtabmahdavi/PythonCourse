def get_numbers():
    numbers = []
    print("Enter your array then enter the symbol \".\" at the end:")
    while(True):
        temp = input()
        if(temp == "."):
            break
        else:
            numbers.append(float(temp))
    return numbers

def check_symmetric(numbers: float):
    for i in range(len(numbers) // 2):
        if(numbers[i] == numbers[len(numbers) - 1 - i]):
            continue
        else:
            print("This array is NOT symmetric!")
            exit()
    print("This array is symmetric.")


if __name__ == "__main__":
    check_symmetric(get_numbers())