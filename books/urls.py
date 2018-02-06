from django.urls import path,re_path
from . import views

app_name='books'
urlpatterns=[
	# re_path(r'^login/', views.login),
	re_path(r'^register/', views.register),
	# re_path(r'^$',views.home),
	# re_path(r'^home/', views.home),
	re_path(r'^author/([0-9]+)/', views.author, name='author'),
	re_path(r'^authors/', views.authors.as_view(), name='authors'),
	re_path(r'^book/([0-9]+)/', views.book, name='book'),
	re_path(r'^books/', views.books.as_view(), name='books'),
	# re_path(r'^category/(?P<id>[0-9]+/)', views.category),
	re_path(r'^categories/', views.categories.as_view(), name='categories'),

]