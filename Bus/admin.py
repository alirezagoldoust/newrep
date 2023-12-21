from django.contrib.admin import register, ModelAdmin
from .models import Travel, Terminal

@register(Travel)
class AirportAdmin(ModelAdmin):
    pass

@register(Terminal)
class AirportAdmin(ModelAdmin):
    pass