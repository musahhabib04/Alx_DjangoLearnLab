from django.urls import path
from .views import RegisterView, CustomAuthToken, ProfileView, follow_user, unfollow_user

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('follow/<int:user_id>/', follow_user, name='follow-user'),
    path('unfollow/<int:user_id>/', unfollow_user, name='unfollow-user'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile-detail'),
]
