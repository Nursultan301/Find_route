from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from cities.forms import HtmlForm, CityForm
from cities.models import City


def home(request, pk=None):
    if request.POST:
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
    # if pk:
    # city = City.objects.filter(pk=pk).first()
    # city = City.objects.get(pk=pk)
    # city = get_object_or_404(City, pk=pk)
    # context = {'object': city}
    # return render(request, 'cities/detail.html', context)
    form = CityForm
    qs = City.objects.all()
    context = {'objects_list': qs, "form": form}
    return render(request, 'cities/home.html', context)


class CityListView(ListView):
    model = City
    paginate_by = 2
    context_object_name = 'objects_list'
    template_name = 'cities/home.html'

    def get_context_data(self, **kwargs):
        context = super(CityListView, self).get_context_data(**kwargs)
        context['form'] = CityForm()
        return context


class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = 'cities/detail.html'


class CityCreateView(SuccessMessageMixin, CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'
    success_message = "Город успешно создан"
    success_url = reverse_lazy('home')


class CityUpdateView(SuccessMessageMixin, UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('home')
    success_message = "Город успешно отредактирован"


class CityDeleteView(DeleteView):
    model = City
    # template_name = 'cities/delete.html'
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        messages.error(request, 'Город успешно уделен')
        return self.post(request, *args, **kwargs)
