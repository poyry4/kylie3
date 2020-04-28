from django import forms
from . import models

class category_create(forms.ModelForm):
    class Meta:
        model = models.category
        fields = ['title', 'imgCat', ]