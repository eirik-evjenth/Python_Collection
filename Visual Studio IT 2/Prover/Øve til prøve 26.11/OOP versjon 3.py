import time


class Book:
    book_count = 0

    def __init__(self, title, genre, author, publication):
        self.title = title
        self.genre = genre
        self.author = author
        self.publication = publication

        Book.book_count += 1
        self.utgave = Book.book_count
        self.book_number = self.utgave

    def __str__(self):
        return 'This book has this number ' + str(self.book.number) + '.'


class Physical(Book):
    def __init__(self, title, genre, author, publication, ISBN):
        super().__init__(title, genre, author, publication)
        self.ISBN = ISBN


class Digital(Book):
    def __init__(self, title, genre, author, audiobook, written, publication):
        super().__init__(title, genre, author, publication)
        self.audiobook = audiobook
        self.written = written



Harry_potter = Physical("Harry Potter", "Fantasy", "J.K Rowling", "26.11.1997", 9788869183157)
Podcast = Digital("How to find happiness", "Self-help", "Eirik Ejenth", True, False, "26.11.2024")

def print_book_info(book):
    print(f"Title: {book.title}")
    print(f"Genre: {book.genre}")
    print(f"Author: {book.author}")
    print(f"Publication Date: {book.publication}")
    print(f"Utgave: {book.utgave}")
    if isinstance(book, Physical):
        print(f"ISBN: {book.ISBN}")
    elif isinstance(book, Digital):
        print(f"Audiobook: {book.audiobook}")
        print(f"Written: {book.written}")
    else:
        print("That is not a valid book")

class Bibliotek():
    def __init__(self, name, books):
        self.name = name
        self.books = books


books = [Harry_potter, Podcast]

asvg_bibliotek = Bibliotek("ASVG bibliotek", books)


def loan_book(bibliotek, book_title):
    for book in bibliotek.books:
        if book.title == book_title:
            current_time = time.time()
            loan_end_time = current_time + 7 * 24 * 60 * 60

            if loan_end_time > time.time():
                print(f"Du har boken tilgjengelig for {round((loan_end_time - time.time())/(3600 * 24))} dager")
            else:
                print("Noe gikk gale med utlånet")
            return
    print("Book not found in the library")

for book in asvg_bibliotek.books:
    print(f"{book.title}")
book_to_loan = input("Enter the title of the book you want to loan: ")
loan_book(asvg_bibliotek, book_to_loan)