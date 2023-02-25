from django.http import HttpResponse

from siteapps.mt5_license import app


def home(request):
    return HttpResponse("AltoInvest")


