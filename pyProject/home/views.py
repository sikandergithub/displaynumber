from django.http import HttpResponse
from django.shortcuts import render  ,HttpResponse


# Create your views here.
# def home(request):
#     return  HttpResponse("This is the data")

def home(request):
    context = {'name':'Python','course':'Django'}
    return render(request,'home.html',context)

def about(request):
    return render(request,'about.html')


def projects(request):
    return render(request,'projects.html')

def contact(request):
    return render(request,'contact.html')

def DisplayNumber(request):
    return render(request,'DisplayNumber.html')        