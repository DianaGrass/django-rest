from django.urls import path
from . import views

urlpatterns = [
    path('world', views.world),
    path('hello', views.hello),
    path('adventure', views.adventure),
    path('train', views.train),
    path('trip', views.trip),
    path('api/v1/list/', views.BookListView.as_view()),
    path('api/v1/create/', views.BookCreateView.as_view()),

]
