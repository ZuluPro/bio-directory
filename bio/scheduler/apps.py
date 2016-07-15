"""Apps for Bio Scheduler"""
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class SchedulerConfig(AppConfig):
    """
    Config for Scheduler application.
    """
    name = 'bio.scheduler'
    label = 'bio_scheduler'
    verbose_name = _('Bio scheduler')
