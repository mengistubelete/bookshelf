from django.shortcuts import render
from .models import Book


def index(request):
    books = Book.objects.all().order_by("year")
    return render(request, "books/index.html", {"books": books})


def old(request):
    books = Book.objects.filter(year__lt=2000).order_by("year")
    return render(request, "books/index.html", {"books": books})