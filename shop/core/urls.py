from django.urls import path
from . import views

urlpatterns = [
    path(route="catalog", view=views.catalog, name="core-catalog"),
    path(route="", view=views.home, name="core-home"),
]