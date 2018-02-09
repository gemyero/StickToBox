from django.urls import path,re_path
from . import views
from django.conf.urls import url
from django.conf import settings
from django.contrib.auth.views import logout
# from django.views.generic import list_detail

app_name = 'books'

urlpatterns=[
	# re_path(r'^login/', views.login),
	# re_path(r'^$', list_detail.object_list, all_models_dict, name='home'),
	re_path(r'^$', views.home, name='home'),
	re_path(r'^register/', views.register, name='register'),
	re_path(r'^login$', views.checkLogin, name='check-login'),
    re_path(r'^logout/$', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
	re_path(r'^reg$', views.checkRegister, name='check-register'),
	path('author/<int:pk>', views.AuthorView.as_view(), name='author-detail'),
	path('authors/', views.AuthorList.as_view(), name='author-list'),
	path('book/<int:pk>', views.BookView.as_view(), name='book-detail'),
	path('books/', views.BookList.as_view(), name='book-list'),
	path('categories/', views.CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>', views.CategoryView.as_view(), name='category-detail'),
	path('service1/<int:id>', views.service1, name="service1"),
	path('service5/<str:status>', views.service5, name="service5"),
	path('search/', views.search, name="search"),
	path('ssearch/<str:keyword>', views.searchService, name="search-service"),
	#path('service2/<int:id>', views.service2, name="service2"),
]
