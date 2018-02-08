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

# Create your views here.
class authors(ListView):
	model = Author		

class books(ListView):
	model = Book

class CategoryList(ListView):
    model = Category

class AuthorView(DetailView):
    model = Author

class BookView(DetailView):
    model = Book

class CategoryView(DetailView):
    model = Category

def checkLogin (request):
	if request.method == 'POST':
		uname = request.POST.get('username')
		passwd = request.POST.get('password')
		user = authenticate(username=uname,password=passwd)
		if user is not None:
			authlogin(request,user)
			return redirect('books:home')
		else :
			return redirect('books:register')

def checkRegister(request):
	form = RegistrationForm(request.POST, request.FILES)
	if form.is_valid():
		
		usr = User(request.POST, request.FILES['img'])
		prof = Profile(request.FILES['img'])
		username = request.POST.get('username')
		# user=User.objects.filter(username=username).exists()
		email = request.POST.get('email')
		password = request.POST.get('password')
		img = request.FILES.get('img')
		# img.upload_to='images/users/'
		# usr.save()
		newUser=User.objects.create_user(username=username,email=email,password=password)
		Profile.objects.filter(user=newUser).update(profile_picture=img)
		return render(request,"books/home.html")
	else: 
		return redirect('books:register')
def register (request):
	regForm = RegistrationForm()
	logForm = LoginForm()
	return render(request,'books/index.html',{'rform':regForm, 'lform':logForm})

# @login_required()
def home (request):
	return render(request,"books/home.html")

def logout(request):
    authlogout(request)
    return redirect('library:login')