import datetime

input_seconds = int(input("Enter seconds: "))
time = str(datetime.timedelta(seconds = input_seconds))

print("Time =", time)