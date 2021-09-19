from django.shortcuts import render
from . import models
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import requests
import datetime
import time
from datetime import datetime, timedelta, time

@csrf_exempt
def test(request):
    city=request.POST.get('city')
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=f8a5d735b096ea2ac24b60c551dca284'
    response = requests.get(url.format(city)).json()
    if response:
        rse = int((response['main']['temp'])/3.4)
        tempe = (rse-32) * 5//9 
        speed = response['wind']['speed']

        rise = (response['sys']['sunrise'])
        ts = datetime.fromtimestamp(rise).strftime('%Y-%m-%d %H:%M:%S')
        date_time_obj = datetime.strptime(ts, '%Y-%m-%d %H:%M:%S').strftime("%I:%M %p")

        sset = (response['sys']['sunset'])
        sts = datetime.fromtimestamp(sset).strftime('%Y-%m-%d %H:%M:%S')
        s_date_time_obj = datetime.strptime(sts, '%Y-%m-%d %H:%M:%S').strftime("%I:%M %p")

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
                'sunrise' : date_time_obj,
                'sunset' : s_date_time_obj,
    			}
        return render(request, 'update.html', {'info1':test}) 
    else:
        return render(request, 'update.html', {'info':"Invalid API key"}) 

@csrf_exempt
def index(request):
    return render(request, 'weather.html')


