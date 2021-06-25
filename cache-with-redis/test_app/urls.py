from django.urls import path
from .views import AuthorListView, BookListView, LibraryListView

urlpatterns = [
    path('authors/', AuthorListView.as_view()),
    path('libraries/', LibraryListView.as_view()),
    path('books/', BookListView.as_view()),
]