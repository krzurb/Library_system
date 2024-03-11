from tkinter import Tk, Label, Button, StringVar
import time
import os
from Book import Book
from Client import Client
from functions import find_clients, find_books, save_clients_to_file, save_books_to_file
from functions import read_from_books, read_from_clients, to_int, print_lists

clients_file_path =  "clients_data.csv"
books_file_path = "books_data.csv"
read_from_books(books_file_path)
read_from_clients(clients_file_path, Book.books)

def main():
    while True:
        choice = display_menu()

        if choice == 10:
            print("Exiting...")
            save_clients_to_file(clients_file_path, Client.clients)
            save_books_to_file(books_file_path, Book.books)
            break

        if 1 <= choice <= 9:
            handle_menu_option(choice)
        else:
            print("Error - Invalid choice!")

        # Update and save to file
        save_clients_to_file(clients_file_path, Client.clients)
        save_books_to_file(books_file_path, Book.books)
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    root = Tk()
    root.title("Library Management System")

    choice_var = StringVar()

    def handle_choice(option):
        choice_var.set(option)
        root.destroy()

    Label(root, text="Select an option:").pack(pady=10)

    options = [
        "Add a Client", "Remove a Client", "Add a Book", "Remove a Book",
        "Rent a Book", "Return a Book","Return all Books", "List of Clients", "List of Books", "Exit"
    ]

    for index, option in enumerate(options, start=1):
        Button(root, text=option, command=lambda idx=index: handle_choice(idx)).pack()

    root.mainloop()

    return int(choice_var.get())

def handle_menu_option(choice):
    if choice == 1:
        client_name = input("Enter client name: ")
        if find_clients(Client.clients, client_name) is None:
            Client(client_name)
            print("Client has been added successfully!")
        else:
            print("Client already in the database!")
    elif choice == 2:
        client_name = input("Enter client name to be removed: ")
        find = find_clients(Client.clients, client_name)
        if find is not None:
            if not find.get_rented_books():
                yes_no = input(f"Are you sure you want to remove {client_name}? (y/n) ")
                if yes_no == "y":
                    print(f"Client {find.get_name()} removed successfully!")
                    Client.clients.remove(find)
                elif yes_no == "n":
                    print("Client has not been removed!")
                else:
                    print("Wrong y/n option!")
            else:
                print("Client needs to return all books to be removed!")
        else:
            print("Client doesn't exist!")
    elif choice == 3:
        book_name = input("Enter book name to be added: ")
        book_year = to_int(input("Enter year of publishing: "))
        if book_year is not None:
            if find_books(Book.books, book_name, book_year) is None:
                number_of_books = to_int(input("Enter number of books: "))
                if number_of_books > 0:
                    b1 = Book(book_name, book_year, number_of_books, number_of_books)
                    print("Book has been added successfully!")
                else:
                    print("Number of copies needs to be larger than 0!")
            else:
                print("Book already in the database!")
        else:
            pass
    elif choice == 4:
        book_name = input("Enter book name to be removed: ")
        book_year = to_int(input("Enter year of publishing: "))
        find = find_books(Book.books, book_name, book_year)
        if find is not None:
            if find.get_numbers() == find.get_max_numbers():
                yes_no = input(f"Are you sure you want to remove {book_name}? (y/n) ")
                if yes_no == "y":
                    print("Book has been removed successfully!")
                    Book.books.remove(find)
                elif yes_no == "n":
                    print("Book has not been removed!")
                else:
                    print("Wrong y/n option!")
            else:
                print("Not all copies have been returned!")
        else:
            print("Book doesn't exist!")
    elif choice == 5:
        client_name = input("Enter client name: ")
        client = find_clients(Client.clients, client_name)
        if client is not None:
            name = input("Enter book name that you want to rent: ")
            year = to_int(input("Enter year of publishing: "))
            book = find_books(Book.books, name, year)
            is_book_rented = find_books(client.get_rented_books(), name, year)
            if book is not None:
                if book.get_numbers() > 0 and is_book_rented is None:
                    client.add_rented_book(book)
                    book.decrement_numbers()
                    print("Book has been rented successfully!")
                else:
                    print("All copies have been rented or client has already rented this book!")
            else:
                print("Book doesn't exist!")
        else:
            print("Client doesn't exist!")
    elif choice == 6:
        client_name = input("Enter client name: ")
        client = find_clients(Client.clients, client_name)
        if client is not None:
            name = input("Enter book name that you want to return: ")
            year = to_int(input("Enter year of publishing: "))
            book = find_books(Book.books, name, year)
            is_book_rented = find_books(client.get_rented_books(), name, year)
            if book is not None:
                if is_book_rented is not None:
                    client.return_rented_book(book)
                    book.increment_numbers()
                    print("Book has been returned successfully!")
                else:
                    print("Book has not been rented by a client!")
            else:
                print("Book doesn't exist!")
        else:
            print("Client doesn't exist!")
    elif choice == 7:
        client_name = input("Enter client name: ")
        client = find_clients(Client.clients, client_name)
        if client is not None:
            if(len(client.get_rented_books())!=0):
                    yes_no = input(f"Are you sure you want to return all books from {client_name}? (y/n) ")
                    if yes_no=='y':
                        client.return_all()
                        print("Books have been returned successfully!")
                    elif yes_no=='n':
                        print("Books have not been returned!")
                    else:
                        print("Wrong y/n option!")
            else:
                    print("Client has not rented any books!")
        else:
            print("Client doesn't exist!")
    elif choice == 8:
        print("List of clients:\n")
        print_lists(clients_file_path)
        time.sleep(3)
    elif choice == 9:
        print("List of books:\n")
        print_lists(books_file_path)
        time.sleep(3)

if __name__ == '__main__':
    main()
