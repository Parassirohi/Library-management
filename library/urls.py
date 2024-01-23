
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('genres', views.GenreViewSet, basename='genre')
router.register('authors', views.AuthorViewSet, basename='author')
router.register('books', views.BookViewSet, basename='book')

urlpatterns = [
    path('', include(router.urls)),
]
