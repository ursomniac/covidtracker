from django.contrib import admin
from .models import DIVOCCase7DayAvg, DIVOCCaseTotal, DIVOCCaseDaily

class DIVOC7dAdmin(admin.ModelAdmin):
    list_display = ['id', 'location', 'case_date', 'cases']
    list_filter = ['location']

class DIVOCCaseTotalAdmin(admin.ModelAdmin):
    list_display = ['id', 'location', 'case_date', 'cases']
    list_filter = ['location']

class DIVOCCaseDailyAdmin(admin.ModelAdmin):
    list_display = ['id', 'location', 'case_date', 'cases']
    list_filter = ['location']
    
admin.site.register(DIVOCCase7DayAvg, DIVOC7dAdmin)
admin.site.register(DIVOCCaseTotal, DIVOCCaseTotalAdmin)
admin.site.register(DIVOCCaseDaily, DIVOCCaseDailyAdmin)