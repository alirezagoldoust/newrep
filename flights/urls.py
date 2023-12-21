from django.urls import path
from .views import list, list2


urlpatterns = [
    path('list', list),
    path('list2', list2),
]
