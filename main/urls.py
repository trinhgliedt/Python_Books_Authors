from django.urls import path

from . import views

urlpatterns = [
    path('book', views.book),
    path('author', views.author),
    path('book/add', views.add_book),
    path('author/add', views.add_author),
    path('book/<int:book_id>', views.show_book),
    path('author/<int:author_id>', views.show_author),
    path('book/add-author/<int:book_id>', views.add_author_to_book),
    path('author/add-book/<int:author_id>', views.add_book_to_author),
]