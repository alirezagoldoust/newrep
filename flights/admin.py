from django.contrib.admin import register, ModelAdmin
from .models import flights, Airport

# Register your models here to show them in admin panel
@register(flights)
class FlightAdmin(ModelAdmin):
    list_display = ['name', 'origin', 'destination']


@register(Airport)
class AirportAdmin(ModelAdmin):
    list_display = ['name', 'city', 'phone_number']