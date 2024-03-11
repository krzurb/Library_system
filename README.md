Simple Library System
Author: Krzysztof Urbanowski

The program consists of four Python files:
- `main.py`: executable script
- `functions.py`: definitions of functions used in `main.py`
- `Book.py`: class `Book`
- `Client.py`: class `Client`

Additionally, there are two CSV files to store data:
- `books_data.csv`
- `clients_data.csv`

Objects of the `Book` class have four attributes:
- Book name
- Year of publication
- Current available number of copies
- Overall number of copies

The `Book` class also has a class attribute `Books`, which is a list of all objects.

Objects of the `Client` class have two attributes:
- Client name
- Rented books list: a list of `Book` class objects that the client has rented

The `Client` class also has a class attribute `Clients`, which is a list of all objects.

Each time the program is run, data from `books_data.csv` and `clients_data.csv` is read. For each iteration of the while loop, the files are updated.

After running `main.py`, a window appears. There are ten options (buttons) that the user can choose from:
- Add a Client: adds a new client to the database. The user specifies a username via the terminal. The username is treated as a primary key, so only one client can have a given name.
- Remove a Client: removes a client from the database if it exists. The user cannot remove a client if they have rented books.
- Add a Book: adds a new book to the database. The user specifies the book name, year of publication, and number of copies via the terminal. Two books cannot have the same name and year of publication.
- Remove a Book: removes a book from the database if it exists. A book cannot be removed if all copies have not been returned.
- Rent a Book: rents a given book for a given client. The user specifies the username, book name, and year of publication via the terminal. A client can rent only one copy of each book. This option decrements the current available number of copies for the given book. The user cannot rent a book if its current available number of copies is equal to 0.
- Return a Book: returns a given book that a given client has rented. The user specifies the client name, book name, and year of publication via the terminal. This option increments the current available number of copies for the given book.
- Return all Books: returns all books from a given client. The user specifies the username via the terminal. This option increments the current available number of copies for all books that the client has rented.
- List of Clients: prints the attributes of the `Client` class for all `Client` objects.
- List of Books: prints the attributes of the `Book` class for all `Book` objects.
- Exit: ends the program.
