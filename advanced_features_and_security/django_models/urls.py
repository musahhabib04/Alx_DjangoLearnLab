from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),              # Homepage
    path("login/", LoginView.as_view(), name="login"),   # Login
    path("logout/", LogoutView.as_view(), name="logout"), # Logout
]
