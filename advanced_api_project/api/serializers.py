from rest_framework import serializers
from .models import Book, Book
from .models import Author

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title','author', 'publication_year']

class BookSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ['title', 'author','books', 'publication_year']

        def validate(self, data):
            if len(data['publication_year']) > 2024/09/08:
                raise serializers.ValidationError ("Publication year must not be from the future.")
            return data
            

class AuthorSerializer(serializers.ModelSerializers):
    class Meta:
        model = Author 
        fields = ['name']


