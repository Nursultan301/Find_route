from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


from trains.forms import TrainForm
from trains.models import Train


class TrainListView(ListView):
    model = Train
    template_name = "trains/home.html"
    paginate_by = 5


class TrainDetailView(DetailView):
    model = Train
    template_name = "trains/detail.html"


class TrainUpdateView(SuccessMessageMixin, UpdateView):
    model = Train
    form_class = TrainForm
    template_name = "trains/update.html"
    success_url = reverse_lazy('trains')
    success_message = "Город успешно отредактирован"


class TrainDeleteView(DeleteView):
    model = Train
    # template_name = ""
    success_url = reverse_lazy('trains')

    def get(self, request, *args, **kwargs):
        messages.error(request, "Город успешно уделен")
        return self.post(request, *args, **kwargs)
