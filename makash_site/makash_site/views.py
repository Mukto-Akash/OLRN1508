# mysite/views.py

from django.http import HttpResponse


def index(request):
    return HttpResponse('CG-OLRN1508-Assignment-1 <br> Mukto Akash')