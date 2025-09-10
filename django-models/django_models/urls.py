from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import admin
from django.urls import path
from relationship_app import views

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", views.home, name="home"),
    path("books/", views.list_books, name="list_books"),
    path("libraries/", views.library_list, name="library_list"),
    path("libraries/<int:pk>/", views.library_detail, name="library_detail"),

    path("register/", views.register, name="register"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", views.CustomLogoutView.as_view(), name="logout"),

    path("admin-view/", views.admin_view, name="admin_view"),
    path("librarian-view/", views.librarian_view, name="librarian_view"),
    path("member-view/", views.member_view, name="member_view"),
]

