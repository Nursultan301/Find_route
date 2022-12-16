from django.shortcuts import render, redirect
from django.contrib import messages

from routes.forms import RouteForm
from routes.services import get_routes


def home(request):
    form = RouteForm()
    return render(request, 'routes/routes.html', {'form': form})


def find_routes(request):
    if request.POST:
        form = RouteForm(request.POST)
        if form.is_valid():
            try:
                context = get_routes(request, form)
            except ValueError as e:
                messages.error(request, e)
                return render(request, "routes/routes.html", {'form': form})
            return render(request, "routes/routes.html", context)
        return render(request, "routes/routes.html", {'form': form})
    else:
        form = RouteForm()
        messages.error(request, "Нет данных для поиска")
        return render(request, "routes/routes.html", {'form': form})


def add_route(request):
    if request.POST:
        context = {}
        data = request.POST
        return render(request, 'routes/create.html', context)
    else:
        messages.error(request, "Нет данных для поиска")
        return redirect('/')
