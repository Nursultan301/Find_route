from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView

from cities.mixins import SuccessDeleteMessageMixin
from cities.models import City
from routes.forms import RouteForm, RouteModelForm
from routes.models import Route
from routes.services import get_routes
from trains.models import Train


# @login_required
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


def save_route(request):
    if request.POST:
        form = RouteModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Маршрут успешно сохранен")
            return redirect('/')
        return render(request, 'routes/create.html', {"form": form})
    else:
        messages.error(request, "Нет данных для поиска")
        return redirect('/')


class RouteListView(ListView):
    paginate_by = 5
    model = Route
    template_name = 'routes/list.html'


class RouteDetailView(DetailView):
    queryset = Route.objects.all()
    template_name = 'routes/detail.html'
    context_object_name = 'object'


class RouteDeleteView(SuccessDeleteMessageMixin, LoginRequiredMixin, DeleteView):
    model = Route
    template_name = 'routes/delete.html'
    success_url = reverse_lazy('cities:home')
    success_message = "Город успешно удален: %(title)s"

    def delete(self, request, *args, **kwargs):
        self.add_success_message(self.request)
        return super(RouteDeleteView, self).delete(request, *args, **kwargs)