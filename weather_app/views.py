# weather_app/views.py

from django.shortcuts import render
from django.http import JsonResponse
from .models import SearchHistory
from .weather_fetcher import get_weather_data

def home(request):
    city = request.GET.get('city', '')
    forecast = None
    error = None
    hourly_data = None

    response = None

    if city:
        obj, created = SearchHistory.objects.get_or_create(city=city)
        if not created:
            obj.count += 1
            obj.save()

        weather_data = get_weather_data(city)
        if "error" in weather_data:
            error = weather_data["error"]
        else:
            forecast = {
                "latitude": weather_data["latitude"],
                "longitude": weather_data["longitude"]
            }
            hourly_data = weather_data["hourly_data"]

        response = render(request, 'home.html', {
            'city': city,
            'forecast': forecast,
            'hourly_data': hourly_data,
            'error': error,
            'last_city': city
        })
        response.set_cookie('last_city', city, max_age=3600*24*7)
        return response

    last_city = request.COOKIES.get('last_city')

    return render(request, 'home.html', {
        'city': '',
        'forecast': forecast,
        'hourly_data': hourly_data,
        'error': error,
        'last_city': last_city
    })

def api_city_stats(request):
    data = list(SearchHistory.objects.values('city', 'count'))
    return JsonResponse(data, safe=False)
