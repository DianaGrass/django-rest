from django.contrib import admin
from book.models import Genre, BookModel


class BooksModelAdmin(admin.ModelAdmin):
    fields = ("title", "text", "author", "publisher", "genre")


admin.site.register(BookModel, BooksModelAdmin)
admin.site.register(Genre)