import time


class Person():
    count = 0

    def __init__(self, name):
        self.name = name
        self.loaned_books = []
        Person.count += 1
        self.id = Person.count

    def loan_book(self, book):
        self.loaned_books.append(book)

    def return_book(self, book):
        if book in self.loaned_books:
            self.loaned_books.remove(book)

    def get_loaned_books_count(self):
        return len(self.loaned_books)

    def __str__(self):
        return f'You have the id: {self.id}. You have loaned {self.get_loaned_books_count()} books.'


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
    def __init__(self, name, books, members):
        self.name = name
        self.books = books
        self.members = members

Eirik = Person("Eirik Evjenth")
Thomas = Person("Thomas Egil Hasselgreen")
JBH = Person("JBH")

members = [Eirik, Thomas, JBH]
books = [Harry_potter, Podcast]

asvg_bibliotek = Bibliotek("ASVG bibliotek", books, members)


for book in asvg_bibliotek.books:
    print(f"{book.title}")



def loan_book(bibliotek, person, book_title):
    for book in bibliotek.books:
        if book.title.lower() == book_title.lower():
            if person.get_loaned_books_count() < 3:
                person.loan_book(book)
                bibliotek.books.remove(book)
                current_time = time.time()
                loan_end_time = current_time + 7 * 24 * 60 * 60

                if loan_end_time > time.time():
                    print(f"{person.name} has loaned: {book.title}")
                    print(f"You have the book available for {round((loan_end_time - time.time())/(3600 * 24))} days")
                else:
                    print("Something went wrong with the loaning process")
                return
            else:
                print(f"{person.name} has already loaned 3 books.")
                return
    print("Book not found in the library")

ambition = input("Do you want to be a member for the ASVG library? y/n: ")
if ambition == "y":
    person_name = input("Enter your full name: ")
    new_member = Person(person_name)
    members.append(new_member)
    book_to_loan = input("Enter the title of the book you want to loan: ")
else:
    print("You have no ambitions, have a good day")
    time.sleep(2)
    exit(1)

for member in asvg_bibliotek.members:
    if member.name.lower() == person_name.lower():
        loan_book(asvg_bibliotek, member, book_to_loan)
        break
else:
    print("Member not found in the library")