from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as authlogin, logout as authlogout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from django.views import generic
from django.db.models import Q
from .models import *
from django.views.generic import ListView, DetailView
from .forms import RegistrationForm, LoginForm
import math

# Create your views here.

class AuthorView(DetailView):
    model = Author

class AuthorList(ListView):
    model = Author

class BookView(DetailView):
    model = Book

class BookList(ListView):
    model = Book

class CategoryList(ListView):
    model = Category

class CategoryView(DetailView):
    model = Category


def checkLogin(request):
	if request.method == 'POST':
		uname = request.POST.get('username')
		passwd = request.POST.get('password')
		user = authenticate(username=uname,password=passwd)
		if user is not None:
			authlogin(request, user)
			return render(request,"books/home.html")
		else:
			return redirect('books:home')

def checkRegister(request):
	form = RegistrationForm(request.POST, request.FILES)
	if form.is_valid():
		profile = Profile()
		usr = User(request.POST, request.FILES['img'])
		prof = Profile(request.FILES['img'])
        # Check duplicate key
		username = request.POST.get('username')
		email = request.POST.get('email')
		password = request.POST.get('password')
		newUser=User.objects.create_user(username=username,email=email,password=password)
		profile.user=newUser
		profile.profile_picture=form.cleaned_data['img']
		profile.save()
		return render(request,"books/home.html")
	else: 
		return redirect('books:register')

def register (request):
	regForm = RegistrationForm()
	logForm = LoginForm()
	return render(request,'books/index.html', {'rform':regForm, 'lform':logForm})

# @login_required(login_url='books:register')
# @login_required(login_url='')
def home (request):
	return render(request, 'books/index.html', {'rform': RegistrationForm, 'lform': LoginForm})

# def logout(request):
#     authlogout(request)
#     return redirect('books:register')


def service1(request, id):
    book = get_object_or_404(Book, id=id)
    rateSum = 0
    counter = 0

    for item in book.profilebook_set.all():
        rateSum += item.rate
        counter += 1

    rateAverage = math.ceil(rateSum / counter)    
    return JsonResponse(rateAverage, safe=False)
