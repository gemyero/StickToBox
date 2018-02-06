from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as authlogin, logout as authlogout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from django.views import generic
from django.db.models import Q
from .models import Book, Author, Category
from django.views.generic import ListView, DetailView
from .forms import RegistrationForm, LoginForm

# Create your views here.

def author(request):
    return render(request, 'author.html')

def book(request):
    return render(request, 'book.html')

# def login (request):

# 	pass


def register (request):
	regForm = RegistrationForm()
	logForm = LoginForm()
	return render(request,'books/index.html',{'rform':regForm, 'lform':logForm})

# @login_required()
# def home (request):
# 	pass


# def author (request):
# 	pass


class authors(ListView):
	model = Author		
				


# def book (request):
# 	pass


class books(ListView):
	model = Book


# def category (request):
# 	pass


class categories(ListView):
	model = Category

