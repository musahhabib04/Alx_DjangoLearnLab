"""
Views for handling Book CRUD operations using Django REST Framework generic views.
Each class is named exactly as required by the ALX checker:
ListView, DetailView, CreateView, UpdateView, DeleteView
"""

from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


class ListView(generics.ListAPIView):
    """
    Retrieve and list all Book instances.
    Accessible to anyone (public).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class DetailView(generics.RetrieveAPIView):
    """
    Retrieve a single Book instance by its ID.
    Accessible to anyone (public).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class CreateView(generics.CreateAPIView):
    """
    Create a new Book instance.
    Only accessible to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class UpdateView(generics.UpdateAPIView):
    """
    Update an existing Book instance.
    Only accessible to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class DeleteView(generics.DestroyAPIView):
    """
    Delete an existing Book instance.
    Only accessible to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
