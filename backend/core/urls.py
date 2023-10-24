from django.contrib import admin
from django.urls import path, include, re_path
from .views import RecicleMaterialsView

urlpatterns = [path("recicle-materials/", RecicleMaterialsView.as_view())]
