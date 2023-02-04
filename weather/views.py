from django.shortcuts import render,HttpResponse
import json
import urllib.request
from weather.models import Contact

# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=ded956a99e83cfa92e3509a573a6b09c').read()
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
    context = {'success':False}
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')

        data = Contact(name=name,email=email,phone=phone,desc=desc)
        data.save()
        context={'success':True}
    return render(request,'contact.html',context)