"""Apps for Bio Guide"""
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class GuideConfig(AppConfig):
    """
    Config for Guide application.
    """
    name = 'bio.guide'
    label = 'bio_guide'
    verbose_name = _('Bio guide')
