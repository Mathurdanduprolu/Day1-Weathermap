from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .weather_service import get_weather_data 
from weatherapp.weather_service import get_weather_data

def weather_view(request):
    weather_data = None
    
    if request.method == 'POST':
        city = request.POST.get('city', '')
        weather_data = get_weather_data(city)
    
    return render(request, 'weather.html', {'weather': weather_data})

