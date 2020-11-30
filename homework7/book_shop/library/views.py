from django.shortcuts import render
from .models import Book


# Create your views here.
def index_view(request):
    books = Book.objects.prefetch_related('author','review').all()
    return render(request, 'library/index.html', {'books': books})