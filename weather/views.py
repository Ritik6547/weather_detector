from django.shortcuts import render,HttpResponse
import json
import urllib.request

# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=f3bb95d267d0d2ffc0ea0a0a5732e408').read()
        json_data = json.loads(res)
        data = {
            "city": city,
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + '' + str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp'])+'k',
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
        }

    else:
        data = {}

        
    return render(request,'index.html',data)

def contact(request):
    return render(request,'contact.html')