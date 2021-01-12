#region             -----External Imports-----
from django.urls import path
#endregion

#region             -----Internal Imports-----
from . import views
#endregion

urlpatterns = [
    path(route="catalog/", view=views.catalog, name="core-catalog"),
    path(route="catalog/<slug:slug>", view=views.product),
    path(route="", view=views.home, name="core-home"),
]