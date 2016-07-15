from django.contrib import admin
from bio.scheduler.admin.forms import ActionForm


class ActionTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filters = ()
    fieldsets = (
        (None, {
            'fields': (
                ('name', 'description'),
            )
        }),
    )


class ActionAdmin(admin.ModelAdmin):
    list_display = ('type',)
    list_filter = ()
    form = ActionForm
    fieldsets = (
        (None, {
            'fields': [
                ('title', 'type', 'color_event'),
                ('plants', 'areas'),
                ('description'),
                ('start', 'end'),
                ('creator', 'calendar'),
                ('rule', 'end_recurring_period'),
                ()
            ]
        }),
    )
