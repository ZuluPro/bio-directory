from django.contrib import admin
from bio.items.models import PlantItem


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


class PlantItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'type')
    list_filter = ()
    fieldsets = (
        (None, {
            'fields': [
                ('type', 'stage'),
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
            for i in range(data.pop('number') - 1):
                PlantItem.objects.create(**data)
        return super(PlantItemAdmin, self).save_model(request, obj, form, change)
