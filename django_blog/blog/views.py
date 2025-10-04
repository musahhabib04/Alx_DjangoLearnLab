from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm


def home(request):
    return render(request, 'blog/home.html')

def post_create(request):
    # placeholder view
    return render(request, 'blog/post_form.html')

def post_update(request, pk):
    # placeholder view
    return render(request, 'blog/post_form.html')

def post_delete(request, pk):
    # placeholder view
    return render(request, 'blog/post_confirm_delete.html')



# blog/views.py
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

# Public listing of posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # your template file
    context_object_name = 'posts'
    ordering = ['-created_at']  # newest first


# Public detail view
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


# Create new post — authenticated users only
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = RegisterForm
    template_name = 'blog/post_form.html'
    # where to redirect on success - detail view of created post
    # we'll use get_absolute_url on model if present, or override get_success_url
    login_url = 'login'

    def form_valid(self, form):
        # set the author to the currently logged-in user
        form.instance.author = self.request.user
        return super().form_valid(form)


# Update post — only the author can edit
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = RegisterForm
    template_name = 'blog/post_form.html'
    login_url = 'login'

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user


# Delete post — only the author can delete
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')
    login_url = 'login'

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user

# Create your views here.
