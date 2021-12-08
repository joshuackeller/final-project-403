from django.contrib import admin

from .models import Customer, Menu_Item, Catering_Event

admin.site.register(Customer)
admin.site.register(Menu_Item)
admin.site.register(Catering_Event)
