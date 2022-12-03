from django.urls import path

from .views import home, CityDetailView

urlpatterns = [
    path('', home, name='home'),
    # path('<int:pk>/', home, name='detail'),
    path('<int:pk>/', CityDetailView.as_view(), name='detail')
]
