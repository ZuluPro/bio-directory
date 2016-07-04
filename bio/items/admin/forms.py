from django import forms
from django.contrib.admin import widgets
from django.utils.translation import ugettext_lazy as _
from bio.items import models


class PlantItemCreationForm(forms.ModelForm):
    number = forms.IntegerField(initial=1, label=_("Number of items"))

    class Meta:
        fields = forms.ALL_FIELDS
        model = models.PlantItem
        widgets = {
        #    'images': widgets.FilteredSelectMultiple(_("Images"), is_stacked=False),
        }
