import numpy as np
import csv
from Books import Book
from Clients import Client
def find_clients(tab, text): # None means that its not in database
    for i in tab:
        if i.get_name() == text:
            return i
    return None
def find_books(tab, text, text2):
    for i in tab:
        if i.get_name() == text and i.get_year() == text2:
            return i
    return None
def save_clients_to_file(file_path, objects_list):
    try:
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Client Name", "Rented Books"])
            for obj in objects_list:
                writer.writerow([obj.get_name()] + [f"{book.get_name()},{book.get_year()}" for book in obj.get_rented_books()])
    except Exception as e:
        print(f"Error while saving objects to {file_path}: {e}")

def save_books_to_file(file_path, objects_list):
    try:
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Book Name", "Year", "Current Available", "Overall number of copies"])
            for obj in objects_list:
                writer.writerow([obj.get_name(), obj.get_year(), obj.get_numbers(), obj.get_max_numbers()])
    except Exception as e:
        print(f"Error while saving objects to {file_path}: {e}")

def read_from_books(file_path):
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                name, year, number, max_number = row
                year = int(year)
                number = int(number)
                max_number = int(max_number)
                Book(name, year, number, max_number)
    except Exception as e:
        print(f"Error while reading data from {file_path}: {e}")

def read_from_clients(file_path, books):
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                name, *rented_books = row
                client = Client(name)
                for book_data in rented_books:
                    book_name, book_year = book_data.split(',')
                    book = find_books(books, book_name, to_int(book_year))
                    client.add_rented_book(book)
    except Exception as e:
        print(f"Error while reading data from {file_path}: {e}")
        return []
def to_int(value):
    result=None
    try:
        result = int(value)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
    return result
def print_lists(file_path):
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
            print(file_content)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
