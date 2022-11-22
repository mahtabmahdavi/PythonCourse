first_num = int(input("First Number = "))
second_num = int(input("Second Number = "))
gcd = 0

if first_num > second_num:
    temp = second_num
else:  
    temp = first_num

for i in range(1, temp + 1):  
    if (( first_num % i == 0) and (second_num % i == 0 )):  
        gcd = i

print("GCD =", gcd)