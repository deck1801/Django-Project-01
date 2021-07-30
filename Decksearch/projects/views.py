from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def projects(request):
    return HttpResponse("Checking........")


def project(request, pk):
    return HttpResponse("Project Page:" + str(pk))
