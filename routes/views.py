from django.shortcuts import render, redirect
from django.contrib import messages

from cities.models import City
from routes.forms import RouteForm, RouteModelForm
from routes.services import get_routes
from trains.models import Train


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
        if data:
            total_time = int(data['total_time'])
            from_city_id = int(data['from_city'])
            to_city_id = int(data['to_city'])
            trains = data['trains'].split(',')
            trains_lst = [int(t) for t in trains if t.isdigit()]
            qs = Train.objects.filter(id__in=trains_lst).select_related('from_city', 'to_city')
            cities = City.objects.filter(id__in=[from_city_id, to_city_id]).in_bulk()
            form = RouteModelForm(
                initial={
                    'from_city': cities[from_city_id],
                    'to_city': cities[to_city_id],
                    'travel_times': total_time,
                    'trains': qs

                         }
            )
            context['form'] = form
        return render(request, 'routes/create.html', context)
    else:
        messages.error(request, "Нет данных для поиска")
        return redirect('/')
