from rest_framework.serializers import ModelSerializer
from .models import Book, Genre
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")


class GenreSerializer(ModelSerializer):
    # author = UserSerializer()

    class Meta:
        model = Genre
        fields = "__all__"


class GenreSerializerCreate(ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class BookSerializerCreate(ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class BookSerializer(ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Book
        fields = "__all__"


