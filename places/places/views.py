from django.shortcuts import render
from .models import Place
from django.http import JsonResponse
from django.http import HttpResponse
import json




# Create your views here.
def list_places(request):
    queryset = Place.objects.all()
    context = list (queryset.values('id','name'))
    return JsonResponse(context, safe=False)

def placeCreate(request):
    if request.method =='POST':
        data = request.body.decode('uft-8')
        data_json = json.loads(data)
        place = Place()
        place.name = data_json["name"]
        place.save()
        return HttpResponse("successfully created Place")