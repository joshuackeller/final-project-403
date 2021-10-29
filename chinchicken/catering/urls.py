from django.urls import path
from .views import cateringPageView, editCateringPageView

urlpatterns = [
    path("catering/", cateringPageView, name="catering"), 
    path("edit_catering/", editCateringPageView, name="edit_catering"), 
] 