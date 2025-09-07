from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.list_books, name="list_books"),
    path("libraries/<int:pk>/", views.library_detail, name="library_detail"),
    path("register/", views.register, name="register"),
    path("login/", LoginView.as_view(), name="login"),       # ✅ fixed
    path("logout/", LogoutView.as_view(), name="logout"),   # ✅ fixed
]

