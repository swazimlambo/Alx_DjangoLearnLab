from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Book, Author
from django.contrib.auth.models import User

class BookAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.author = Author.objects.create(name='Author 1')
        self.book = Book.objects.create(title='Book 1', publication_year=2020, author=self.author)

    def test_list_books(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check if the response data contains the correct book title
        self.assertEqual(response.data[0]['title'], 'Book 1')
        self.assertEqual(response.data[0]['publication_year'], 2020)

    def test_create_book(self):
        url = reverse('book-list')
        self.client.login(username='testuser', password='password')
        data = {'title': 'New Book', 'publication_year': 2021, 'author': self.author.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Check if the created book is in the response data
        self.assertEqual(response.data['title'], 'New Book')
        self.assertEqual(response.data['publication_year'], 2021)

    def test_update_book(self):
        url = reverse('book-detail', args=[self.book.id])
        self.client.login(username='testuser', password='password')
        data = {'title': 'Updated Title', 'publication_year': 2020, 'author': self.author.id}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Verify the response data reflects the update
        self.assertEqual(response.data['title'], 'Updated Title')

    def test_delete_book(self):
        url = reverse('book-detail', args=[self.book.id])
        self.client.login(username='testuser', password='password')
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Verify the book is no longer in the database
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books(self):
        url = reverse('book-list') + '?title=Book 1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check that the filtered response contains the correct book
        self.assertEqual(response.data[0]['title'], 'Book 1')

    def test_search_books(self):
        url = reverse('book-list') + '?search=Book'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check that the search results contain the book
        self.assertEqual(response.data[0]['title'], 'Book 1')

    def test_order_books(self):
        url = reverse('book-list') + '?ordering=publication_year'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check that the response data is ordered by publication_year
        self.assertEqual(response.data[0]['publication_year'], 2020)