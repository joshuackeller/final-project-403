from django.http import HttpResponse


def cateringPageView(request):
    return(HttpResponse('Catering page view'))

def editCateringPageView(request):
    return(HttpResponse('Edit catering page view'))

