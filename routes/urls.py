from django.urls import path

from routes.views import home

urlpatterns = [
    path('', home)
]
