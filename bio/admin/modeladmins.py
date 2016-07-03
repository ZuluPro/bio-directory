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
                ('name', 'latin_name', 'variety'),
                'description',
                'lifecycle',
                ('illustration', 'images'),
                ('food', 'toxic')
            )
        }),
        (_('Cultivation'), {
            'fields': (
                ('seedling_start', 'seedling_end'),
                'seedling_description',
                'germination_period',

                ('planting_start', 'planting_end'),
                'planting_description',

                'growth_period',
                ('growth_description', 'growth_maintenance'),

                'blossom_period',
                ('blossom_description', 'blossom_maintenance'),
                ('harvest_start', 'harvest_end'),
                'harvest_description',
            )
        }),
        (_('Environment'), {
            'fields': (
                'environment_description',
                ('temp_min', 'temp_optimal_night', 'temp_optimal_day', 'temp_max'),
                ('exposition', 'exposition_time'),
                ('humidity_min', 'humidity_max'),
                ('ph_min', 'ph_max'),
                ('nitrogen', 'phosphorus', 'potassium'),
                ('like', 'dislike'),
                ('after', 'before'),
            )
        }),
        (_('Diseases'), {
            'fields': (
                ('pathologies', 'pests'),
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
