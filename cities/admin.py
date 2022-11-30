from django.contrib import admin

from .models import City


@admin.register(City)
class AdminCity(admin.ModelAdmin):
    pass
