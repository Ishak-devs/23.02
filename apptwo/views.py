from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def djangorocks(request):

    return HttpResponse("C\est django, Django!")

def picturedetails(request, category):
    body = "Category={}".format(category)
    return HttpResponse(body)

def index(request):
    return HttpResponse("Hello, world!")
