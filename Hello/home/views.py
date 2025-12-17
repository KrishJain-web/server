from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')
def about(request):
    return HttpResponse("tell me about")
def services(request):
    return HttpResponse("services")