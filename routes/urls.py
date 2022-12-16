from django.urls import path

from routes.views import home, find_routes, add_route

urlpatterns = [
    path('', home, name='home'),
    path('find_routes/', find_routes, name='find_routes'),
    path('add_route/', add_route, name='add_route'),
]
