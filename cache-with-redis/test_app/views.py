from django.shortcuts import render
from .models import Book, Author, Library
from django.views.generic import ListView

class BookListView(ListView):
    model = Book
    template_name = 'home.html'
    context_object_name = 'objects'


class AuthorListView(ListView):
    model = Author
    template_name = 'home.html'
    context_object_name = 'objects'


class LibraryListView(ListView):
    model = Library
    template_name = 'home.html'
    context_object_name = 'objects'
