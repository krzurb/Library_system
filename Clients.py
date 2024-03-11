from Books import Book
class Client:
    clients = []
    def __init__(self,a):
        self.name = a
        Client.clients.append(self)
        self.rented_books=[]
    def get_name(self):
        return self.name
    def get_rented_books(self):
        return self.rented_books
    def rent_book(self,book):
        self.rented_books.append(book)
    def __del__(self):
        pass
    def add_rented_book(self,book):
        self.rented_books.append(book)
    def return_rented_book(self,book):
        self.rented_books.remove(book)
    def return_all(self):
        books=self.get_rented_books()
        for book in books:
            book.increment_numbers()
        self.rented_books.clear()

        