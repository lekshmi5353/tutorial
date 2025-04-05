class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


rect = Rectangle(5, 3)
print(f"Area of Rectangle: {rect.area()} square units")
