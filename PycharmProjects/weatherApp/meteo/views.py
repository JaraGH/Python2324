from datetime import datetime

import geocoder
import requests
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def temp_here(request):
    endpoint = "https://api.open-meteo.com/v1/forecast"
    location = geocoder.ip('me').latlng
    api_request = f"{endpoint}?latitude={location[0]}&longitude={location[1]}&hourly=temperature_2m"
    now = datetime.now()
    hour = now.hour
    meteo_data = requests.get(api_request).json()
    temp = meteo_data['hourly']['temperature_2m'][hour]
    return HttpResponse(f"Here is temp {temp} degress")


def saludo(request):
    return HttpResponse(f"Hola desde Django")
