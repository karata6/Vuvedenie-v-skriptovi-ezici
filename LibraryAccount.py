class LibraryAccount:
    def __init__(self, name):
        self.name = name
        self.books = []

    def borrow_book(self, book_name):
        self.books.append(book_name)
        print(f"Knigata '{book_name}' e zaeta uspeshno")

    def return_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print(f"Knigata '{book_name}' e vurnata")
        else:
            print("Error: Tazi kniga ne zaemana")

    def list_books(self):
        if len(self.books) == 0:
            print("Nqma zaeti knigi")
        else:
            print("Zaeti knigi")
            for book in self.books:
                print("-", book)


account = LibraryAccount("Ivan")

account.borrow_book("Pod igoto")
account.borrow_book("Baj Ganio")
account.list_books()

account.return_book("Pod igoto")
account.return_book("Harry Potter")
account.list_books()