from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("<h1>Welcome to my first website!</h1>")
