from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Hero


# Create your views here.

def index(request):
    all_heroes = Hero.objects.all()
    context = {
        'all_heroes': all_heroes
    }
    return render(request, 'heroes/index.html', context)


def detail(request, hero_id):
    specific_hero = Hero.objects.get(pk=hero_id)
    context = {
        'specific_hero': specific_hero
    }
    return render(request, 'heroes/index.html', context)


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary = request.POST.get('primary_ability')
        secondary = request.POST.get('secondary_ability')
        catchphrase = request.POST.get('catchphrase')
        new_hero = Hero(name=name, alter_ego=alter_ego, primary_ability=primary, secondary_ability=secondary,
                        catchphrase=catchphrase)
        new_hero.save()
        return HttpResponseRedirect(reverse('heroes:index'))
    else:
        return render(request, 'heroes/create.html')
