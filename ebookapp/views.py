from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Book,Category
from .serializers import BookSerializer, CatagorySerializer
from rest_framework import generics,permissions

# home page 
def home(request):
    return JsonResponse({'message':'Hello and Welcome'})
    
@api_view(['GET','POST'])
#list all books or create new ones
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all().order_by('upload_time')
        serializer = BookSerializer(books, many =True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,Status=status.HTTP_201_CREATED)
            return Response(serializer.error,Status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET','PUT','DELETE'])        
def book_detail(request,pk):
    try:
        book = Book.object.get(pk=pk)
    except Book.DoesNotExist:
        return Response({'error':'Book Not Found'})
    status = status.HTTP_404_NOT_FOUND

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = BookSerializer(book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        book.delete()
        return
    Response(status=status.HTTP_204_NO_CONTENT)

#handles get,post,put,delete for CRUD
#uses serializer to convert model data to json   
# List all books or create a new one
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# Retrieve, update or delete a book
class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]