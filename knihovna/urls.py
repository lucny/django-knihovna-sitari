from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('authors/', views.AutorListView.as_view(), name='authors_list'),
    path('authors/<int:pk>', views.AutorDetailView.as_view(), name='author_detail'),
    path('books/', views.KnihaListView.as_view(), name='books_list'),
    path('books/<int:pk>', views.KnihaDetailView.as_view(), name='book_detail'),
    path('books/add', views.KnihaCreateView.as_view(), name='book_add'),
]
