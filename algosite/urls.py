from django.urls import include, path

urlpatterns = [
    path('', include('siteapps.urls')),
]

