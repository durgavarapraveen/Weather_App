from django.shortcuts import render
import json
import urllib.request
from .models import weather

# Create your views here.

def index(request):

    cities = ['Delhi', 'Dubai', 'Texas','Sydney']

    weather_app = []


    for city in cities:
        api_key = 'd39e0397b540a1719f49547334a60299'
        url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + api_key
        res = urllib.request.urlopen(url).read()
        json_data = json.loads(res)

        data_json = json.loads(res)
        data1 = {
            'city' : city,
            'temp' : str(data_json['main']['temp']) + 'k',
            'pressure' : str(data_json['main']['pressure']) + 'pa',
            'humidity' : str(json_data['main']['humidity']) + '%',
        }
        weather_app.append(data1)
    print(weather_app)
    print(weather_app[0])


    if request.method == 'POST':
        city = request.POST['city']
        # res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'appid=d39e0397b540a1719f49547334a60299').read()

        api_key = 'd39e0397b540a1719f49547334a60299'
        url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + api_key

        res = urllib.request.urlopen(url).read()

        json_data = json.loads(res)
        data = {
            'city' : city,
            'country_code' : str(json_data['sys']['country']),
            'coordinate' : str(json_data['coord']['lon']) + ' '+ str(json_data['coord']['lat']),
            'temp' : str(json_data['main']['temp']) + 'k',
            'feels_like' : str(json_data['main']['feels_like']) + 'k',
            'temp_min' : str(json_data['main']['temp_min']) + 'K',
            'temp_max' : str(json_data['main']['temp_max']) + 'k',
            'pressure' : str(json_data['main']['pressure'])+ 'hPa',
            'humidity' : str(json_data['main']['humidity'])+ '%',
            'wind_speed' : str(json_data['wind']['speed'])+ 'm/s',
            'sun_rise' : str(json_data['sys']['sunrise']) + 'unix',
            'sun_set' : str(json_data['sys']['sunset'])+ 'unix',
        }

        return render(request, 'index.html', {'data': data, 'weather_app':weather_app})
    
    return render(request, 'index.html', {'weather_app': weather_app})



        

    