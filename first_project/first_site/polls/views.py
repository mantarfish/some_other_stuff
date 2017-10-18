from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, World. why is this funtion called index/nthis views.index")

def view2(request):
    return HttpResponse('views.view2')
