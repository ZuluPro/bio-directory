from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from bio import models


class PlantAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_image')
    list_filters = ('planting_start', 'harvest_start', 'food', 'toxic',
                    'heliophilous')
    fieldsets = (
        (_('Informations'), {
            'fields': (
                ('name', 'latin_name'),
                'description',
                ('illustration', 'images'),
                ('food', 'toxic')
            )
        }),
        (_('Cultivation'), {
            'fields': (
                ('planting_start', 'planting_end'),
                'planting_description',
                ('harvest_start', 'harvest_end'),
                'harvest_description',
            )
        }),
        (_('Environment'), {
            'fields': (
                'environment_description',
                ('temp_min', 'temp_max'),
                ('humidity_min', 'humidity_max'),
                ('like', 'dislike'),
                'heliophilous',
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


# admin.site.register(models.Order)
# admin.site.register(models.Family)
# admin.site.register(models.Genus)
admin.site.register(models.Plant, PlantAdmin)
admin.site.register(models.Pathology)
admin.site.register(models.Pest)
admin.site.register(models.Image)
