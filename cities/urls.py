from django.urls import path

from .views import home, CityDetailView, CityCreateView, CityUpdateView

urlpatterns = [
    path('', home, name='home'),
    # path('<int:pk>/', home, name='detail'),
    path('detail/<int:pk>/', CityDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', CityUpdateView.as_view(), name='update'),
    path('add/', CityCreateView.as_view(), name='create'),
]
