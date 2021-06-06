from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from .models import SuperHero

# Create your views here.

def index(request):
    heroe = SuperHero.objects.get(hero_name='Superman')
    heroe = model_to_dict(heroe)
    # heroes_list = list(heroes.values())
    return render(request, 'index.html', {'heroe': heroe})
    return HttpResponse(list(heroes.values()))
    return HttpResponse(list(heroes.values()))

def api(request):
    heroes = SuperHero.objects.all()
    return JsonResponse(list(heroes.values()), safe=False)