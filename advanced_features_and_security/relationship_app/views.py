from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView


# Homepage redirect
def home(request):
    return redirect("login")  # or wherever you want to land after home


# Registration view
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})


# Login view
class CustomLoginView(LoginView):
    template_name = "relationship_app/login.html"


# Logout view
class CustomLogoutView(LogoutView):
    template_name = "relationship_app/logout.html"
