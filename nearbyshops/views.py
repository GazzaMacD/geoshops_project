from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from django.shortcuts import render
from django.views import generic

from nearbyshops.models import Shop

latitude = 39.290440
longitude = -76.612330

user_location = Point(longitude, latitude, srid=4326)


class Home(generic.ListView):
    model = Shop
    context_object_name = "shops"
    queryset = Shop.objects.annotate(
        distance=Distance("location", user_location)
    ).order_by("distance")[0:6]
    print(queryset)
    template_name = "index.html"
