from django.urls import path

from routes.views import home, find_routes

urlpatterns = [
    path('', home, name='home'),
    path('find_routes/', find_routes, name='find_routes'),
]
