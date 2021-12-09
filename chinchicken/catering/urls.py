from django.urls import path
from .views import cateringPageView, deleteCateringPageView, editCateringPageView, addCateringPageView

urlpatterns = [
    path("catering/", cateringPageView, name="catering"), 
    path("edit_catering/", editCateringPageView, name="edit_catering"), 
    path("add_catering/", addCateringPageView, name="add_catering"),
    path('delete_catering/<int:cust_id>/', deleteCateringPageView, name = 'delete_catering'),
] 