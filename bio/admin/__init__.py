from django.contrib import admin
from bio import models
from bio.admin import modeladmins


# admin.site.register(models.Order)
# admin.site.register(models.Family)
# admin.site.register(models.Genus)
admin.site.register(models.Plant, modeladmins.PlantAdmin)
admin.site.register(models.Pathology)
admin.site.register(models.Pest)
admin.site.register(models.Image)
