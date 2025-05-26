from datetime import datetime, timedelta, timezone
import openmeteo_requests
import pandas as pd
import requests_cache
from retry_requests import retry
import requests
import numpy as np

def get_weather_data(city_name):
    geocoding_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1&language=en&format=json"
    geo_response = requests.get(geocoding_url)
    if geo_response.status_code != 200:
        return {"error": "Ошибка получения координат"}

    geo_data = geo_response.json()
    if not geo_data.get("results"):
        return {"error": "Город не найден"}

    latitude = geo_data["results"][0]["latitude"]
    longitude = geo_data["results"][0]["longitude"]

    cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
    retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
    openmeteo = openmeteo_requests.Client(session=retry_session)

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m",
        "forecast_days": 1
    }

    try:
        responses = openmeteo.weather_api(url, params=params)
        response = responses[0]

        hourly = response.Hourly()
        hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
        times_raw = hourly.Time()

        start_time = datetime.fromtimestamp(times_raw, tz=timezone.utc)
        times = [start_time + timedelta(hours=i) for i in range(len(hourly_temperature_2m))]

        hourly_data = []
        for i, t in enumerate(times):
            temp = hourly_temperature_2m[i]
            hourly_data.append({
                "time": t.strftime("%H:%M"),
                "temperature": round(float(temp), 1)
            })

        return {
            "city": city_name,
            "latitude": latitude,
            "longitude": longitude,
            "hourly_data": hourly_data
        }

    except Exception as e:
        return {"error": str(e)}
