from django.contrib import admin
from bio.items import models
from bio.items.admin import modeladmins

admin.site.register(models.PlantItem, modeladmins.PlantItemAdmin)
admin.site.register(models.PlantSet, modeladmins.PlantSetAdmin)
admin.site.register(models.Area, modeladmins.AreaAdmin)
