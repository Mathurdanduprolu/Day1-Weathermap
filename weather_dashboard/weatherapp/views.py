from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
#from .weather_service import get_weather_data 
from weatherapp.weather_service import get_weather_data

def weather_view(request):
    weather_data = None
    error_message = None
    background_color = "#FFFFFF"  # Default white background
    
    if request.method == 'POST':
        city = request.POST.get('city', '')
        weather_data = get_weather_data(city)
        
        if "error" in weather_data:
            error_message = weather_data["error"]
        else:
            # Set background color based on temperature
            temp = weather_data['main']['temp']
            if temp < 10:
                background_color = "#E6F3FF"  # Cool blue for cold
            elif 10 <= temp < 20:
                background_color = "#FFFDE7"  # Light yellow for mild
            else:
                background_color = "#FFF3E0"  # Light orange for warm
    
    context = {
        'weather': weather_data,
        'error_message': error_message,
        'background_color': background_color
    }
    return render(request, 'weather.html', context)
