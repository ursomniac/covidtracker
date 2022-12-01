from django.contrib import admin
from .models import StateRegion, USCounty

class StateRegionAdmin(admin.ModelAdmin):
    list_display = ['name', 'population', 'location_class', 'abbreviation']
    list_filter = ['location_class']

class USCountyAdmin(admin.ModelAdmin):
    list_display = ['name', 'population', 'location_class', 'abbreviation']

admin.site.register(StateRegion, StateRegionAdmin)
admin.site.register(USCounty, USCountyAdmin)