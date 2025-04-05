class Car:
    def __init__(self, model, year, price):
        self.model = model
        self.year = year
        self.price = price

    def cost(self):
        print(f"Car Model: {self.model}, Year: {self.year}, Price: ${self.price}")



car1 = Car("Toyota Corolla", 2020, 20000)
car2 = Car("Honda Civic", 2022, 22000)



car1.cost()
car2.cost()
