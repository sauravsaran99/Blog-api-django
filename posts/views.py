# posts/views.py
# Code Before ViewSet
# from django.contrib.auth import get_user_model # new
# from django.shortcuts import render
# from rest_framework import generics

# from .models import Post
# from .serializers import PostSerializers, UserSerializer
# from .permissions import IsAuthorOrReadOnly
# # Create your views here.

# class PostList(generics.ListCreateAPIView):
#     permission_classes = (IsAuthorOrReadOnly,) 
#     queryset = Post.objects.all()
#     serializer_class = PostSerializers


# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthorOrReadOnly,)
#     # permission_classes = (permissions.IsAdminUser,) #new
#     queryset = Post.objects.all()
#     serializer_class = PostSerializers

# class UserList(generics.ListCreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer

# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer

# Code after ViewSet

from django.contrib.auth import get_user_model # new
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser # new

from .models import Post
from .serializers import PostSerializers, UserSerializer
from .permissions import IsAuthorOrReadOnly
# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializers

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser] # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer   
