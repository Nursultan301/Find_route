from django.shortcuts import render
from django.contrib import messages

from routes.forms import RouteForm


def route_home(request):
    form = RouteForm()
    return render(request, 'routes/home.html', {"form": form})


def find_routes(request):
    if request.POST:
        form = RouteForm(request.POST)
        a = 1
        return render(request, 'routes/home.html', {"form": form})

    else:
        form = RouteForm()
        messages.error(request, "Нет данных для поиска")
        return render(request, 'routes/home.html', {"form": form})
