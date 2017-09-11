from __future__ import unicode_literals
from django import forms
from .models import Photo

class PhotoForm(forms.ModelForm):
    image = forms.ImageField()
    filtered_image = forms.ImageField()
    content = forms.CharField(
        max_length = 500,
        required = False,
        widget = forms.Textarea
        )
    created_at = forms.DateTimeField(required=False)

    class Meta: # o specify a custom widget for a field, use the widgets attribute of the inner Meta class
        model = Photo
        #fields = ('image','content',)
        exclude = ('filtered_image', )