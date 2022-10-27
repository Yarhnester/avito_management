from django.contrib import admin
from .models import Record


class RecordAdmin(admin.ModelAdmin):
    list_display = ('partner',)
    search_fields = ('partner',)
    list_filter = ('payment_date',)


# Register your models here.
admin.site.register(Record, RecordAdmin)
