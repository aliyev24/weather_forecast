import requests

def get_forecast(cities):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=3473651768de5e545f7d20a5187dc1fd'
    forecast_data = []
    for city in cities:
        city_weather = requests.get(url.format(city)).json()
        weather = {
            'city': city,
            'temperature': city_weather['main']['temp'],
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon']
        }
        forecast_data.append(weather)
    return forecast_data