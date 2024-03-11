class Book:
    books = [] # list of all Book objects
    def __init__(self,a,b,c,d):
        self.name = a
        self.year = b
        self.numbers = c
        self.max_numbers=d
        Book.books.append(self)
    def get_name(self):
        return self.name
    def get_year(self):
        return self.year
    def get_numbers(self):
        return self.numbers
    def get_max_numbers(self):
        return self.max_numbers
    def increment_numbers(self):
        self.numbers += 1
    def decrement_numbers(self):
        self.numbers -= 1
    
        