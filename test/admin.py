from django.contrib import admin
from .models import *


class TrainAdmin(admin.ModelAdmin):
    list_display = ('number', 'train_type', 'vagon_number')
    list_display_links = ('number', 'vagon_number')
    search_fields = ('number', 'train_type', 'vagon_number')


class StationAdmin(admin.ModelAdmin):
    list_display = ('name', 'zone')
    list_display_links = ('name', 'zone')
    search_fields = ('name', 'zone')


class PathAdmin(admin.ModelAdmin):
    list_display = ('start_station', 'end_station', 'station_list', 'start_time', 'end_time')
    list_display_links = ('start_station', 'end_station', 'station_list')
    search_fields = ('start_station', 'end_station', 'station_list', 'start_time', 'end_time')


admin.site.register(Train, TrainAdmin)
admin.site.register(Station, StationAdmin)
admin.site.register(Path, PathAdmin)




# Register your models here.
