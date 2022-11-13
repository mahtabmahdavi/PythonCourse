weight = float(input("Enter your weight(kg): "))
height = float(input("Enter your height(m): "))

BMI = weight / (height * height)
print("\nBMI =", BMI)

if BMI < 18.5:
    print("Underweight")

elif BMI >= 18.5 and BMI < 25:
    print("Normal")

elif BMI >= 25 and BMI < 30:
    print("Overweight")

elif BMI >= 30 and BMI < 35:
    print("Obese")

elif BMI >= 35 and BMI < 40:
    print("Extremely Obese")

else:
    print("Undefined")