from django.contrib import admin
from .models import Workshop


# Register your models here.
class WorkshopAdmin(admin.ModelAdmin):
    list_display = ('session', 'title', 'roomnumber', 'starttime', 'endtime')
    list_filter = ('session', 'title', 'roomnumber', 'starttime', 'endtime')

admin.site.register(Workshop, WorkshopAdmin)
