from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from bio.admin import forms


class PlantAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_image')
    list_filters = ('planting_start', 'harvest_start', 'food', 'toxic')
    form = forms.PlantForm
    fieldsets = (
        (_('Informations'), {
            'fields': (
                ('name', 'latin_name',),
                'description',
                'lifecycle',
                ('illustration', 'images'),
                ('food', 'toxic'),
                'max_age',
                ('green_manure', 'nitrogen_fixing'),
                'bio_indication',
            )
        }),
        (_('Morphology'), {
            'fields': (
                'morphology',
                'deciduous_leaf',
                ('root_depth', 'root_area'),
                ('dense_roots', 'pivot_roots', 'plunging_roots', 'oblique_pivot_roots', 'creeping_roots'),
                ('woody', 'herbaceous'),
                'transplantable'
            )
        }),
        (_('Reproduction'), {
            'fields': (
                ('angiospermae', 'stoloniferous', 'cutting'),
                ('monoecious', 'dioecy', 'hermaphrodite'),
                ('autogamous', 'allogamous'),
            )
        }),
        (_('Germination'), {
            'fields': (
                ('seed_need_stratification', 'seed_conservation_time'),
                ('germination_min_time', 'germination_rate'),
                ('germination_min_temp', 'germination_max_temp'),
                ('germination_humidity_min', 'germination_humidity_max'),
            )
        }),
        (_('Environment'), {
            'fields': (
                'environment_description',
                ('temp_min', 'temp_max'),
                ('humidity_min', 'humidity_max'),
                ('ph_min', 'ph_max'),
                'water_requirement',
                ('nitrogen', 'phosphorus', 'potassium'),
                ('exposition_shade', 'exposition_partial', 'exposition_full'),

            )
        }),
        (_('Culture'), {
            'fields': (
                ('determinate_growth', 'indeterminate_growth'),
            )
        }),
    )

    def get_image(self, obj):
        if not obj.illustration:
            return ''
        return '<a href="{url}" target="_blank"><img src="{url}" height="100px"/></a>'.format(
            url=obj.illustration.image.url)
    get_image.short_description = 'Illustration'
    get_image.allow_tags = True


class PathologyAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_image',)
    fieldsets = (
        (_('Informations'), {
            'fields': (
                ('name', 'latin_name'),
                'description',
                ('illustration', 'images'),
                'symptom',
                'treatment',
            )
        }),
    )

    def get_image(self, obj):
        if not obj.illustration:
            return ''
        return '<a href="{url}" target="_blank"><img src="{url}" height="100px"/></a>'.format(
            url=obj.images.first().image.url)
    get_image.short_description = 'Illustration'
    get_image.allow_tags = True


class PestAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_image',)
    fieldsets = (
        (None, {
            'fields': (
                ('name', 'latin_name'),
                'description',
                ('illustration', 'images'),
                'symptom',
                'treatment',
            )
        }),
    )

    def get_image(self, obj):
        if not obj.illustration:
            return ''
        return '<a href="{url}" target="_blank"><img src="{url}" height="100px"/></a>'.format(
            url=obj.images.first().image.url)
    get_image.short_description = 'Illustration'
    get_image.allow_tags = True
