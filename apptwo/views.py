from django.shortcuts import render

# Create your views here.
def djangorocks(request):

    return HttpResponse("C\est django, Django!")

def picturedetails(request, category):
    body = "Category={}".format(category)
        return HttpResponse(body)
