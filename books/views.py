from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from .models import Book

class BookListView(APIView):
    def get(self, request):
        books = Book.objects.all()
        print(books)
        serialized_books = [
            {
                "id": book.id,
                "title": book.title,
                "author": book.author,
                "year": book.year,
                "publisher": book.publisher,
                "genre": book.genre,
                "rating": book.rating,
            }
            for book in books
        ]
        return Response(serialized_books)

class BookDetailView(APIView):
    def get(self, request, book_id):
        try:
            book = Book.objects.get(id=book_id)
            serialized_book = {
                "id": book.id,
                "title": book.title,
                "author": book.author,
                "year": book.year,
                "publisher": book.publisher,
                "genre": book.genre,
                "rating": book.rating,
            }
            return Response(serialized_book)
        except Book.DoesNotExist:
            return Response({'message': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

class BookCreateView(APIView):
    def post(self, request):
        title = request.GET.get('title', 'Tidak Berjudul')
        author = request.GET.get('author', 'Tidak Berpenulis')
        year = int(request.GET.get('year', 1945)) if request.GET.get('year') and request.GET.get('year').isdigit() else None
        publisher = request.GET.get('publisher', 'Tidak ada Publisher')
        genre = request.GET.get('genre', 'Tidak Berkategori')
        rating = request.GET.get('rating', 0.0)

        if not any([title, author, year, genre, rating]):
            return JsonResponse({'message': 'At least one required field should be provided'}, status=status.HTTP_400_BAD_REQUEST)
        
        newBook = {
            'title': title,
            'author': author,
            'year': year,
            'publisher': publisher,
            'genre': genre,
            'rating': rating
        }

        serialized_book = {
            "title": newBook['title'],
            "author": newBook['author'],
            "year": newBook['year'],
            "publisher": newBook['publisher'],
            "genre": newBook['genre'],
            "rating": newBook['rating'],
        }

        Book.objects.create(**newBook)

        return JsonResponse(serialized_book, status=status.HTTP_201_CREATED)

class BookUpdateView(APIView):
    def put(self, request, book_id):
        try:
            book = Book.objects.get(id=book_id)
            book_data = {
            'title': request.GET.get('title', book.title),
            'author': request.GET.get('author', book.author),
            'year': int(request.GET.get('year', book.year)) if request.data.get('year') and request.data.get('year').isdigit() else book.year,
            'publisher': request.GET.get('publisher', book.publisher),
            'genre': request.GET.get('genre', book.genre),
            'rating': float(request.GET.get('rating', book.rating))
            }

            for field, value in book_data.items():
                setattr(book, field, value)
            book.save()

            serialized_book = {
                "id": book.id,
                'title': request.data.get('title', book.title),
                'author': request.data.get('author', book.author),
                'year': int(request.data.get('year', book.year)) if request.data.get('year') and request.data.get('year').isdigit() else book.year,
                'publisher': request.data.get('publisher', book.publisher),
                'genre': request.data.get('genre', book.genre),
                'rating': float(request.data.get('rating', book.rating))
            }
            return JsonResponse(serialized_book)
        except Book.DoesNotExist:
            return Response({'message': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

class BookDeleteView(APIView):
    def delete(self, request, book_id):
        try:
            book = Book.objects.get(id=book_id)
            book.delete()
            return Response({'message': 'Book deleted successfully'})
        except Book.DoesNotExist:
            return Response({'message': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
