# mysite/views.py
""" A simple view to demostrate django.
"""
from django.http import HttpResponse


def index(request):
    """ Returns the text for the webpage
    """
    return HttpResponse('CG-OLRN1508-Assignment-1 <br> Mukto Akash')
