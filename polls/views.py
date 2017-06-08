from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from math import sqrt


def index(request):
    return HttpResponse("Fibnonci of 10 using <br> Normal Approach:"+fibnonci_normal(10)+"  <br> Easy Formula Approach"+fibnonci_easy(10))


def fibnonci_normal(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return fibnonci_normal(n-1)+fibnonci_normal(n-2)

def fibnonci_easy(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))