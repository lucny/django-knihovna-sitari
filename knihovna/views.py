from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import KnihaForm
from .models import Kniha, Zanr, Autor


def index(request):
    zanr = 'povídky'
    context = {
        'nadpis': zanr,
        'knihy': Kniha.objects.order_by('rok_vydani').filter(zanry__nazev=zanr),
        'zanry': Zanr.objects.all()
    }
    return render(request, 'index.html', context=context)


class AutorListView(ListView):
    model = Autor
    context_object_name = 'authors'
    template_name = 'autor/authors_list.html'


class AutorDetailView(DetailView):
    model = Autor
    context_object_name = 'author'
    template_name = 'autor/author_detail.html'


class KnihaListView(ListView):
    model = Kniha
    context_object_name = 'books'
    template_name = 'kniha/books_list.html'


class KnihaDetailView(DetailView):
    model = Kniha
    context_object_name = 'book'
    template_name = 'kniha/books_detail.html'


class KnihaCreateView(CreateView):
    model = Kniha
    form_class = KnihaForm
    template_name = 'kniha/books_form.html'
    success_url = reverse_lazy('books_list')