from django.contrib import admin
from .models import Publisher, Author, Genre, Book, Tyrage

admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(Tyrage)

# Register your models here.
