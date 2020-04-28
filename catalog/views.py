from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre

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