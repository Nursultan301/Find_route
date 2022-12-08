from django.contrib import admin

from trains.models import Train


@admin.register(Train)
class TrainAdmin(admin.ModelAdmin):
    list_display = ('title', 'from_city', 'to_city', 'travel_time')
    search_fields = ('title', 'travel_time')
    list_filter = ('from_city', 'to_city')
    fields = ('title', 'from_city', 'to_city', 'travel_time')

