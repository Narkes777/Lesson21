from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Player, Match

# Create your views here.

class PlayerList(ListView):
    model = Player
    paginate_by = 2
    paginate_orphans = 1

class PlayerDetail(DetailView):
    model = Player
    context_object_name = 'player'

class PlayerCreate(CreateView):
    model = Player
    fields = '__all__'
    success_url = reverse_lazy('player_list')


class PlayerUpdate(UpdateView):
    model = Player
    fields = '__all__'
    success_url = reverse_lazy('player_list')


class PlayerDelete(DeleteView):
    model = Player
    success_url = reverse_lazy('player_list')
    template_name = 'New/post_form.html'


class MatchList(ListView):
    model = Match
    paginate_by = 2
    paginate_orphans = 1

class MatchDetail(DetailView):
    model = Match
    context_object_name = 'match'

class MatchCreate(CreateView):
    model = Match
    fields = '__all__'
    success_url = reverse_lazy('match_list')


class MatchUpdate(UpdateView):
    model = Match
    fields = '__all__'
    success_url = reverse_lazy('match_list')


class PlayerDelete(DeleteView):
    model = Player
    success_url = reverse_lazy('match_list')
    template_name = 'New/post_form.html'