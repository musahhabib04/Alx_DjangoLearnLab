from django.contrib import admin
from .models import Author, Book, Library, Librarian, UserProfile


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "library")
    list_filter = ("library", "author")
    search_fields = ("title",)


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "location")
    search_fields = ("name", "location")


@admin.register(Librarian)
class LibrarianAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "library")


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "role")
    list_filter = ("role",)
    search_fields = ("user__username",)
