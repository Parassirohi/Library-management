
from rest_framework import viewsets
from .models import Genre,  Author, Book
from .serializers import GenreSerializer,  AuthorSerializer, BookSerializer

from .pagination import DefaultPagination

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = 'registration_code'

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = DefaultPagination
