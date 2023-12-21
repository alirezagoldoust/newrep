
from django.http.response import HttpResponse, JsonResponse

def wellcome(request):
    return HttpResponse('Wellcome to Alibaba!')

def About(request):
    return HttpResponse('Here is About page')

def flight(request):
    flights = {
        'name':'boeing-707',
        'Flight_number':'142',
        'Seats':90,
        'Price':1200000,
    }
    return JsonResponse(flights)