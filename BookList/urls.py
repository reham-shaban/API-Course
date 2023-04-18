from django.urls import path
from . import views

app_name = 'booklist'

urlpatterns = [
    path('books', views.books, name='books'),
    path('book/<int:pk>', views.BookView.as_view())
]