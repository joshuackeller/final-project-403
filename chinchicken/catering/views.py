from django.shortcuts import render
from menu.models import Menu_Item, Customer, Catering_Event

def cateringPageView(request):
    if request.method == 'POST':
        sEvent_name = request.POST['event_name']
        sAddress = request.POST['address']
        sCity = request.POST['city']
        sState = request.POST['state']
        sZip = request.POST['zip']
        dDatetime = request.POST['datetime']
        sCost = request.POST['cost']
        events = Catering_Event.objects.filter(event_name = sEvent_name).filter(address = sAddress).filter(city = sCity).filter(state = sState).filter(zip = sZip).filter(datetime = dDatetime).filter(Cost = sCost)
        context = {
            'events': events
        }
    else:
        events = Catering_Event.objects.all()
        context = {
            'events': events
        }
    return render(request, 'catering/catering.html', context)

def singleCateringPageView(request, id):
    event = Catering_Event.objects.get(id=id)

    context = {
        "event": event
    }

    return render(request, "menu/singleCatering.html", context)

def editCateringPageView(request):
    if request.method == 'POST':
        cust_id = request.POST['cust_id']
        event = Catering_Event.object.get(id=cust_id)
        event.event_name = request.POST['event_name']
        event.address = request.POST['address']
        event.city = request.POST['city']
        event.state = request.POST['state']
        event.zip = request.POST['zip']
        event.datetime = request.POST['datetime']
        event.cost = request.POST['cost']
        event.save()
        return cateringPageView(request)
    else:
        data = Catering_Event.objects.get(id = id)
        context = {
        'record': data
        }
        return render(request, 'catering/editCatering.html',context)

def deleteCateringPageView(request,cust_id):
    data = Catering_Event.objects.get(id = cust_id)
    data.delete()
    return cateringPageView(request)

def addCateringPageView(request):
    if request.method == 'POST':
        event = Catering_Event()
        event.event_name = request.POST['event_name']
        event.address = request.POST['address']
        event.city = request.POST['city']
        event.state = request.POST['state']
        event.zip = request.POST['zip']
        event.datetime = request.POST['datetime']
        event.cost = request.POST['cost']
        event.save()
        return cateringPageView(request)
    else:
        return render(request, 'catering/addCatering.html')
        