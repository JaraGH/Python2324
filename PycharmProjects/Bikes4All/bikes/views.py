from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from bikes.forms import BikeForm
from bikes.models import UsedBikes


# Create your views here.

### class based views

class BikeCreateView(View):
    model = UsedBikes
    form_class = BikeForm
    template_name = 'bike_edit.html'
    success_url = reverse_lazy('list-all')



class BikeListView(View):

    def get(self, request):
        bikes = UsedBikes.objects.all().only('id', 'brand', 'age', 'bike_name', 'city', 'price')[:10]
        context = {
            'message': 'List of bikes',
            'bikes': bikes,
        }
        return HttpResponse(render(request, template_name="bikes_list.html", context=context))
        #return render(request, template_name="bikes_list.html", context=context)


class BikeFilterByBrand(View):

    def get(self, request, brand):
        bikes = UsedBikes.objects\
            .filter(brand=brand).only('id', 'brand', 'age', 'bike_name', 'city', 'price')[:10]
        context = {
            'message': 'List of bikes: ' + brand,
            'bikes': bikes,
        }
        return HttpResponse(render(request, template_name="bikes_list.html", context=context))


class BikeDetailView(View):

    def get(self, request, id):
        bike = UsedBikes.objects.filter(id=id).values().first()
        context = {
            'bike': bike,
            'id': bike['id'],
        }
        return HttpResponse(render(request, template_name="bike_detail.html", context=context))


class BikeUpdateView(UpdateView):
    model = UsedBikes
    form_class = BikeForm
    template_name = 'bike_edit.html'
    success_url = reverse_lazy('list-all')



class BikesTop5ByPrice(View):

    def get(self, request):
        bikes = UsedBikes.objects.only('id', 'brand', 'age', 'bike_name', 'city', 'price').order_by('-price')[:5]
        context = {
            'bikes': bikes,
        }
        return HttpResponse(render(request, template_name="bikes_list.html", context=context))


# @login_required
# def list_all(request):
#     context = {
#         'Ipcliente': request.META.get('REMOTE_ADDR'),
#         'Path': request.build_absolute_uri(),
#         'Method': request.method,
#         'ServerPort': request.META.get('SERVER_PORT'),
#     }
#     return render(request, template_name="list-bikes.html",
#                   context=context);

#
# def bike_detail_view(request, id):
#     context = {
#         'id':id,
#     }
#     return render(request, template_name="detail-bike.html",
#                   context=context);
#
#
# def bike_sold(request, mes, anio):
#     context = {
#         'mes': mes,
#         'anio': anio,
#     }
#     return render(request, template_name="bikes-sold.html",
#                   context=context);
#
# def bike_sold_get(request):
#     context = {
#         'dict': request.GET,
#         'valor': request.GET.get('valor')
#     }
#     return render(request, template_name="bikes-sold-get.html",
#                   context=context);
#
#
# def bike_new(request):
#
#     if request.method=='POST':
#         context = {
#             'name': request.POST['name'],
#             'precio': request.POST['precio']
#
#         }
#         return render(request, template_name="bikes-post-add.html",
#                       context=context)
#     else:
#         return render(request, template_name="new-bike.html")