from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from django import forms
from .forms import BookSearchForm, BookForm, ExampleForm 


@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})


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


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)

def search_books(request):
    form = SearchForm(request.GET or None)
    books = []
    if form.is_valid():
        query = form.cleaned_data["query"]
        # ORM prevents SQL injection
        books = Book.objects.filter(title__icontains=query)
    return render(request, "bookshelf/book_list.html", {"books": books, "form": form})



# Create your views here.
