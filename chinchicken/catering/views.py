from django.shortcuts import render
from menu.models import Menu_Item, Customer, Catering_Event

def cateringPageView(request):
    if request.method == 'POST':
        eventName = request.POST['eventName']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        zipcode = request.POST['zipcode']
        datetime = request.POST['datetime']
        customer = request.POST['customer']
        cost = request.POST['cost']
        if customer == "none":
            events = Catering_Event.objects.filter(event_name__icontains=eventName).filter(address__icontains =address).filter(city__icontains =city).filter(state__icontains=state).filter(zip__icontains =zipcode).filter(datetime__icontains=datetime).filter(cost__icontains = cost)
        else:
            events = Catering_Event.objects.filter(event_name__icontains=eventName).filter(address__icontains =address).filter(city__icontains =city).filter(state__icontains=state).filter(zip__icontains =zipcode).filter(datetime__icontains=datetime).filter(cost__icontains = cost).filter(customerID=customer)
        customers = Customer.objects.all()
        context = {
            'events': events,
             'customers': customers,
        }
    else:
        events = Catering_Event.objects.all()
        customers = Customer.objects.all()
        context = {
            'events': events,
            'customers': customers,
        }
    return render(request, 'catering/catering.html', context)



def singleCateringPageView(request, id):

    event = Catering_Event.objects.get(id=id)
    availableMenuItems = Menu_Item.objects.exclude(id__in=event.menu_items.all())
    context = {
        "event": event,
        "menuItems": availableMenuItems
    }

    return render(request, "catering/singleCatering.html", context)

def editCateringPageView(request, id):
    if request.method == 'POST':
        event = Catering_Event()
        event.event_name = request.POST['eventName']
        event.address = request.POST['address']
        event.city = request.POST['city']
        event.state = request.POST['state']
        event.zip = request.POST['zipcode']
        event.datetime = request.POST['datetime']
        event.customerID = Customer.objects.get(id=request.POST['customer'])
        event.cost = request.POST['cost']
        event.save()

        events = Catering_Event.objects.all()
        customers = Customer.objects.all()
        context = {
            'events': events,
            'customers': customers,
        }
        return render(request, 'catering/catering.html', context)
    else:
        event = Catering_Event.objects.get(id = id)
        customers = Customer.objects.all()
        context = {
            'event': event,
            'customers': customers,
        }
        return render(request, 'catering/editCatering.html',context)

def deleteCateringPageView(request,id):
    data = Catering_Event.objects.get(id = id)
    data.delete()
    return cateringPageView(request)

def addCateringPageView(request):
    if request.method == 'POST':
        event = Catering_Event()
        event.event_name = request.POST['eventName']
        event.address = request.POST['address']
        event.city = request.POST['city']
        event.state = request.POST['state']
        event.zip = request.POST['zipcode']
        event.datetime = request.POST['datetime']
        event.cost = request.POST['cost']
        event.customerID = Customer.objects.get(id=request.POST['customer'])
        event.save()
        events = Catering_Event.objects.all()
        customers = Customer.objects.all()
        context = {
            'events': events,
            'customers': customers,
        }
        return render(request, 'catering/catering.html', context)
    else:
        customers = Customer.objects.all()
        context = {"customers":customers}
        return render(request, 'catering/addCatering.html',context)

def addEventMenuItemsPageView(request, id):
    if request.method == 'POST':
        event = Catering_Event.objects.get(id=id)
        event.menu_items.add(Menu_Item.objects.get(id=request.POST['menuItem']))
        event.save()
        availableMenuItems = Menu_Item.objects.exclude(id__in=event.menu_items.all())

        context = {
            "event": event,
            "menuItems": availableMenuItems
        }

        return render(request, "catering/singleCatering.html", context)

def removeEventMenuItemPageView(request, eventId, menuItemId):
    event = Catering_Event.objects.get(id=eventId)
    event.menu_items.remove(Menu_Item.objects.get(id=menuItemId))
    event.save()
    availableMenuItems = Menu_Item.objects.exclude(id__in=event.menu_items.all())
    context = {
            "event": event,
            "menuItems": availableMenuItems
        }

    return render(request, "catering/singleCatering.html", context)

        