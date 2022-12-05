from django.urls import path

from trains.views import TrainListView, TrainDetailView, TrainCreateView

urlpatterns = [
    path('', TrainListView.as_view(), name='train'),
    path('detail/<int:pk>/', TrainDetailView.as_view(), name='train_detail'),
    path('add/', TrainCreateView.as_view(), name='train_create'),
]
