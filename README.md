Simple library system
Author: Krzysztof Urbanowski

Program consists of 4 python files:
- main.py: exectuable script
- function.py: definitions of functions used in main.py
- Book.py: class Book
- Client.py: class Client
and 2 csv files to store data:
- books_data.csv
- clients_data.csv

Objects of class Book have 4 attributes:
- book name,
- year of publication,
- current available number of copies,
- overall number of copies.
Class Book has also class attribute Books which is a list of all objects.

Objects of class Client have 2 attributes:
- client name,
- rented books list: list of Book class obcjects that client has rented.
Class Client has also class attribute Clients which is a list of all objects.

Each time the program is run, data from booka_data.csv and clients_data is read. For each iteration of while loop, files are updated.

After running main.py, window appears. There are 10 options (buttons) that user can choose from:
- Add a Client: adds a new client to databes. By using terminal, user specify user name. User name is treated as primary key, so only one client can have given name.
- Remove a Client: removes client from database if it exists. User cannot remove client if it has rented books.
- Add a Book: adds a new book to databes. By using terminal, user specify book name, year of publication, number of copies. Two books cannot have the same name and year of puiblication.
- Remove a Book: removes book from databes if it exists. Book cannot be removed if all copies have not been returned.
- Rent a Book: rent a given book for given client. By using terminal, user specify user name, book name, year of publication. One client can rent one copy of each book. This option decrement current available number of copies of given book. User cannot rent a book if its current available number of copies is equal to 0.
- Return a Book: returns given book that given client has rented. By using terminal, user specify client name, book name and year of publication. This option increment currrent available number of copies of given book.
-  Return all Books: returs all books from given client. By using terminal, user specify user name. This option increments currrent available number of copies for all rented books.
- List of Clients: prints class Client attributes for all Client objects.
- List of Books: prints class Book attributes for all Book objects.
- Exit: ends the program.
