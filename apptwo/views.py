from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def djangorocks(request):

    return HttpResponse("C\est django, Django!")

def picturedetails(request, category, year=0, month=0):
    body = "Category={}, Year={}, Month={}".format(category, year, month)
    return HttpResponse(body)

def index(request):
    return HttpResponse("Hello, world!")
