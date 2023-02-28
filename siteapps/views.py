from django.http import HttpResponse
from django.shortcuts import render

from .mt5 import mt5


# Direciona para o APP de validação de licença do EA no MT5
def mt5_view(request):
    return mt5(request)


def home(request):
    return render(request, 'pages/home.html')


