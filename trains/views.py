from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from trains.forms import TrainForm
from trains.models import Train


class TrainListView(ListView):
    model = Train
    paginate_by = 5
    template_name = 'trains/trains.html'


class TrainDetailView(DetailView):
    model = Train
    template_name = 'trains/detail_train.html'


class TrainCreateView(CreateView):
    model = Train
    template_name = 'trains/create_train.html'
    success_url = reverse_lazy('trains:train')
    form_class = TrainForm
