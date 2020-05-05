from rest_framework import serializers
from book.models import Genre, BookModel
from django.contrib.auth.models import User


class UserSerializerAPI(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")


class GenreSerializerAPI(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("title",)


class BookModelSerialzerAPI(serializers.ModelSerializer):
    publisher = UserSerializerAPI()
    genre = GenreSerializerAPI()

    class Meta:
        model = BookModel
        fields = "__all__"


class BookModelSerializerAPIPOST(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = (
            "title",
            "text",
            "author",
            "publisher",
            "genre",
        )