from django.contrib import admin
from books.models import *

# Register your models here.

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(ProfileBook)
admin.site.register(ProfileCategory)