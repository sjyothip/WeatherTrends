from django.shortcuts import render
from . import models
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import requests

@csrf_exempt
def test(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=f8a5d735b096ea2ac24b60c551dca284'

    city=request.POST.get('city')
    response = requests.get(url.format(city)).json()
    rse = int((response['main']['temp'])/3.4)
    tempe = (rse-32) * 5//9 
    speed = response['wind']['speed']
    test = {
            'city_name': city,
			'temp': tempe,
			'weather': response['weather'][0]['main'],
			'wind_speed': speed,
            'Clouds' : response['clouds']['all'],
            'pressure' : response['main']['pressure'] ,
            'humidity' : response['main']['humidity'],            
            'Latitude' : response['coord']['lat'],
            'Longitude' : response['coord']['lon'],
			}
    return render(request, 'update.html', context={'info1':test}) 

@csrf_exempt
def multi(request):
    return render(request, 'weather.html')

