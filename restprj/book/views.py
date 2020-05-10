from django.shortcuts import render, HttpResponse


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
