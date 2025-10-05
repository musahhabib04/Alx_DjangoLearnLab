from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.db.models import Q
from .models import Post


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

def search_posts(request):
    query = request.GET.get('q')
    results = Post.objects.filter(
        Q(title__icontains=query) | 
        Q(content__icontains=query) | 
        Q(tags__name__icontains=query)
    ).distinct()
    return render(request, 'blog/search_results.html', {'posts': results, 'query': query})



# Public listing of posts

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # your template file
    context_object_name = 'posts'
    paginate_by = 10
    ordering = ['-created_at']  # newest first


# Public detail view
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

def get_context_data(self, **kwargs):
        """
        Adds:
        - comments: all comments for the post
        - comment_form: an empty CommentForm to render on the post detail page
        """
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['comments'] = post.comments.all()
        context['comment_form'] = CommentForm()
        return context

# Create new post — authenticated users only
class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView, CreateView):
    model = Post
    form_class = PostForm
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
    form_class = PostForm
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


# ---------- COMMENT VIEWS ----------

class CommentCreateView(LoginRequiredMixin, CreateView):
    """
    Handles POST when a user submits a comment for a specific post.
    URL should include post_id; after saving, redirect back to the post detail.
    """
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'  # in practice we're posting from post_detail; this is fallback
    login_url = 'login'

    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        form.instance.author = self.request.user
        form.instance.post = post
        return super().form_valid(form)

    def get_success_url(self):
        # Redirect to the post detail after creating a comment
        return reverse_lazy('post-detail', args=[self.object.post.pk])


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'
    login_url = 'login'

    def test_func(self):
        comment = self.get_object()
        return comment.author == self.request.user

    def get_success_url(self):
        return reverse_lazy('post-detail', args=[self.object.post.pk])


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'
    login_url = 'login'

    def test_func(self):
        comment = self.get_object()
        return comment.author == self.request.user

    def get_success_url(self):
        return reverse_lazy('post-detail', args=[self.object.post.pk])
# Create your views here.
