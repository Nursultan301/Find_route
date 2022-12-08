from django.shortcuts import render
from django.contrib import messages

from routes.forms import RouteForm


def home(request):
    form = RouteForm()
    return render(request, 'routes/routes.html', {'form': form})


def find_route(request):
    if request.Post:
        form = RouteForm(request.POST)
        a = 1
    else:
        form = RouteForm()
        messages.error(request, "Нет данных для поиска")
        return render(request, "routes/routes.html", {'form': form})
