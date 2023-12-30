from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
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
        return render(request, 'create-country.html',
                      context={
                          'form': CountryForm()
                      })

    def post(self, request):
        form = CountryForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(to='all-countries')



class DeleteCountryView(View):

    def get(self, request, id):
        obj = get_object_or_404(Country, id=id)
        obj.delete()
        return redirect(to='all-countries')

###################################################################

def updateView(request, id):
    obj = Country.objects.get(id=id)
    form = CountryForm(instance=obj)
    if request.method == 'POST':
        form = CountryForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('all-countries')
    template_name = 'update-country'
    context = {'form': form}
    return render(request, template_name, context)


#class UpdateCountryView(View):


# def edit(request, id):
#     print("Edit")
#     country = Country.objects.get(id__exact=id)
#     template = loader.get_template('update-country.html')
#     context = {
#         'date': datetime.now(),
#         'form': CountryForm(instance=country),
#         'title': 'Edit country:  ' + country.name + str(country.id)
#     }
#     return HttpResponse(template.render(context, request))
#
# def update(request):
#
#     form = CountryForm(request.POST)
#
#     #country = Country.objects.get(id=form.id)
#     if request.method == 'POST':
#         if form.is_valid:
#
#             form.save()
#             return redirect(to='all-countries')
#     template = loader.get_template('update-country.html')
#     context = {
#         'date': datetime.now(),
#         'form': form,
#         'title': 'Edit country:  ' + form.name
#     }
#
#     return render(request, template, context)





# render(request, "create-country.html", context)def edit(self, request, id):
#     obj = Country.objects.filter(id=id)
#     if obj:
#         return render(request, 'create-country.html',
#                       context={
#                           'form': CountryForm(request.POST)
#                       })
#     else:
#         return redirect(to='all-countries')
#
# def post(self, request):
#
#         context = {}
#         obj = get_object_or_404(Country, id=id)
#
#         # pass the object as instance in form
#         form = CountryForm(request.POST or None, instance=obj)
#
#         if form.is_valid():
#             form.save()
#             return redirect(to='all-countries')
#
#         context["form"] = form
#         return