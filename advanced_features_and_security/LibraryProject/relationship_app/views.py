from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from .models import Book, Library
from django.shortcuts import render, get_object_or_404
from .models import Library


# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


# Class-based view for library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"


# Registration view
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("list_books")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})


# Login view
class CustomLoginView(LoginView):
    template_name = "relationship_app/login.html"


# Logout view
class CustomLogoutView(LogoutView):
    template_name = "relationship_app/logout.html"


# Homepage redirect to book list
def home(request):
    return redirect("list_books")


def library_detail(request, pk):
    library = get_object_or_404(Library, pk=pk)
    return render(request, "relationship_app/library_detail.html", {"library": library})


def library_list(request):
    libraries = Library.objects.all()
    return render(request, "relationship_app/library_list.html", {"libraries": libraries})


from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# Role check helpers
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'


# Views
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")


@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")


@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")


# LibraryProject/relationship_app/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required('relationship_app.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/book_list.html', {'books': books})

@permission_required('relationship_app.can_create', raise_exception=True)
def book_create(request):
    # Example: create a new book (you can replace with a proper form)
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        Book.objects.create(title=title, author=author)
        return redirect("book_list")
    return render(request, "relationship_app/book_form.html")

@permission_required('relationship_app.can_edit', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.save()
        return redirect("book_list")
    return render(request, "relationship_app/book_form.html", {"book": book})

@permission_required('relationship_app.can_delete', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect("book_list")


