from django.contrib import admin

from routes.models import Route


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    pass
