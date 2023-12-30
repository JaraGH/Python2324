from django.urls import path

from sports.views import SportListView, SportCreateView, SportUpdateView

urlpatterns = [
    path('list/', SportListView.as_view(), name='sport_list'),
    path('new/', SportCreateView.as_view(), name='sport_list'),
    path('update/<int:pk>', SportUpdateView.as_view(), name='sport_list'),
    path('new/', SportCreateView.as_view(), name='sport_list'),

]