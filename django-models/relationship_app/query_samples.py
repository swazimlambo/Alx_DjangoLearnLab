from .models import Book, Librarian, Library, Author

def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = author.objects.filter(author=author)

def books_in_library(library_name):
    library_books = Library.objects.get(name=library_name)
    books = books.all()    

def get_librarian(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)