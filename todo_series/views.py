from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from .models import Movie, Saison


def index(request):
    list_series = Movie.objects.all()[:5]
    context = {'list_series': list_series}
    return render(request, 'todo_series/index.html', context)

def detail(request, serie_id):
    serie = get_object_or_404(Movie, pk=serie_id)
    return render(request, 'todo_series/detail.html', {'serie': serie})


def detail_saison(request, serie_id, saison_id):
    saison = get_object_or_404(Saison, pk=saison_id)
    return render(request, 'todo_series/detail_saison.html', {'saison': saison})