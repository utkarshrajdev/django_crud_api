from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
# Create your views here.

class CreateBook(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class RetrieveUpdateDestroyBook(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
