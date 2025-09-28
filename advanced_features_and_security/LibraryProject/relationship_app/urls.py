from django.contrib import admin
from django.urls import path
from relationship_app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Homepage
    path('', views.home, name='home'),

    # Books
    path('books/', views.list_books, name='list_books'),
    path('books/add/', views.add_book, name='add_book'),
    path('books/edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('books/delete/<int:book_id>/', views.delete_book, name='delete_book'),

    # Libraries
    path('libraries/', views.library_list, name='library_list'),
    path('libraries/<int:pk>/', views.library_detail, name='library_detail'),

    # Authentication
    path('register/', views.register, name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),

    # Role-based views
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),
]
