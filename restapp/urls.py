from django.urls import path

from .views import BookListAPIView, BookDetailAPIView, BookDeleteAPIView, BookUpdateAPIView, BookCreateAPIView, \
    BookListCreateAPIView, BookDeleteUpdateAPIView

urlpatterns = [
    path('books/', BookListAPIView.as_view()),
    path('book/', BookListCreateAPIView.as_view()),
    path('books/create/', BookCreateAPIView.as_view()),
    path('<int:pk>/', BookDetailAPIView.as_view()),
    path('<int:pk>/update/', BookUpdateAPIView.as_view()),
    path('<int:pk>/delete/', BookDeleteAPIView.as_view()),
    path('<int:pk>/destroy/', BookDeleteUpdateAPIView.as_view()),
]
