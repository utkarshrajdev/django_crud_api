from django.contrib import admin
from django.urls import include, path
from .views import CreateBook,RetrieveUpdateDestroyBook

urlpatterns = [
    path('book/', CreateBook.as_view(),name="create_book"),
    path('update/<int:pk>/',RetrieveUpdateDestroyBook.as_view(),name="retrieve_update_destroy_book"),
]