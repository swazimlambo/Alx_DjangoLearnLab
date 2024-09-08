from rest_framework import serializers
from datetime import timezones
from .models import Book, Author

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year','author']

    def validation_publication_year(self, date):
        if date > timezones.now().year:
            raise serializers.ValidationError('The publication year can not be a future date')
        

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']


