from django.shortcuts import render, HttpResponse
from .models import Book, Genre
from .serializers import BookSerializer, BookSerializerCreate, GenreSerializerCreate, GenreSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions


def hello(request):
    return render(request, "index.html", {"name": "Morty", "title": "chaos", "user": "Rick"})


def world(request):
    return render(request, "world.html", {"X": "text", "Y": "PF", "Z": "1212123"})


def adventure(request):
    return render(request, "adventure.html", {"what": "adventure", "time": "20", "text": "go"})


def train(request):
    return render(request, "train.html", {"what": "train", "time": "20", "text": "www.train.com"})


def trip(request):
    return render(request, "trip.html")


class BookListView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookCreateView(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = BookSerializerCreate


class BookDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = BookSerializerCreate
    queryset = Book.objects.all()


class GenreListView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()


class GenreCreateView(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = GenreSerializerCreate


