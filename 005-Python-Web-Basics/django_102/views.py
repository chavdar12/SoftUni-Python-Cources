from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView

from django_102.models.game import Game
from django_102.models.person import Person
from django_102.models.player import Player


def test_view(request):
    return HttpResponse("This should return something")


def index(request):
    title = 'My first Django Project'
    users = User.objects.all()
    games = Game.objects.all_with_players_count()

    context = {
        'title': title,
        'users': users,
        'games': games,
    }
    return render(request, 'index.html', context)


class UsersListView(ListView):
    model = User
    template_name = 'index2.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = 'From class view'
        return context


class GamesListView(ListView):
    model = Game
    template_name = 'games.html'


def method_req(request):
    context = {
        'name': 'My Name',
        'age': 17,
    }

    if request.content_type == 'application/json':
        return JsonResponse(context)

    return render(request, 'method_req.html', context)


def raises_exception(request):
    raise Exception('Raised')


def create_game(request):
    game = Game(name='CoD', difficulty_level=0)
    game.save()
    return redirect(request, 'index')
