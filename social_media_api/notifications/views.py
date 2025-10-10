from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Notification
from .serializers import NotificationSerializer
from rest_framework.response import Response
from rest_framework.views import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

class NotificationListAPIView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user).order_by('read', '-created_at')

class MarkNotificationReadAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk, format=None):
        notification = get_object_or_404(Notification, pk=pk, recipient=request.user)
        notification.read = True
        notification.save()
        return Response({'detail': 'Marked as read'}, status=status.HTTP_200_OK)

# Create your views here.
