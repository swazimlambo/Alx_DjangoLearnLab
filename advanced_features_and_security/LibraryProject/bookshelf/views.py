from django.contrib.auth.decorators import permission_required
from .models import Book
from django.shortcuts import render

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    book = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': book})
