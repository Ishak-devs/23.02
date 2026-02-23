from django.shortcuts import render

# Create your views here.
def djangorocks(request):

    return HttpResponse("C\est django, Django!")

def picturedetails(response, category):
    body = f"Voici les détails de l'image dans la catégorie {category}."
    return HttpResponse(body)
