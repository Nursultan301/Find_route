from django.urls import path

from trains.views import TrainListView, TrainDetailView, TrainCreateView, TrainUpdateView, TrainDeleteView

urlpatterns = [
    path('', TrainListView.as_view(), name='train'),
    path('detail/<int:pk>/', TrainDetailView.as_view(), name='train_detail'),
    path('update/<int:pk>/', TrainUpdateView.as_view(), name='train_update'),
    path('delete/<int:pk>/', TrainDeleteView.as_view(), name='train_delete'),
    path('add/', TrainCreateView.as_view(), name='train_create'),
]
