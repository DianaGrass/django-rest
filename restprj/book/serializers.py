from rest_framework import serializers
from book.models import Genre, Book
from django.contrib.auth.models import User


class UserSerializerAPI(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")


class GenreSerializerAPI(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("title",)


class BookSerializerAPI(serializers.ModelSerializer):
    publisher = UserSerializerAPI()
    genre = GenreSerializerAPI()

    class Meta:
        model = Book
        fields = "__all__"


class BookSerializerAPIPOST(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            "title",
            "text",
            "author",
            "publisher",
            "genre",
        )