from django.urls import path,re_path
from . import views

app_name='books'
urlpatterns=[
	# re_path(r'^login/', views.login),
	# re_path(r'^register/', views.register, name='register'),
	re_path(r'^$',views.register, name='register'),
	re_path(r'^login$',views.checkLogin, name='check-login'),
	re_path(r'^reg$',views.checkRegister, name='check-register'),
	re_path(r'^home/', views.home, name='home'),
	
	path('author/<int:pk>', views.AuthorView.as_view(), name='author-detail'),
	path('authors/', views.AuthorList.as_view(), name='author-list'),
	path('book/<int:pk>', views.BookView.as_view(), name='book-detail'),
	path('books/', views.BookList.as_view(), name='book-list'),
	path('categories/', views.CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>', views.CategoryView.as_view(), name='category-detail'),
	path('service1/<int:id>', views.service1, name="service1"),
	
	#path('service2/<int:id>', views.service2, name="service2"),
]