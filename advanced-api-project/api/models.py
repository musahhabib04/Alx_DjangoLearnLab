from django.db import models


class Author(models.Model):
    """
    Author model:
    Stores information about book authors.
    One author can have multiple books.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model:
    Stores information about individual books.
    Each book is linked to an Author (one-to-many relationship).
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"

# Create your models here.
