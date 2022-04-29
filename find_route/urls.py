from django.contrib import admin
from django.urls import path, include

from routes.views import route_home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cities.urls')),
    path('trains/', include('trains.urls')),
    path('routes/', route_home, name='route'),

]
