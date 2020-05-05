from django.contrib import admin
from book.models import Genre, BookModel


class BookModelAdmin(admin.ModelAdmin):
    fields = ("title", "text", "author", "publisher", "genre")


admin.site.register(BookModel, BookModelAdmin)
admin.site.register(Genre)
