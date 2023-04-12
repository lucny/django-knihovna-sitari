from django.shortcuts import render
from django.views.generic import ListView, DetailView

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
