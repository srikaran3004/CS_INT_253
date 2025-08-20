from django.shortcuts import render
from django.http import HttpResponse

def handler404(request,exception):
    return HttpResponse("<h1>Dear user the page you are loading doesn't exist</h1>",status=404)

