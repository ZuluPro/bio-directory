import random
import json

from django import forms
from django.db.models import fields as model_fields
from django.utils.translation import ugettext_lazy as _

from . import models
from bio import models as bio_models
from bio import forms as bio_forms

BOOLEAN_CHOICES = (
    ('yes', _('Yes')),
    ('no', _('No')),
)


def plant_question_form_factory(plant=None, fieldname=None, user=None):
    from . import utils
    while True:
        if plant is None:
            plant = bio_models.Plant.objects.order_by('?').first()
        elif fieldname is None:
            fieldname = utils.get_plant_unknown_field(plant, user)
        else:
            break
    question = models.PlantQuestion(plant=plant, fieldname=fieldname)
    form_class = forms.modelform_factory(model=bio_models.Plant,
                                         form=PlantQuestionForm,
                                         fields=[fieldname])
    form_class._meta.fields.append('reference')
#     if not hasattr(form_class.Meta, 'widgets'):
#         form_class.Meta.widgets = {}
#     field = bio_models.Plant._meta.get_field(fieldname)
#     if isinstance(field, (model_fields.BooleanField, model_fields.NullBooleanField)):
#         form_class.Meta.widgets[field.attname] = forms.RadioSelect()
#         setattr(form_class, field.attname, forms.ChoiceField(choices=BOOLEAN_CHOICES, widget=forms.RadioSelect()))
#     elif hasattr(field, 'choices'):
#         form_class.Meta.widgets[field.attname] = forms.ChoiceField(choices=field.choices, widget=forms.RadioSelect())
# 
    return form_class
    # form = form_class(instance=question)
    # return form


class AddPlantQuestionForm(forms.ModelForm):
    class Meta:
        model = bio_models.Plant
        fields = ('name',)


class PlantQuestionForm(forms.ModelForm):
    reference = forms.CharField(initial=None, required=False, widget=forms.Textarea(attrs={'class': 'textarea-lg', 'placeholder': _("What are your references ?")}))

    class Meta:
        model = bio_models.Plant
        fields = '__all__'
        exclude = ('id', 'pk', 'illustration_id', 'images')
        widgets = {
          'description': forms.Textarea(attrs={'class': 'textarea-lg'}),
          'environment_description': forms.Textarea(attrs={'class': 'textarea-lg'}),
          'bio_indication': forms.Textarea(attrs={'class': 'textarea-lg'}),
          'latin_name': forms.TextInput(attrs={'class': 'input-lg'})
        }

    def __init__(self, *args, **kwargs):
        super(PlantQuestionForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name) 
            if field:
                if isinstance(field.widget, forms.widgets.NullBooleanSelect):
                    field.widget = forms.widgets.Select(attrs={'placeholder': field.label})

    def field_options(self):
        help_text = self.field.help_text
        if isinstance(self.field, forms.NullBooleanField):
            choices = BOOLEAN_CHOICES
            widget = None
        elif isinstance(self.field, forms.TypedChoiceField):
            model_field = self._meta.model._meta.get_field(self._meta.fields[0])
            choices = [(f, s) for f, s in self.field.choices if f not in (None, '')]
            if isinstance(model_field, model_fields.CharField):
                widget = None
            else:
                widget = '<input class="slider" type="text" name="%s" data-slider-min="%s" data-slider-max="%s" data-slider-step="%s" data-slider-ticks-labels="%s" data-slider-value=""><br><h3 id=value> </h3>' % (
                    self._meta.fields[0],
                    choices[0][0],
                    choices[-1][0],
                    1,
                    json.dumps([c[0] for c in choices]))
        elif hasattr(self.field, 'choices'):
            choices = [(f, s) for f, s in self.field.choices if f not in (None, '')]
            widget = None
        else:
            choices = []
            widget = self.field.widget.render(self._meta.fields[0], None)
        return {
          'choices': choices,
          'widget': widget,
          'help_text': help_text
        }

    @property
    def field(self):
        for fieldname in self.fields:
            return self.fields.get(fieldname)


class PlantImageForm(forms.ModelForm):
    class Meta(bio_forms.ImageForm.Meta):
        model = models.PlantImage
        exclude = ('validated_by', 'declined_by')
