from django.contrib import admin
from .models import Chart


class ChartAdmin(admin.ModelAdmin):
    list_display = ('date',)
    search_fields = ('name',)
    list_filter = ('pvz',)


admin.site.register(Chart, ChartAdmin)
