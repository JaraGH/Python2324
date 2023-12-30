from django.http import request, HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView

from sports.forms import SportForm
from sports.models import Sport


# Create your views here.

class SportListView(ListView):
    model = Sport
    template_name = 'sport_list.html'
    context_object_name = 'sports'





# class SportListView(View):
#
#     def get(self, request):
#         sports = Sport.objects.all()
#         return render(request,
#                       'sport_list.html',
#                       {'sports': sports})


### para forms.ModelForm

class SportCreateView(CreateView):
    model = Sport
    form_class = SportForm
    template_name = 'sport_form.html'
    success_url = '/sports/list/'

class SportUpdateView(UpdateView):
    model = Sport
    form_class = SportForm
    template_name = 'sport_form.html'
    success_url = '/sports/list/'


# class SportCreateView(View):
#
#     def get(self, request):
#
#         form = SportForm()
#         return render(request,
#                       'sport_form.html',
#                       {'form': form})
#
#     def post(self, request):
#
#         form = SportForm(request.POST, request.FILES)
#         if form.is_valid():
#             sport = Sport()
#             sport.name = form.cleaned_data['name']
#             sport.description = form.cleaned_data['description']
#             sport.is_outdoor = form.cleaned_data['is_outdoor']
#             sport.number_players = form.cleaned_data['number_players']
#             sport.type = form.cleaned_data['type']
#             sport.origin = form.cleaned_data['origin']
#             sport.image = form.cleaned_data['image']
#             sport.save()
#             return HttpResponse('Sport created')
#         return render(request,
#                       'sport_form.html',
#                       {'form': form})






### para forms.Form
# class SportCreateView(View):
#
#     def get(self, request):
#         form = SportForm()
#         return render(request,
#                       'sport_form.html',
#                       {'form': form})
#
#     def post(self, request):
#         form = SportForm(request.POST, request.FILES)
#         if form.is_valid():
#             sport = Sport()
#             sport.name = form.cleaned_data['name']
#             sport.description = form.cleaned_data['description']
#             sport.is_outdoor = form.cleaned_data['is_outdoor']
#             sport.number_players = form.cleaned_data['number_players']
#             sport.type = form.cleaned_data['type']
#             sport.origin = form.cleaned_data['origin']
#             sport.image = form.cleaned_data['image']
#             sport.save()
#             return HttpResponse('Sport created')
#         return render(request,
#                       'sport_form.html',
#                       {'form': form})