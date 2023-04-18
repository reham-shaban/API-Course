from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from django.db import IntegrityError
from django.forms.models import model_to_dict

from .models import Book

# fuction
@api_view(['GET', 'POST'])
def books(request):
    if request.method == 'GET':
        books = Book.objects.all().values()
        return Response(books, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        title = request.POST.get('title') 
        author = request.POST.get('author')
        price = request.POST.get('price')      
        book = Book(title=title, author=author, price=price)
        
        try:
            book.save()
        except IntegrityError:
            return Response( {'error':'true', 'message':'required field missing'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(model_to_dict(book), status=status.HTTP_201_CREATED)

# class
class BookView(APIView): 
    def get(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            return Response(model_to_dict(book), status.HTTP_200_OK)
        
        except Book.DoesNotExist:
            error_message = {"error":f"book with id {pk} does not exist"}
            return Response(error_message, status=status.HTTP_404_NOT_FOUND)
            
    def put(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            book.title = request.POST.get('title')
            book.author = request.POST.get('author')
            book.price = request.POST.get('price')
            book.save()
            
            return Response(model_to_dict(book), status.HTTP_205_RESET_CONTENT)
            
        except Book.DoesNotExist:
            error_message = {"error":f"book with id {pk} does not exist"}
            return Response(error_message, status=status.HTTP_404_NOT_FOUND)
        