from django.shortcuts import render


def home(request):
    return render(request, 'cities/home.html')


def about(request):
    return render(request, 'cities/about.html')