from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .serializers import BookSerializer, AuthorSerializer
from .models import Book, Author
from rest_framework.authentication import TokenAuthentication
from django_filters import rest_framework as filter
from rest_framework.filters import SearchFilter, OrderingFilter

class BookListView(generics.ListAPIView):
    permissions_classes = [IsAuthenticatedOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filter.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name', 'author', 'publication_year']
    search_fields = ['title', 'author_name']
    ordering_fields = ['title', 'publication_year']

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

class BookDeleteView(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permissions_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer    
