n = int(input("Enter the length of the Fibonacci sequence you want: "))

first_element, second_element = 1, 1

if n <= 0:
    print("Your number must be greater than zero!")

if n == 1:
    print("Our Fibonacci sequence =", first_element)

elif n > 1:
    print("Our Fibonacci sequence = ", end = "")

    for i in range(n):
        if i == n - 1:
            print(first_element, end = "")
        else:
            print(first_element, end = ", ")
            fibo = first_element + second_element
            first_element = second_element
            second_element = fibo