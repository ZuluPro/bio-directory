from django.contrib import admin
from bio.scheduler import models
from bio.scheduler.admin import modeladmins


admin.site.register(models.ActionType, modeladmins.ActionTypeAdmin)
admin.site.register(models.Action, modeladmins.ActionAdmin)
