from django.db import models
from django.db.models.fields import DateTimeField


class Menu_Item(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField
    photo_main = models.ImageField(upload_to='photos')    

    class Meta:
        db_table = "menu_item"

    def __str__(self):
        return (self.name)

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=13, blank=True)

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def __str__(self):
        return (self.full_name)

class Catering_Event(models.Model):
    event_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    zip = models.CharField(max_length=15)
    datetime = models.DateTimeField
    cost = models.FloatField
    customerID = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    menu_items = models.ManyToManyField(Menu_Item, blank=True)

    def __str__(self):
        return (self.event_name)








    