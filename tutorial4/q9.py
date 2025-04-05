class Rectangle:
    def __init__(self, height, width, corner_x, corner_y):
        self.height = height
        self.width = width
        self.corner_x = corner_x
        self.corner_y = corner_y

    def center(self):
        return (self.corner_x + self.width / 2, self.corner_y + self.height / 2)

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)


rect = Rectangle(4, 6, 2, 3)
print(f"Center: {rect.center()}")
print(f"Area: {rect.area()}")
print(f"Perimeter: {rect.perimeter()}")
