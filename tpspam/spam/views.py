from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("spam 전화번호")
