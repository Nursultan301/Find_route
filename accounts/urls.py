from django.urls import path

from accounts.views import login_view, logout_view, registration_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout_view/', logout_view, name='logout'),
    path('registration/', registration_view, name='register'),
]
