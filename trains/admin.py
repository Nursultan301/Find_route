from django.contrib import admin

from trains.models import Train


@admin.register(Train)
class TrainAdmin(admin.ModelAdmin):
    list_display = ('title', 'travel_time', 'from_city', 'to_city')
    search_fields = ('title', 'travel_time')
    list_filter = ('from_city', 'to_city')