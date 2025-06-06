from rest_framework import serializers 
from ebookapp.models import Book,Category


class CatagorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        field = ['id','name']

class BookSerializer(serializers.ModelSerializer):

    category = CatagorySerializer(read_only=True)
    category_id= serializers.PrimaryKeyRelatedField(queryset=Category.objects.all()
    ,write_only=True,source='category')


    class Meta:
        model = Book
        field = ['title','author','description','pdf_file','catagory',
     'upload_time','category','category_id']