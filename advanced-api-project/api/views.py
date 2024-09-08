from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .serializers import BookSerializer
from .models import Book
from rest_framework.authentication import TokenAuthentication
from .permissions import IsAuthorOrReadOnly

class BookListView(generics.ListAPIView):
    permissions_classes = [IsAuthenticatedOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.DetailAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookCreateView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permissions_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
class BookUpdateView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permissions_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDeleteView(generics.DeleteAPIView):
    authentication_classes = [TokenAuthentication]
    permissions_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer    
