class Book:
    def get_details(self, title, author, cost):
        self.title = title
        self.author = author
        self.cost = cost

    def print_details(self):
        print(f"Title: {self.title}, Author: {self.author}, Cost: ${self.cost}")


book = Book()
book.get_details("The Great Gatsby", "F. Scott Fitzgerald", 15)
book.print_details()
