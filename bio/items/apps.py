"""Apps for Bio Items"""
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ItemConfig(AppConfig):
    """
    Config for Item application.
    """
    name = 'bio.items'
    label = 'bio_items'
    verbose_name = _('Bio items')
