from .models import Book, Author, Category
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    cat = serializers.StringRelatedField()
    class Meta:
        model = Book
        fields = ['author', 'cat', 'name', 'title', 'published_date']

