from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('cities.urls', 'cities'))),
    path('trans/', include(('trains.urls', 'trains')))
]
