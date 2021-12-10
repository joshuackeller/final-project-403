from django.urls import path

from catering.views import addCateringPageView


from .views import addMenuItemPageView, deleteMenuItemPageView, indexPageView, menuPageView, editMenuItemPageView, searchMenuItem, singleMenuItemPageView, aboutPageView

urlpatterns = [
    path("", indexPageView, name="index"), 
    path("about/", aboutPageView, name="about"),
    path("menu/", menuPageView, name="menu"), 
    path("editMenu/<id>/", editMenuItemPageView, name="editMenuItem"), 
    path("singleMenuItem/<id>/", singleMenuItemPageView, name="singleMenuItem"),
    path("searchMenuItem/",searchMenuItem, name="searchMenuItem"),
    path("deleteMenuItem/<id>/", deleteMenuItemPageView, name="deleteMenuItem"),
    path("addMenuItem/", addMenuItemPageView, name="addMenuItem"),
] 