from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Author(models.Model):
    """Model representing an author."""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Library(models.Model):
    """Model representing a library."""
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255, null=True, blank=True)


    def __str__(self):
        return self.name


class Book(models.Model):
    """Model representing a book."""
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    library = models.ForeignKey(Library, on_delete=models.CASCADE, related_name="books", null=True, blank=True)


    def __str__(self):
        return self.title


class Librarian(models.Model):
    """Model representing a librarian."""
    name = models.CharField(max_length=100)
    library = models.OneToOneField(
        Library, on_delete=models.CASCADE, related_name="librarian"
    )

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    """Extended user profile with roles and custom permissions."""
    ROLE_CHOICES = [
        ("Admin", "Admin"),
        ("Librarian", "Librarian"),
        ("Member", "Member"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="Member")

    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_edit_book", "Can edit book"),
            ("can_delete_book", "Can delete book"),
        ]
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

    def __str__(self):
        return f"{self.user.username} - {self.role}"
