import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_models.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
author = Author.objects.get(name="Chinua Achebe")
books_by_author = Book.objects.filter(author=author)
print("Books by Chinua Achebe:", [book.title for book in books_by_author])

# 2. List all books in a library
library = Library.objects.get(name="Accra Central Library")
books_in_library = library.books.all()
print("Books in Accra Central Library:", [book.title for book in books_in_library])

# 3. Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print("Librarian for Accra Central Library:", librarian.name)
