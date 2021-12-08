from django.shortcuts import render


def cateringPageView(request):
    return render(request, 'catering/catering.html')

def editCateringPageView(request):
   return render(request, 'catering/editCatering.html')

