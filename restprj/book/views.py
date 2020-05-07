from django.shortcuts import render, HttpResponse


def hello(request):
    return render(request, "index.html", {"name": "Morty", "title": "chaos", "user": "Rick"})


def world(request):
    return render(request, "world.html", {"X": "text", "Y": "PF", "Z": "1212123"})
