from django.contrib import admin
from django.urls import path, include

from routes.views import route_home, find_routes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cities.urls')),
    path('trains/', include('trains.urls')),
    path('routes/', route_home, name='route'),
    path('find_routes/', find_routes, name='find_routes'),

]
