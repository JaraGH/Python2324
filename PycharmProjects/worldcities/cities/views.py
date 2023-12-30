from django.http import HttpResponse
from django.template import loader
from datetime import datetime
from cities.models import Worldcities


# Create your views here.

def my_custom_404_view(request, exception):
    template = loader.get_template('404.html')
    context = {
        'date': datetime.now(),
        'title': 'Page not found'
    }
    return HttpResponse(template.render(context, request))

def all(request):
    cities = Worldcities.objects.all().values()
    template = loader.get_template('list_cities.html')
    context = {
        'date': datetime.now(),
        'cities': cities,
        'title': 'All cities in database'
    }
    return HttpResponse(template.render(context, request))


def country_cities(request, country_name):
    cities = Worldcities.objects.all().filter(country=country_name)
    template = loader.get_template('list_cities.html')
    context = {
        'date': datetime.now(),
        'cities': cities,
        'title': 'Cities of ' + country_name
    }
    return HttpResponse(template.render(context, request))


def spain(request):
    cities = Worldcities.objects.filter(country='Spain')
    template = loader.get_template('list_cities.html')
    context = {
        'date': datetime.now(),
        'cities': cities,
        'title': 'Cities of Spain'
    }
    return HttpResponse(template.render(context, request))

def top5(request):
    cities = Worldcities.objects.order_by('-population')[0:5]
    template = loader.get_template('list_cities.html')
    context = {
        'date': datetime.now(),
        'cities': cities,
        'title': 'Top 5 population'
    }
    return HttpResponse(template.render(context, request))


def cities_id(request, id):
    city = Worldcities.objects.get(id__exact=id)
    template = loader.get_template('show_city_detail.html')
    context = {
        'date': datetime.now(),
        'city': city,
        'title': 'City detail' + str(city.city)
    }
    return HttpResponse(template.render(context, request))
