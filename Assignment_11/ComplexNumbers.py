class ComplexNumbers:
    # Properties
    def __init__(self, real = 0, imaginary = 0):
        self.real = real
        self.imaginary = imaginary

    # Methods
    def show(self):
        print(f"{self.real} + {self.imaginary}i")

    def add(self, other):
        result = ComplexNumbers()
        result.real = self.real + other.real
        result.imaginary = self.imaginary + other.imaginary
        return result

    def multiply(self, other):
        result = ComplexNumbers()
        result.real = self.real * other.real - self.imaginary * other.imaginary
        result.imaginary = self.real * other.imaginary + self.imaginary * other.real
        return result

    def subtract(self, other):
        result = ComplexNumbers()
        result.real = self.real - other.real
        result.imaginary = self.imaginary - other.imaginary
        return result

# Create objects from the Complex Numbers class
first_object = ComplexNumbers(3, -4)
second_object = ComplexNumbers(7, 2)

# Calling methods
result = first_object.add(second_object)
print("Add = ", end = "")
result.show()

result = first_object.multiply(second_object)
print("Multiply = ", end = "")
result.show()

result = first_object.subtract(second_object)
print("Subtract = ", end = "")
result.show()