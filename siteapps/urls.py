from django.urls import path

from siteapps.mt5_license import app
from siteapps.views import home

urlpatterns = [
    path('', home),  # Home   
    path('mt5/', app) 
]