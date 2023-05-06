# posts/views.py
from django.shortcuts import render
from rest_framework import generics

from .models import Post
from .serializers import PostSerializers
from .permissions import IsAuthorOrReadOnly
# Create your views here.

class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,) 
    queryset = Post.objects.all()
    serializer_class = PostSerializers


class PostDetail(generics.RetrieveDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    # permission_classes = (permissions.IsAdminUser,) #new
    queryset = Post.objects.all()
    serializer_class = PostSerializers