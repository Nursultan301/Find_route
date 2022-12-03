from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from cities.forms import CityForm
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
    context = {'qs': qs, 'form': form}
    return render(request, 'cities/index.html', context)


class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = 'cities/detail.html'
    context_object_name = 'object'
