from django.urls import path
from .views import AuthorListView, BookListView, LibraryListView
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

app_name = 'test_app'
urlpatterns = [
    path('cache/authors/', cache_page(60)(AuthorListView.as_view()), name='cache_authors'),
    path('cache/libs/', cache_page(60*5)(LibraryListView.as_view()), name='cache_libs'),
    path('cache/books/', cache_page(60*5)(BookListView.as_view()), name='cache_books'),
    
    
    path('authors/', AuthorListView.as_view(), name='authors'),
    path('libs/', LibraryListView.as_view(), name='libs'),
    path('books/', BookListView.as_view(), name='books'),
]