from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookCreateView, BookDeleteView, BookDetailView, BookListView, BookUpdateView
from rest_framework.authtoken import views

router = DefaultRouter()
router.register(r'book', BookCreateView, BookDeleteView, BookDetailView, BookListView, BookUpdateView)

urlspatterns = [
    path('api/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
    path('/books/', BookListView.as_view(), name='book-list'),
    path('books/create', BookCreateView.as_view(), name='book-create'),
    path('books/delete', BookDeleteView.as_view(), name='book-delete'),
    path('books/details', BookDetailView.as_view(), name='book-detail'),
    path('books/update', BookUpdateView.as_view(), name='book-update')
]