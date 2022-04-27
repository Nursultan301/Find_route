from django.urls import path

from trains.views import TrainListView, TrainUpdateView, TrainDeleteView, TrainDetailView

urlpatterns = [
    path('', TrainListView.as_view(), name='trains'),
    path('detail/<int:pk>', TrainDetailView.as_view(), name='detail'),
    path('update/<int:pk>', TrainUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', TrainDeleteView.as_view(), name='delete'),
]