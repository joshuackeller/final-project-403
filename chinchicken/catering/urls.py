from django.urls import path
from .views import addEventMenuItemsPageView, cateringPageView, deleteCateringPageView, editCateringPageView, addCateringPageView, removeEventMenuItemPageView, singleCateringPageView

urlpatterns = [
    path("catering/", cateringPageView, name="catering"), 
    path("editCatering/<id>/", editCateringPageView, name="editCatering"), 
    path("addCatering", addCateringPageView, name="addCatering"),
    path('deleteCatering/<id>/', deleteCateringPageView, name = 'deleteCatering'),
    path('singleCatering/<id>/', singleCateringPageView, name="singleCatering"),
    path('addEventMenuItem/<id>/', addEventMenuItemsPageView, name="addEventMenuItem"),
    path('removeEventMenuItem/<eventId>/<menuItemId>/', removeEventMenuItemPageView, name="removeEventMenuItem")
] 