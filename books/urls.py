from django.urls import path,re_path
from . import views

app_name='books'
urlpatterns=[
	# re_path(r'^login/', views.login),
	# re_path(r'^register/', views.register, name='register'),
	re_path(r'^$',views.register, name='register'),
	re_path(r'^login$',views.checkLogin, name='checkLogin'),
	re_path(r'^reg$',views.checkRegister, name='checkRegister'),
	re_path(r'^home/', views.home, name='home'),
	re_path(r'^author/([0-9]+)/', views.AuthorView, name='AuthorView'),
	re_path(r'^authors/', views.authors.as_view(), name='authors'),
	re_path(r'^book/([0-9]+)/', views.BookView, name='BookView'),
	re_path(r'^books/', views.books.as_view(), name='books'),
	re_path(r'^category/(?P<id>[0-9]+/)', views.CategoryView, name='CategoryView'),
	re_path(r'^categories/', views.CategoryList.as_view(), name='CategoryList'),

]