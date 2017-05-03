from django import forms
from django.utils.translation import ugettext_lazy as _
from bio import models


class ImageForm(forms.ModelForm):
    class Meta:
        model = models.Image
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'input-lg',
                'placeholder': _("e.g.: A flowering tomato")
            }),
            'description': forms.Textarea(attrs={
                'class': 'textarea-lg', 
                'rows': 3,
                'placeholder': _("e.g.: Tomato will pass from green to red")
            }),
            'image': forms.FileInput(attrs={'style': 'display: none'})
        }
