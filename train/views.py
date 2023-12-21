from django.http.response import JsonResponse, HttpResponse
from .models import Train
from django.shortcuts import render

# Create your views here.

def list(request):
    trains = Train.objects.all()
    train_list = []
    for item in trains:
        train_list.append({
            'Origin' : item.origin.name,
            'Destination' : item.destination.name,
            'Price' : item.price,
        })
    print(train_list)
    return JsonResponse(train_list, safe=False)
    # return HttpResponse('Hi')

# def list(request):
    # return render(request, 'train/list.html')

# def list(request):
    # trains = Train.objects.all()
    # contex = { 'trains' : trains }
    # print(contex)
    # return render(request, 'train/list.html', context=contex)

#def list(request):
    #airports = Airport.objects.all()
    #airport_list = []
    #for item in airports:
        #dic = {
            #'name' : item.name,
            #'city': item.city,
        #}
        #airport_list.append(dic)
    #return HttpResponse(airport_list)