from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .forms import ImageForm

from menu.models import Menu_Item

def indexPageView(request):
    return render(request, "menu/index.html")

def aboutPageView(request):
    return render(request, "menu/about.html")

def menuPageView(request):
    menu_items = Menu_Item.objects.all()

    context = {
        "menu_items": menu_items
    }

    return render(request, "menu/menu.html", context)

def singleMenuItemPageView(request, id):
    item = Menu_Item.objects.get(id=id)

    context = {
        "item": item
    }

    return render(request, "menu/singleMenuItem.html", context)

# def editMenuItemPageView(request, id):

#     if request.method == "POST":
#         item = Menu_Item.objects.get(id=id)
#         item.name = request.POST['itemName']
#         item.price = request.POST['itemPrice']
#         item.photo_main = request.POST['itemImage']

#         item.save()

#         context = {
#             "item":item
#         }

#         return render(request, "menu/singleMenuItem.html", context)

#     else:
#         item = Menu_Item.objects.get(id=id)

#         context = {
#             "item":item
#         }

#         return render(request, "menu/editMenuItem.html", context)

def editMenuItemPageView(request,id):
    menuItem = Menu_Item.objects.get(id=id)
    form = ImageForm(instance=menuItem)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            menu_items = Menu_Item.objects.all()

            context = {
                "menu_items": menu_items,
                'form': form,
                'img_obj': img_obj
            }
            return render(request, 'menu/menu.html', context)
    else:
        form = ImageForm(instance=menuItem)

    return render(request, 'menu/editMenu.html', {'form': form})



def searchMenuItem(request):
    if request.method == "POST":
        itemName = request.POST['itemName']

        menu_items = Menu_Item.objects.filter(name__icontains=itemName)

        context = {
            "menu_items": menu_items
        }

        return render(request, "menu/menu.html", context)
    
    else:
        menu_items = Menu_Item.objects.all()

        context = {
            "menu_items": menu_items
        }

        return render(request, "menu/menu.html", context)

def deleteMenuItemPageView(request, id):
    menu_item = Menu_Item.objects.get(id=id)

    menu_item.delete()

    return searchMenuItem(request)

# def addMenuItemPageView(request):
#     if request.method == "POST":
#         item = Menu_Item()
#         item.name = request.POST['itemName']
#         item.price = request.POST['itemPrice']
#         item.photo_main = request.POST['itemImage']
#         item.save()
        

#         menu_items = Menu_Item.objects.all()

#         context = {
#             "menu_items": menu_items
#         }

#         return render(request, "menu/menu.html", context)

#     else:
#         return render(request, "menu/addMenuItem.html")


def addMenuItemPageView(request):

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            menu_items = Menu_Item.objects.all()

            context = {
                "menu_items": menu_items,
                'form': form,
                'img_obj': img_obj
            }
            return render(request, 'menu/menu.html', context)
    else:
        form = ImageForm()

    return render(request, 'menu/addMenuItem.html', {'form': form})