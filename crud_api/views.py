from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BookSerializer
from .models import Book
from rest_framework import status
# Create your views here.

@api_view(['GET','POST'])
def book(request):
    if request.method == 'GET':
        data = Book.objects.all()
        serializer = BookSerializer(data, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = BookSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET','PUT','PATCH','DELETE'])
def book_detail(request, id):
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        book = Book.objects.all()
        serializer = BookSerializer(book, many = True)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        data = request.data
        serializer = BookSerializer(book, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    if request.method == 'PATCH':
        data = request.data
        serializer = BookSerializer(book, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
    if request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
