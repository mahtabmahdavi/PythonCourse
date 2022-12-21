class Time:
    def __init__(self, hour = 0, minute = 0, second = 0):
        # Properties
        self.hour = hour
        self.minute = minute
        self.second = second
        self.convertSecondToTime()


    # Methods
    def show(self):
        print(self.hour, ":", self.minute, ":", self.second)


    def add(self, other):
        result = Time()
        result.hour = self.hour + other.hour
        result.minute = self.minute + other.minute
        result.second = self.second + other.second
        result.convertSecondToTime()
        return result


    def subtract(self, other):
        result = Time()
        self.subtractHelper(other)
        result.second = self.second - other.second
        result.minute = self.minute - other.minute
        result.hour = self.hour - other.hour
        return result


    def subtractHelper(self, other):
        if self.second < other.second:
            self.second += 60
            self.minute -= 1

        if self.minute < other.minute:
            self.minute += 60
            self.hour -= 1


    def convertSecondToTime(self):
        while self.second >= 60:
            self.second -= 60
            self.minute += 1

        while self.minute >= 60:
            self.minute -= 60
            self.hour += 1


    def convertTimeToSecond(self):
        result = self.hour * 3600 + self.minute * 60 + self.second
        return result