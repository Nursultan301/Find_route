from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from cities.mixins import SuccessDeleteMessageMixin
from trains.forms import TrainForm
from trains.models import Train


class TrainListView(ListView):
    model = Train
    paginate_by = 5
    template_name = 'trains/trains.html'


class TrainDetailView(DetailView):
    model = Train
    template_name = 'trains/detail_train.html'


class TrainCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/create_train.html'
    success_url = reverse_lazy('trains:train')
    success_message = "Поезд успешно создан %(title)s"


class TrainUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/update_train.html'
    success_url = reverse_lazy('trains:train')
    success_message = 'Поезд успешно отредактирован: %(title)s'


class TrainDeleteView(SuccessDeleteMessageMixin, LoginRequiredMixin, DeleteView):
    model = Train
    template_name = 'trains/delete_train.html'
    success_url = reverse_lazy('trains:train')
    success_message = "Поезд успешно удален: %(title)s"

    def delete(self, request, *args, **kwargs):
        self.add_success_message(self.request)
        return super(TrainDeleteView, self).delete(request, *args, **kwargs)
