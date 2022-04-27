from django.contrib import admin

from trains.models import Train


@admin.register(Train)
class TrainAdmin(admin.ModelAdmin):
    list_display = ('name', 'from_city', 'to_city', 'travel_time')
    list_filter = ('from_city', 'to_city')
    list_editable = ('travel_time', )
    search_fields = ("name",)


