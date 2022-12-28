class Time:
    def __init__(self, hour = 0, minute = 0, second = 0):
        # Properties
        self.hour = hour
        self.minute = minute
        self.second = second
        self.convert_second_to_time()

    # Methods
    def show(self):
        print(self.hour, ":", self.minute, ":", self.second)

    def add(self, other):
        result = Time()
        result.hour = self.hour + other.hour
        result.minute = self.minute + other.minute
        result.second = self.second + other.second
        result.convert_second_to_time()
        return result

    def subtract(self, other):
        result = Time()
        self.subtract_helper(other)
        result.second = self.second - other.second
        result.minute = self.minute - other.minute
        result.hour = self.hour - other.hour
        return result

    def subtract_helper(self, other):
        if self.second < other.second:
            self.second += 60
            self.minute -= 1

        if self.minute < other.minute:
            self.minute += 60
            self.hour -= 1

    def convert_second_to_time(self):
        while self.second >= 60:
            self.second -= 60
            self.minute += 1

        while self.minute >= 60:
            self.minute -= 60
            self.hour += 1

    def convert_time_to_second(self):
        result = self.hour * 3600 + self.minute * 60 + self.second
        return result

    def convert_GMT_to_Tehran(self):
        result = Time()
        result.hour = self.hour + 3
        result.minute = self.minute + 30
        result.second = self.second
        result.convert_second_to_time()
        return result

# Create objects from the Time class
first_object = Time(0, 345, 121)
second_object = Time(8, 45, 5)

# Calling methods
result = first_object.add(second_object)
print("Add = ", end = "")
result.show()

result = first_object.subtract(second_object)
print("Subtract = ", end = "")
result.show()

first_object.convert_second_to_time()
print("Convert to time = ", end = "")
first_object.show()

print("Convert to seconds =",first_object.convert_time_to_second())

result = second_object.convert_GMT_to_Tehran()
print("Convert to Tehran = ", end = "")
result.show()