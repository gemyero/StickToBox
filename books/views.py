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
from django.template import Context, Template
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


def checkLogin (request):
    form = LoginForm(request.POST)
    if request.method == 'POST' :
        uname = request.POST.get('username')
        passwd = request.POST.get('password')
        user = authenticate(username=uname,password=passwd)
        if user is not None:
            authlogin(request,user)
            return render(request,"books/index.html")
        else :
            regForm = RegistrationForm()
            return render(request,'books/index.html',{'rform':regForm, 'lform':form, 'error':'Either Usernme or Password is not correct'})
    else:
        return redirect('books:register')

def checkRegister(request):
    form = RegistrationForm(request.POST, request.FILES)
    logForm = LoginForm()
    username = request.POST.get('username')
    existUsr = User.objects.filter(username=username).exists()
    if not existUsr:
        if form.is_valid():
            profile = Profile()
            usr = User(request.POST, request.FILES['img'])
            prof = Profile(request.FILES['img'])
            email = request.POST.get('email')
            password = request.POST.get('password')
            repass = request.POST.get('repass')
            if password != repass:
                return render(request,'books/index.html',{'rform':form, 'lform':logForm, 'pass_err':'Password does not match'})
            else :
                newUser=User.objects.create_user(username=username,email=email,password=password)
                profile.user=newUser
                profile.profile_picture=form.cleaned_data['img']
                profile.save()
                return render(request,"books/home.html")
        else:
            return render(request,'books/index.html',{'rform':form, 'lform':logForm})
    else : 
        return render(request,'books/index.html',{'rform':form, 'lform':logForm, 'user_errors':'this user name already exists'})
        # return redirect('books:register')

def register(request):
    regForm = RegistrationForm()
    logForm = LoginForm()
    category_list = Category.objects.all()
    book_list = Book.objects.all()
    return render(request, 'books/index.html',
        {'rform': RegistrationForm, 'lform': LoginForm,
        'category_list': category_list, 'book_list': book_list})

# @login_required(login_url='books:register')
@login_required(login_url='books:register')
def home (request):
    # if User.is_authenticated:
        # user_image = User.Profile_set.filter(username='a7mad').profile_picture
    category_list = Category.objects.all()
    book_list = Book.objects.all()
    return render(request, 'books/home.html',
        {'category_list': category_list, 'book_list': book_list})

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


def service2(request, id):
    if request.user.is_authenticated :
        myBook=get_object_or_404(Book,id = id)
        rate = request.GET.get('rate')
        profilebook = ProfileBook.objects.filter(profile=request.user.profile, book=myBook)
        if bool(profilebook):
            profilebook.update(rate=rate)
        else:
            ProfileBook.objects.create(profile=request.user.profile, book=myBook, rate=rate)
        return JsonResponse("success",safe=False)
    else:
        return redirect('books:register')

def service3(request):
    status = ProfileBook.STATUS
    return JsonResponse(status,safe=False)

@login_required(redirect_field_name='returnURL', login_url='books:register')
def Status(request, id):
    myBook=get_object_or_404(Book, id = id)
    profilebook = ProfileBook.objects.filter(profile=request.user.profile, book=myBook)
    curstatus = profilebook[0].status
    return JsonResponse(curstatus,safe=False)

# @login_required(redirect_field_name='returnURL', login_url='books:register')
def service4(request, Id):
    if request.user.is_authenticated :
        myBook=get_object_or_404(Book,id = Id)
        stat = request.GET.get('status')
        profilebook = ProfileBook.objects.filter(profile=request.user.profile, book=myBook)
        if bool(profilebook):
            profilebook.update(status=stat)
        else:
            ProfileBook.objects.create(profile=request.user.profile, book=myBook, status=stat)
        return JsonResponse("success",safe=False)
    else:
        return redirect('books:register')


def search(request):
    return render(request, 'books/search.html')

def searchService(request, keyword):
    book_results = Book.objects.filter(title__iexact=keyword.strip()).values()
    author_results = Author.objects.filter(first_name__iexact=keyword.strip()).values()
    category_results = Category.objects.filter(name__iexact=keyword.strip()).values()

    return JsonResponse({'results': [list(author_results), list(book_results), list(category_results)]})

def service5(request, status):
    d = eval(status)
    myProfile = get_object_or_404(Profile, id=request.user.profile.id)
    myCategory = get_object_or_404(Category, id=int(d['c_id']))

    if ProfileCategory.objects.filter(profile=myProfile, category=myCategory):
        ProfileCategory.objects.filter(profile=myProfile, category=myCategory).update(fav=(1 if d['fav'] == 'true' else 0))
    else:
        ProfileCategory.objects.create(profile=myProfile, category=myCategory, fav=(1 if d['fav'] == 'true' else 0))
    
    return JsonResponse(status, safe=False)