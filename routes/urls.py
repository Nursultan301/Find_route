from django.urls import path

from routes.views import home, find_route

urlpatterns = [
    path('', home, name='home'),
    path('find_route/', find_route, name='find_route'),
]
