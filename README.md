ENG

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


PL


Prosty system biblioteczny
Autor: Krzysztof Urbanowski

Program składa się z czterech plików w języku Python:
- `main.py`: skrypt wykonywalny
- `functions.py`: definicje funkcji używanych w `main.py`
- `Book.py`: klasa `Book`
- `Client.py`: klasa `Client`

Dodatkowo, istnieją dwa pliki CSV do przechowywania danych:
- `books_data.csv`
- `clients_data.csv`

Obiekty klasy `Book` posiadają cztery atrybuty:
- Nazwa książki
- Rok wydania
- Aktualna dostępna liczba kopii
- Ogólna liczba kopii

Klasa `Book` posiada także atrybut klasy `Books`, który jest listą wszystkich obiektów.

Obiekty klasy `Client` posiadają dwa atrybuty:
- Nazwa klienta
- Lista wypożyczonych książek: lista obiektów klasy `Book`, które klient wypożyczył

Klasa `Client` posiada także atrybut klasy `Clients`, który jest listą wszystkich obiektów.

Za każdym razem, gdy program jest uruchamiany, dane z plików `books_data.csv` i `clients_data.csv` są odczytywane. W każdej iteracji pętli while pliki są aktualizowane.

Po uruchomieniu `main.py` pojawia się okno wyboru. Dostępnych jest dziesięć opcji (przycisków), z których użytkownik może wybierać:
- Add a Client: dodaje nowego klienta do bazy danych. Użytkownik określa nazwę użytkownika za pośrednictwem terminala. Nazwa użytkownika traktowana jest jako klucz główny, więc tylko jeden klient może mieć daną nazwę.
- Remove a Client: usuwa klienta z bazy danych, jeśli istnieje. Użytkownik nie może usunąć klienta, jeśli ten ma wypożyczone książki.
- Add a Book: dodaje nową książkę do bazy danych. Użytkownik określa nazwę książki, rok wydania i liczbę kopii za pośrednictwem terminala. Dwie książki nie mogą mieć takiej samej nazwy i roku wydania.
- Remove a Book: usuwa książkę z bazy danych, jeśli istnieje. Książka nie może zostać usunięta, jeśli wszystkie kopie nie zostały zwrócone.
- Rent a Book: wypożycza daną książkę dla danego klienta. Użytkownik określa nazwę użytkownika, nazwę książki i rok wydania za pośrednictwem terminala. Klient może wypożyczyć tylko jedną kopię każdej książki. Ta opcja zmniejsza aktualną dostępną liczbę kopii danej książki. Użytkownik nie może wypożyczyć książki, jeśli jej aktualna dostępna liczba kopii wynosi 0.
- Return a Book: zwraca daną książkę, którą dany klient wypożyczył. Użytkownik określa nazwę klienta, nazwę książki i rok wydania za pośrednictwem terminala. Ta opcja zwiększa aktualną dostępną liczbę kopii danej książki.
- Return all Books: zwraca wszystkie książki od danego klienta. Użytkownik określa nazwę użytkownika za pośrednictwem terminala. Ta opcja zwiększa aktualną dostępną liczbę kopii dla wszystkich książek, które klient wypożyczył.
- List of Clients: drukuje atrybuty klasy `Client` dla wszystkich obiektów klasy `Client`.
- List of Books: drukuje atrybuty klasy `Book` dla wszystkich obiektów klasy `Book`.
- Exit: kończy program.
