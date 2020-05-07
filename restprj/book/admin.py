from django.contrib import admin
from book.models import Genre, Book


class BookModelAdmin(admin.ModelAdmin):
    fields = ("title", "text", "author", "publisher", "genre")


admin.site.register(Book, BookModelAdmin)
admin.site.register(Genre)
