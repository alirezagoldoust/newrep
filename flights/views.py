# Create your views here.
from django.http.response import JsonResponse, HttpResponse
from .models import Airport

def list(request):
    flights = {
        'name':'boeing-707',
        'Flight_number':'142',
        'Seats':90,
        'Price':1200000,
    }
    return JsonResponse(flights)

def list2(request):
    airports = Airport.objects.all()
    airport_list = []
    for item in airports:
        dic = {
            'name' : item.name,
            'city': item.city,
        }
        airport_list.append(dic)
    return HttpResponse(airport_list)
