from django.shortcuts import render

# Create your views here.

def author(request):
    return render(request, 'author.html')

def book(request):
    return render(request, 'book.html')