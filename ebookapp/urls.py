from django.urls import path
from . import views


urlpatterns=[
    path('',views.home, name='home'),
    # Get and Post
    path('books/',views.book_list, name='book_list'),
    #get,put and deletee
    path('books/<int:pk>/',views.book_detail, name ='book_detail'),
]

