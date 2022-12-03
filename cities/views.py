from django.shortcuts import render, get_object_or_404

from cities.models import City


def home(request, pk=None):
    if pk:
        city = get_object_or_404(City, id=pk)
        context = {'objects': city}
        return render(request, 'cities/detail.html', context)
    qs = City.objects.all()
    context = {'qs': qs}
    return render(request, 'cities/index.html', context)
