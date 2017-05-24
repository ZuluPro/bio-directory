from django.contrib import admin
from bio import models
from bio.admin import modeladmins


admin.site.register(models.Plant, modeladmins.PlantAdmin)
admin.site.register(models.Image)
admin.site.register(models.Tag, modeladmins.TagAdmin)
