class Book():
    def __init__(self, title, physical, digital, written, audiobook, author, ISBN, publication):
        self.name = title
        self.physical = physical
        self.digital = digital
        self.written = written
        self.audiobook = audiobook
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.publication = publication

Harry_potter = Book("Harry Potter", False, True, False, True, "J.K Rowling", 9788869183157, "26.6.1997")
available_books = []
attributes = ["physical", "digital", "written", "audiobook"]

for attr in attributes:
    if getattr(Harry_potter, attr):
        available_books.append(attr)

available_books_str = ", ".join(available_books)
print(f"{Harry_potter.name} has the following books available: {available_books_str}.")


'''
if Harry_potter.physical:
    print(f"{Harry_potter.name} is a physical book.")
else:
    print(f"{Harry_potter.name} is a digital book.")
'''
