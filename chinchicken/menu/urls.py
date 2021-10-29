from django.urls import path
from .views import indexPageView, menuPageView, editMenuPageView

urlpatterns = [
    path("", indexPageView, name="index"), 
    path("menu/", menuPageView, name="menu"), 
    path("edit_menu/", editMenuPageView, name="edit_menu"), 
] 