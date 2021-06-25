from django.shortcuts import render, redirect
from .models import Book, Author, Library
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.urls import reverse_lazy


# @method_decorator(cache_page(60 * 15), name='dispatch')
class BookListView(ListView):
    model = Book
    template_name = 'books-list.html'
    context_object_name = 'objects'

    ## if you want to follow through relation's uncomment this
    # def get_context_data(self,**kwargs):
    #     context = dict()
    #     context['objects'] = self.model.objects.select_related().all()
    #     return context


# @method_decorator(cache_page(60 * 15), name='dispatch')
class AuthorListView(ListView):
    model = Author
    template_name = 'authors-list.html'
    context_object_name = 'objects'

    def dispatch(self, request, *args, **kwargs):
        if 'clear' in request.GET:
            cache.clear()
            print("in cache")
        print("not in cache")
        return super().dispatch(request, *args, **kwargs)

    # if you want to follow through relation's uncomment this
    # def get_context_data(self,**kwargs):
    #     context = dict()
    #     context['objects'] = self.model.objects.prefetch_related('book_set').all()
    #     return context


class LibraryListView(ListView):
    model = Library
    template_name = 'libraries-list.html'
    context_object_name = 'objects'

def clear_cache(request):
    cache.clear()
    return redirect(reverse_lazy('test_app:cache_authors'))
