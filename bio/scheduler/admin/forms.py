from django import forms
from bio.scheduler import models as scheduler_models
from schedule.widgets import SpectrumColorPicker


class ActionForm(forms.ModelForm):
    class Meta:
        exclude = []
        widgets = {
            'color_event': SpectrumColorPicker,
        }
