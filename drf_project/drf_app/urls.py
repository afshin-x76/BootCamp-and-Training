from django.urls import path
from .views import BookDetailSerializerView, BookListSerializerView


urlpatterns = [
    path('books-list/', BookListSerializerView.as_view(), name='books_list'),
    path('books-detail/<int:pk>/', BookDetailSerializerView.as_view(), name='books_detail'),
]