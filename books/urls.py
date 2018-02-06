from django.urls import path,re_path
from . import views

#app_name='books'
urlpatterns=[
	# re_path(r'^login/', views.login),
	re_path(r'^register/', views.register),
	# re_path(r'^$',views.home),
	# re_path(r'^home/', views.home),
	path('author/<int:pk>', views.AuthorView.as_view(), name='author-detail'),
	#re_path(r'^authors/', views.authors.as_view(), name='authors'),
	path('book/<int:pk>', views.BookView.as_view(), name='book-detail'),
	#re_path(r'^books/', views.books.as_view(), name='books'),
	path('categories/', views.CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>', views.CategoryView.as_view(), name='category-detail'),
]