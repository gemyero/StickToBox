from django.urls import path,re_path
from . import views

urlpatterns=[
	re_path(r'^login/', views.login),
	re_path(r'^register/', views.register),
	re_path(r'^',views.home),
	re_path(r'^home/', views.home),
	re_path(r'^author/(?P<id>[0-9]+)/', views.author),
	re_path(r'^authors/', authors),
	re_path(r'^book/(?P<id>[0-9]+)/', views.book),
	re_path(r'^books/', views.books),
	re_path(r'^category/', views.category),
	re_path(r'^categories/(?P<id>[0-9]+/)', views.categories),

]