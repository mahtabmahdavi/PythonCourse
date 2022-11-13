first_name = input("First Name: ")
last_name = input("Last Name: ")

grade_1 = float(input("grade 1: "))
grade_2 = float(input("grade 2: "))
grade_3 = float(input("grade 3: "))

avg = (grade_1 + grade_2 + grade_3) / 3
print(f"\n{first_name} {last_name}'s average = {avg}")
  
if avg >= 17:
    print("Great")

elif avg < 17 and avg >= 12:
      print("Normal")

elif avg < 12:
    print("Fail")


