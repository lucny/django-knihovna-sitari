from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('authors', views.AutorListView.as_view(), name='authors_list'),
    path('authors/<int:pk>', views.AutorDetailView.as_view(), name='author_detail'),
]
