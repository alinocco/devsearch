from django.shortcuts import render
from django.http import HttpResponse


def projects(request):
    return HttpResponse("Hi")


def project(request, pk):
    return HttpResponse("Hello" + " " + str(pk))
