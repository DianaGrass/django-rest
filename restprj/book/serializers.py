from rest_framework.serializers import ModelSerializer
from .models import Book
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")

#
# class GenreSerializerCreate(ModelSerializer):
#     class Meta:
#         model = Genre
#         fields = ("title",)


class BookSerializerCreate(ModelSerializer):
    # publisher = UserSerializerAPI()
    # genre = GenreSerializerAPI()

    class Meta:
        model = Book
        fields = "__all__"


class BookSerializer(ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Book
        fields = "__all__"


