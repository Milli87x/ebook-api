from rest_framework import serializers 
from ebookapp.models import Book,Category


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        field = '__all__'
        

class CatagorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        field = '__all__'
   