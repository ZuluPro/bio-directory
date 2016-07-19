from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render, redirect
from bio.items.models import PlantItem, PlantSet


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


class PlantItemAdmin(admin.ModelAdmin):
    actions = ('change_stage_selected', 'change_seedling_date_selected',
               'change_planting_date_selected', 'change_blossom_start_date_selected')
    list_display = ('__str__', 'stage', 'type', 'set', 'seedling_date',
                    'planting_date', 'blossom_start_date',)
    list_filter = ()
    fieldsets = (
        (None, {
            'fields': [
                ('type', 'stage', 'set'),
                ('seedling_area', 'seedling_date'),
                ('planting_area', 'planting_date'),
                'blossom_start_date',
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

    def change_stage_selected(self, request, queryset):
        return self._change_field_selected(request, queryset, 'stage')
    change_stage_selected.short_description = _("Change plants' stage")

    def change_seedling_date_selected(self, request, queryset):
        return self._change_field_selected(request, queryset, 'seedling_date')
    change_seedling_date_selected.short_description = _("Change plants' seedling date")

    def change_planting_date_selected(self, request, queryset):
        return self._change_field_selected(request, queryset, 'planting_date')
    change_planting_date_selected.short_description = _("Change plants' planting date")

    def change_blossom_start_date_selected(self, request, queryset):
        return self._change_field_selected(request, queryset, 'blossom_start_date')
    change_blossom_start_date_selected.short_description = _("Change plants' blossom start date")
