a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if a + b > c and a + c > b and b + c > a:
    print("Yes, It is possible.")
else:
    print("No, It isn't possible!")