from django.shortcuts import render
from django.http import HttpResponse
from polls.models import  Game
import polls.rest_calls
from django.shortcuts import render
from django.template.response import TemplateResponse


def index(request):

    Game.objects.all().delete()
    game_json = polls.rest_calls.game()
    i=""
    for e in game_json:
        Game.objects.create(
            players=e['spillere'],
            dice=e['terninger'],
            user=e['brugernavn'],
            port=e['port']).save()

    return HttpResponse("updated database")

    #response = TemplateResponse(request, 'polls/user_listing.html', {})
    #for u in users:
    #    s += "<p> " + str(u) + "</p> </br>"
    #polls.rest_calls.login(u.username, u.password)
    #return render(request, 'polls/user_listing.html', {'users': users})


def login(request):
    return HttpResponse("hej")
