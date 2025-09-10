from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# -------------------------------------------------------------------
# ROLE CHOICES (Global)
# -------------------------------------------------------------------
ROLE_CHOICES = [
    ("Admin", "Admin"),
    ("Librarian", "Librarian"),
    ("Member", "Member"),
]

# -------------------------------------------------------------------
# Core Models
# -------------------------------------------------------------------
class Author(models.Model):
    """Represents a book author."""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Library(models.Model):
    """Represents a library branch or location."""
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    """Represents a book stored in a library."""
    title = models.CharField(max_length=200)
    published_date = models.DateField(null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    library = models.ForeignKey(
        Library,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="books"
    )

    def __str__(self):
        return self.title


class Librarian(models.Model):
    """Represents a librarian responsible for one library."""
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# -------------------------------------------------------------------
# User Profile Model (Extends Django User)
# -------------------------------------------------------------------
class UserProfile(models.Model):
    """Extends the default User model with a role and custom permissions."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="Member"
    )

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]

    def __str__(self):
        return f"{self.user.username} ({self.role})"

# -------------------------------------------------------------------
# Signals to Auto-Create & Save User Profiles
# -------------------------------------------------------------------
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
