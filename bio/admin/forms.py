from django import forms
from django.contrib.admin import widgets
from django.utils.translation import ugettext_lazy as _
from bio import models


class PlantForm(forms.ModelForm):
    class Meta:
        model = models.Plant
        fields = forms.ALL_FIELDS
        widgets = {
            'images': widgets.FilteredSelectMultiple(_("Images"), is_stacked=False),
            'pests': widgets.FilteredSelectMultiple(_("Pests"), is_stacked=True),
            'pathologies': widgets.FilteredSelectMultiple(_("Pathologies"), is_stacked=True),
            'like': widgets.FilteredSelectMultiple(_("Like"), is_stacked=True),
            'dislike': widgets.FilteredSelectMultiple(_("Dislike"), is_stacked=True),
            'before': widgets.FilteredSelectMultiple(_("Plant before"), is_stacked=True),
            'after': widgets.FilteredSelectMultiple(_("Plant after"), is_stacked=True),
        }
