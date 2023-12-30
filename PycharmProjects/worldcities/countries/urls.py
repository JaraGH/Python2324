from django.urls import path

from countries import views
from countries.views import AllCountriesView, EuropeCountriesView, NewCountryView, DeleteCountryView

urlpatterns = [
    path("all/", AllCountriesView.as_view(), name="all-countries"),
    path("europe/", EuropeCountriesView.as_view()),
    path("new/", NewCountryView.as_view()),
    path("add/", NewCountryView.as_view(), name="create-country"),
    path("delete/<int:id>", DeleteCountryView.as_view(), name="delete-country"),

    #path("update/", views.update, name="update-country"),
    path("edit/<int:id>", views.updateView, name="edit-country"),
]