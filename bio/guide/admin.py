from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from bio.guide import models


class GuideAdmin(admin.ModelAdmin):
    list_display = ('name', 'stage')
    list_filter = ('stage', 'exposition')
    fieldsets = (
        (None, {
            'fields': (
                ('name', 'stage'),
                'description',
                ('area_type', 'soil_type'),
                ('exposition', 'exposition_time'),
                ('humidity_min', 'humidity_max'),
                ('temperature_min', 'temperature_max'),
            )
        }),
    )

admin.site.register(models.Guide, GuideAdmin)
