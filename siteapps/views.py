from django.http import HttpResponse, JsonResponse

from .mt5 import mt5


def mt5_view(request):
    return mt5(request)


def home(request):
    return HttpResponse("AltoInvest")


