from django.contrib.auth.decorators import login_required
from django.urls import path

from bikes.views import BikeListView, BikeDetailView, BikesTop5ByPrice, BikeUpdateView, BikeFilterByBrand, \
    BikeCreateView

urlpatterns = [
    path('list/', login_required(BikeListView.as_view()), name="list-all"),
    path('top5/', BikesTop5ByPrice.as_view(), name="list-top5"),
    path('detail/<int:id>', BikeDetailView.as_view(),  name="bike-detail"),
    path('edit/<int:pk>', BikeUpdateView.as_view(),  name="bike-edit"),
    path('list/brand/<str:brand>', BikeFilterByBrand.as_view(),  name="filter-by-brand"),
    path('new/', BikeCreateView.as_view(),  name="bike-create"),



]