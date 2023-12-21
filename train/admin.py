from django.contrib.admin import register, ModelAdmin
from .models import Train, Station

@register(Train)
class TranAdmin(ModelAdmin):
    list_display = ['date_time', 'origin', 'destination', 'capacity', 'price']

@register(Station)
class StationAdmin(ModelAdmin):
    list_display = ['name', 'city', 'phone_number']