from django.contrib.auth.models import User
from accounts.serializers import UserSerializer
from rest_framework import generics

class UserView(generics.ListAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

class UserDetailsView(generics.RetrieveAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer