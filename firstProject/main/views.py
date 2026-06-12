from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from .models import Team
# Create your views here.

def home_view(request:HttpRequest):
    x = 500
    teams = Team.objects.all()
    return render(request, 'main/home.html', {'x':x, 'teams': teams})

def add_view(request:HttpRequest):
    if request.method == 'POST':
        team_name = request.POST.get('name')
        team_city = request.POST.get('city')
        team_wins = request.POST.get('wins')
        team_losses = request.POST.get('losses')
        new_team = Team(name=team_name, city=team_city, wins=team_wins, losses=team_losses)
        new_team.save()
    return render(request, 'main/add.html')