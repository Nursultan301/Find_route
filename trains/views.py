from django.shortcuts import render
from django.views.generic import ListView

from trains.models import Train


class TrainListView(ListView):
    model = Train
    paginate_by = 5
    template_name = 'trains/trains.html'
