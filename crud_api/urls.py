from django.contrib import admin
from django.urls import include, path
from .views import book, book_detail

urlpatterns = [
    path('book/', book),
    path('book/<int:id>', book_detail),
]