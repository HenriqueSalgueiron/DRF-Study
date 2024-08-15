# v2: Using ViewSets
from rest_framework import viewsets
from django.contrib.auth.models import User
from accounts.serializers import UserSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet): #provides 'list and 'retrieve'
  queryset = User.objects.all()
  serializer_class = UserSerializer



## V1: Using View class ##

# from django.contrib.auth.models import User
# from accounts.serializers import UserSerializer
# from rest_framework import generics

# class UserView(generics.ListAPIView):
#   queryset = User.objects.all()
#   serializer_class = UserSerializer

# class UserDetailsView(generics.RetrieveAPIView):
#   queryset = User.objects.all()
#   serializer_class = UserSerializer