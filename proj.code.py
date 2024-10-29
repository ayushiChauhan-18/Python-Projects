import tkinter as tk
from tkinter import messagebox

class Book:
    def _init_(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.available = True  

    def display_details(self):
        return f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}, Available: {'Yes' if self.available else 'No'}"

class LibraryCatalog:
    def _init_(self):
        self.books = []

    def add_book(self, title, author, genre):
        book = Book(title, author, genre)
        self.books.append(book)

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def borrow_book(self, title):
        book = self.search_book(title)
        if book and book.available:
            book.available = False
            return True
        return False

    def return_book(self, title):
        book = self.search_book(title)
        if book and not book.available:
            book.available = True
            return True
        return False

    def display_available_books(self):
        return [book.display_details() for book in self.books if book.available]

class LibraryApp:
    def _init_(self, root):
        self.library = LibraryCatalog()
        self.root = root
        self.root.title("Library Catalog System")

        self.title_label = tk.Label(root, text="Title:")
        self.title_label.pack()
        self.title_entry = tk.Entry(root)
        self.title_entry.pack()

        self.author_label = tk.Label(root, text="Author:")
        self.author_label.pack()
        self.author_entry = tk.Entry(root)
        self.author_entry.pack()

        self.genre_label = tk.Label(root, text="Genre:")
        self.genre_label.pack()
        self.genre_entry = tk.Entry(root)
        self.genre_entry.pack()

        self.add_button = tk.Button(root, text="Add Book", command=self.add_book)
        self.add_button.pack()
        
        self.borrow_button = tk.Button(root, text="Borrow Book", command=self.borrow_book)
        self.borrow_button.pack()
        
        self.return_button = tk.Button(root, text="Return Book", command=self.return_book)
        self.return_button.pack()
        
        self.display_button = tk.Button(root, text="Display Available Books", command=self.display_books)
        self.display_button.pack()

        self.result_label = tk.Label(root, text="", fg="blue")
        self.result_label.pack()

    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        genre = self.genre_entry.get()
        
        if title and author and genre:
            self.library.add_book(title, author, genre)
            self.result_label.config(text=f"Book '{title}' added.")
        else:
            messagebox.showwarning("Warning", "Please enter title, author, and genre.")

    def borrow_book(self):
        title = self.title_entry.get()
        
        if title:
            if self.library.borrow_book(title):
                self.result_label.config(text=f"You have borrowed '{title}'.")
            else:
                self.result_label.config(text=f"'{title}' is not available.")
        else:
            messagebox.showwarning("Warning", "Please enter the title of the book to borrow.")

    def return_book(self):
        title = self.title_entry.get()
        
        if title:
            if self.library.return_book(title):
                self.result_label.config(text=f"'{title}' returned successfully.")
            else:
                self.result_label.config(text=f"'{title}' not found or already available.")
        else:
            messagebox.showwarning("Warning", "Please enter the title of the book to return.")

    def display_books(self):
        available_books = self.library.display_available_books()
        
        if available_books:
            books_text = "\n".join(available_books)
            self.result_label.config(text=books_text)
        else:
            self.result_label.config(text="No books available.")

if __name__ == "_main_":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()
