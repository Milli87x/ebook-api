from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
   
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    pdf_file = models.FileField(upload_to= 'media')
    catagory = models.ForeignKey(Category, on_delete = models.SET_NULL, null = True)
    upload_time = models.DateTimeField(auto_now_add = True)
    

    def __str__(self):
        return self.title
        