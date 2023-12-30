from django.urls import path


from cities import views

urlpatterns = [
    path("all/", views.all, name="all"),
    path("top5/", views.top5, name="top5"),
    path("spain/", views.spain, name="spain"),
    path('country/<str:country_name>/', views.country_cities),
    path('id/<int:id>/', views.cities_id)

]