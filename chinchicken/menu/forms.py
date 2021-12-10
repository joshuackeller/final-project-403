from django import forms
from .models import Menu_Item


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Menu_Item
        fields = ('name', 'price', 'photo_main')
