class Arith:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def read(self):
        self.num1 = float(input("Enter the first number: "))
        self.num2 = float(input("Enter the second number: "))

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Error! Division by zero."


calc = Arith()
calc.read()
print(f"Sum: {calc.add()}")
print(f"Difference: {calc.subtract()}")
print(f"Product: {calc.multiply()}")
print(f"Quotient: {calc.divide()}")

