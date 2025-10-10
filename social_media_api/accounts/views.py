from django.contrib.auth import get_user_model
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from .serializers import RegisterSerializer, ProfileSerializer, UserSerializer


User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = User.objects.get(id=token.user_id)
        return Response({'token': token.key, 'username': user.username})

class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'


    def get_object(self):
        return self.request.user

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def follow_user(request, user_id):
    try:
        to_follow = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response({'detail':'User not found'}, status=status.HTTP_404_NOT_FOUND)
    if to_follow == request.user:
        return Response({'detail': "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

    request.user.following.add(to_follow)
    return Response({'detail': f'You are now following {to_follow.username}.'}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unfollow_user(request, user_id):
    try:
        to_unfollow = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response({'detail':'User not found'}, status=status.HTTP_404_NOT_FOUND)

    request.user.following.remove(to_unfollow)
    return Response({'detail': f'You have unfollowed {to_unfollow.username}.'}, status=status.HTTP_200_OK)

# Create your views here.
