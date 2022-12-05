from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

from cities.forms import CityForm
from cities.mixins import SuccessDeleteMessageMixin
from cities.models import City


def home(request, pk=None):
    if request.POST:
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
    # if pk:
    #     city = get_object_or_404(City, id=pk)
    #     context = {'objects': city}
    #     return render(request, 'cities/detail.html', context)
    form = CityForm()
    qs = City.objects.all()
    lst = Paginator(qs, 2)
    page_number = request.GET.get('page')
    page_obj = lst.get_page(page_number)
    context = {'page_obj': page_obj, 'form': form}
    return render(request, 'cities/index.html', context)


class CityListView(ListView):
    model = City
    paginate_by = 10
    template_name = "cities/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CityForm()
        return context


class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = 'cities/detail.html'
    context_object_name = 'object'


class CityCreateView(SuccessMessageMixin, CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('cities:home')
    success_message = "Город успешно создан: %(title)s"


class CityUpdateView(SuccessMessageMixin, UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('cities:home')
    success_message = "Город успешно отредактирован: %(title)s"


class CityDeleteView(SuccessDeleteMessageMixin, DeleteView):
    model = City
    template_name = 'cities/delete.html'
    success_url = reverse_lazy('cities:home')
    success_message = "Город успешно удален: %(title)s"

    def delete(self, request, *args, **kwargs):
        self.add_success_message(self.request)
        return super(CityDeleteView, self).delete(request, *args, **kwargs)

