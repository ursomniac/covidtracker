from django.contrib import admin
from .models import USVaccination

class USVAdmin(admin.ModelAdmin):
    list_display = ['id', 'location', 'sample_date', 'people_vaccinated_per_hundred', 'people_fully_vaccinated_per_hundred', 'total_boosters_per_hundred']
    list_filter = ['location']

admin.site.register(USVaccination, USVAdmin)