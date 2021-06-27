from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView
from .serializers import BookSerializer
from .models import Book

## Generic Views
class BookDetailSerializerView(RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookListSerializerView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer