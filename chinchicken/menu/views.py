from django.http import HttpResponse
from django.shortcuts import render

def indexPageView(request):
    return render(request, "menu/index.html")

def menuPageView(request):
    return render(request, "menu/menu.html")

def editMenuPageView(request):
    return render(request, "menu/editMenu.html")