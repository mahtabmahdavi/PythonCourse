import jdatetime


class Date:
    def __init__(self, year = 0, month = 0, day = 0):
        # Properties
        self.year = year    
        self.month = month
        self.day = day
        self.convertDaysToDate()


    # Methods
    def show(self):
        print(self.year, "/", self.month, "/", self.day)


    def subtract(self, other):
        result = Date()
        self.subtractHelper(other)
        
        result.year = self.year - other.year
        result.month = self.month - other.month
        result.day = self.day - other.day
        
        return result


    def subtractHelper(self, other):
        if self.day < other.day:
            self.day += 30
            self.month -= 1

        if self.month < other.month:
            self.month += 30
            self.year -= 1


    def convertDaysToDate(self):
        while self.day > 30:
            self.day -= 30
            self.month += 1

        while self.month >= 12:
            self.month -= 12
            self.year += 1


    def convertDateToDays(self):
        result = self.year * 365 + self.month * 30 + self.day
        return result


    def convertJalaliToGregorian(self):
        tempDate = str(jdatetime.date(self.year, self.month, self.day).togregorian())
        tempDate = tempDate.split("-")

        result = Date()
        result.year = tempDate[0]
        result.month = tempDate[1]
        result.day = tempDate[2]

        return result


    def convertGregorianToJalali(self):
        tempDate = str(jdatetime.date.fromgregorian(day = self.day, month = self.month, year = self.year))
        tempDate = tempDate.split("-")

        result = Date()
        result.year = tempDate[0]
        result.month = tempDate[1]
        result.day = tempDate[2]

        return result