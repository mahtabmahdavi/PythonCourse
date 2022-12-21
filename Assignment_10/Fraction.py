class Fraction:
    def __init__(self, numerator = 0, denominator = 1):
        # Properties
        self.numerator = numerator

        if denominator != 0:
            self.denominator = denominator
        else:
            self.denominator = 1
        

    # Methods
    def show(self):
        print(self.numerator, "/", self.denominator)


    def add(self, other):
        result = Fraction()
        result.numerator = self.numerator * other.denominator + self.denominator * other.numerator
        result.denominator = self.denominator * other.denominator
        return result


    def subtract(self, other):
        result = Fraction()
        result.numerator = self.numerator * other.denominator - self.denominator * other.numerator
        result.denominator = self.denominator * other.denominator
        return result


    def multiply(self, other):
        result = Fraction()
        result.numerator = self.numerator * other.numerator
        result.denominator = self.denominator * other.denominator
        return result


    def divide(self, other):
        result = Fraction()
        result.numerator = self.numerator * other.denominator
        result.denominator = self.denominator * other.numerator
        return result


    def simplify(self):
        commonFactor = 1

        for i in range(min(abs(self.numerator), abs(self.denominator)), 1, -1):
            if self.numerator % i == 0 and self.denominator % i == 0:
                commonFactor = i
                break

        result = Fraction()
        result.numerator = int(self.numerator / commonFactor)
        result.denominator = int(self.denominator / commonFactor)
        return result