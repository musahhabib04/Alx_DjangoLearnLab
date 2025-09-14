from django import forms
from .models import Book


class BookSearchForm(forms.Form):
    query = forms.CharField(
        label="Search Books",
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Enter title or author'})
    )


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']
