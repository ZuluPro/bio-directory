from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render, redirect
from bio.items.models import PlantItem, PlantSet

MULTIPLE_CHANGE_FIELDS = (
    ('stage', _("Change plants' stage")),
    ('set', _("Change plants' set")),

    ('germination_guide', _("Change plants' germination guide")),
    ('seedling_area', _("Change plants' seedling area")),
    ('seedling_date', _("Change plants' seedling date")),
    ('real_leaf_date', _("Change plants' first real leaves date")),

    ('transplanting_guide', _("Change plants' transplanting guide")),
    ('transplanting_area', _("Change plants' transplanting area")),
    ('transplanting_date', _("Change plants' transplanting date")),

    ('blossom_guide', _("Change plants' blossom guide")),
    ('blossom_start_date', _("Change plants' blossom start date")),
    ('harvest_start_date', _("Change plants' harvest start date")),

    ('death_date', _("Change plants' death date")),
)


def create_action(field, verbose):
    def action(modeladmin, request, queryset):
        return modeladmin._change_field_selected(request, queryset, field)
    action.func_name = 'change_%s_selected' % field
    action.short_description = verbose
    return action


class AreaAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')
    list_filters = ()
    fieldsets = (
        (None, {
            'fields': (
                ('name', 'type'),
                ('morning_temp', 'day_temp', 'night_temp'),
                ('morning_humidity', 'day_humidity', 'night_humidity'),
                ('morning_exposition', 'afternoon_exposition', 'exposition_time')
            )
        }),
    )


class PlantSetAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'comment', 'active')
    list_filter = ('active',)
    actions = [create_action(field, verbose)
               for field, verbose in MULTIPLE_CHANGE_FIELDS]

    def _change_field_selected(self, request, queryset, field):
        ModelForm = PlantItemAdmin(PlantItem, admin.site).get_form(request, obj=queryset.first(), fields=[field])
        if 'post' in request.POST:
            form = ModelForm(request.POST)
            if form.is_valid():
                for set_ in queryset:
                    set_.plantitem_set.update(**{field: request.POST[field]})
                self.message_user(request, "%(count)i plant set successfully changed to %(field)s." % {
                    'count': queryset.count(),
                    'field': request.POST[field]
                })
                return redirect(request.path)
            else:
                self.message_user(request, form.errors[field], 50)
        else:
            form = ModelForm(instance=queryset.first().plantitem_set.first())
        return render(request, 'bio/admin/change_field_selected.html', {
            'queryset': queryset,
            'action_checkbox_name': '_selected_action',
            'opts': queryset.model._meta,
            'form': form,
            'field': field,
            'field_verbose': PlantItem._meta.get_field(field).verbose_name,
            'media': self.media + form.media
        })


class PlantItemAdmin(admin.ModelAdmin):
    actions = [create_action(field, verbose)
               for field, verbose in MULTIPLE_CHANGE_FIELDS]
    list_display = ('__str__', 'stage', 'type', 'set', 'seedling_date',
                    'real_leaf_date', 'transplanting_date', 'blossom_start_date',)
    list_filter = ()
    fieldsets = (
        (None, {
            'fields': [
                ('type', 'stage', 'set'),
                ('germination_guide', 'seedling_area', 'seedling_date'),
                ('real_leaf_date', 'transplanting_area', 'transplanting_date'),
                ('blossom_guide', 'blossom_start_date'),
                'harvest_start_date',
                'death_date'
            ]
        }),
    )

    def get_form(self, request, obj=None, **kwargs):
        from bio.items.admin.forms import PlantItemCreationForm
        if obj is None or obj.id is None:
            return PlantItemCreationForm
        return super(PlantItemAdmin, self).get_form(request, obj, **kwargs)

    def get_fieldsets(self, request, obj=None):
        fieldsets = super(PlantItemAdmin, self).get_fieldsets(request, obj)
        if (obj is None or obj.id is None) and fieldsets[0][1]['fields'][0] != 'number':
            fieldsets[0][1]['fields'].insert(0, 'number')
        return fieldsets

    def save_model(self, request, obj, form, change):
        if not change:
            data = form.cleaned_data.copy()
            if not data.get('set'):
                data['set'] = PlantSet.objects.create()
            for i in range(data.pop('number')):
                PlantItem.objects.create(**data)
            return
        return super(PlantItemAdmin, self).save_model(request, obj, form, change)

    def _change_field_selected(self, request, queryset, field):
        ModelForm = self.get_form(request, obj=queryset.first(), fields=[field])
        if 'post' in request.POST:
            form = ModelForm(request.POST)
            if form.is_valid():
                queryset.update(**{field: request.POST[field]})
                self.message_user(request, "%(count)i plant(s) successfully changed to %(field)s." % {
                    'count': queryset.count(),
                    'field': getattr(queryset.first(), field),
                })
                return redirect(request.path)
            else:
                self.message_user(request, form.errors[field], 50)
        else:
            form = ModelForm(instance=queryset.first())
        return render(request, 'bio/admin/change_field_selected.html', {
            'queryset': queryset,
            'action_checkbox_name': '_selected_action',
            'opts': queryset.model._meta,
            'form': form,
            'field': field,
            'field_verbose': self.model._meta.get_field(field).verbose_name,
            'media': self.media + form.media
        })
