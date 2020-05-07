from django.urls import path
from . import views

urlpatterns = [
    path('world', views.world),
    path('hello', views.hello),
    path('adventure', views.adventure),
]
