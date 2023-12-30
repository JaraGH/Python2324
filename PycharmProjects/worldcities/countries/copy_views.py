from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.views import View
from django.forms import formset_factory
from countries.forms import CountryForm
from countries.models import Country


# Create your views here.

class EuropeCountriesView(View):

    def get(self, request):
        context = {
            'date': datetime.now(),
            'title': 'Europe countries',
            'countries': Country.objects.filter(continent='Europe'),
        }
        return render(request, 'list-countries.html',
                      context=context)


class AllCountriesView(View):

    def get(self, request):
        context = {
            'date': datetime.now(),
            'title': 'All countries',
            'countries': Country.objects.all(),
        }
        return render(request, 'list-countries.html',
                      context=context)



class NewCountryView(View):

    def get(self, request):
        template = loader.get_template('create-country.html')
        # context = {
        #     'date': datetime.now(),
        #     'title': 'Add new country',
        #     'form': CountryForm(),
        # }
        return render(request, 'create-country.html',
                      context={
                          'form': formset_factory(CountryForm)
                      })

    def post(self, request):
        formset = formset_factory(CountryForm)
        formset = formset(data=request.POST)

        if formset.is_valid():
            for form in formset:
                if form.has_changed():
                    form.save()
            return redirect(to='all-countries')

        else:
            return render(request, 'create_book.html',
                          context={'forms': formset})



