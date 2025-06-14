from django.urls import path
from . import views
from .views import BookListCreateView, BookRetrieveUpdateDestroyView

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),

    # Optional: Using class-based views (can replace the ones above)
    path('cbv/books/', BookListCreateView.as_view(), name='book-list-create'),
    path('cbv/books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-detail'),
]
