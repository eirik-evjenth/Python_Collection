class Book():
    def __init__(self, title, genre, author, publication):
        self.name = title
        self.title = title
        self.genre = genre
        self.author = author
        self.publication = publication

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
    if isinstance(book, Physical):
        print(f"ISBN: {book.ISBN}")
    elif isinstance(book, Digital):
        print(f"Audiobook: {book.audiobook}")
        print(f"Written: {book.written}")
    else:
        print("That is not a valid book")


print_book_info(Podcast)