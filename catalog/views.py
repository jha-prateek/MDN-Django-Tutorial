from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre
from django.views import generic

# Create your views here.
def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    num_authors = Author.objects.count()

    context = {
        'numBooks': num_books,
        'numInstaces': num_instances,
        'numAvailable': num_instances_available,
        'numAuthors': num_authors
    }

    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    queryset = Book.objects.all()


class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    queryset = Author.objects.all()

class AuthorDetailView(generic.DetailView):
    model = Author