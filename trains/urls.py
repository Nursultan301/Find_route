from django.urls import path

from trains.views import TrainListView


urlpatterns = [
    path('', TrainListView.as_view(), name='train')
]
