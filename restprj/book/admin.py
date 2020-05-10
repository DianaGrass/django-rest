from django.contrib import admin
from .models import Book, Genre, Comment


class BookModelAdmin(admin.ModelAdmin):
    fields = ("title", "text", "author", "genre")


admin.site.register(Book, BookModelAdmin)
admin.site.register(Genre)
admin.site.register(Comment)
