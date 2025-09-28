from django import forms
from .models import Book

# Example form required by the checker
class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your Name")
    email = forms.EmailField(label="Your Email")

# Form for searching books
class BookSearchForm(forms.Form):
    query = forms.CharField(label="Search Books", max_length=100, required=False)

# ModelForm for Book
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "published_date"]
