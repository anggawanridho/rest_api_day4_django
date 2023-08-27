from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookListView.as_view(), name='book-list'),
    path('books/<int:book_id>/', views.BookDetailView.as_view(), name='book-detail'),
    path('books/create/', views.BookCreateView.as_view(), name='book-create'),
    path('books/<int:book_id>/update/', views.BookUpdateView.as_view(), name='book-update'),
    path('books/<int:book_id>/delete/', views.BookDeleteView.as_view(), name='book-delete'),
]