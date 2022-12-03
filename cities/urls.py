from django.urls import path

from .views import home, CityDetailView, CityCreateView

urlpatterns = [
    path('', home, name='home'),
    # path('<int:pk>/', home, name='detail'),
    path('detail/<int:pk>/', CityDetailView.as_view(), name='detail'),
    path('add/', CityCreateView.as_view(), name='create'),
]
