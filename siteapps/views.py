import subprocess

from django.http import HttpResponse


def home(request):
    return HttpResponse("AltoInvest")

def run_app(request):
    subprocess.Popen(['python', 'app.py'])
    return HttpResponse('Python app has been started!')
