from django.shortcuts import render
import requests
from . import models
# Create your views here.


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=3473651768de5e545f7d20a5187dc1fd'
    forecast_data = []
    cities = models.Region.objects.all().order_by('-id')[:5]
    for city in cities:
        city_weather = requests.get(url.format(city)).json()
        weather = {
            'city': city,
            'temperature': city_weather['main']['temp'],
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon']
        }
        forecast_data.append(weather)
    context = {'forecast_data': forecast_data}
    return render(request, 'core/index.html', context)
