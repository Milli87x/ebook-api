from django.urls import path
from . import views
from .views import BookListCreateView, BookRetrieveUpdateDestroyView

urlpatterns = [
    path('', views.home, name='home'),
    path('books/',BookListCreateView.as_view(),name='book-list-create'),
    path('books/<int:pk>/',BookRetrieveUpdateDestroyView.as_view(),name='book-detail'),
]
