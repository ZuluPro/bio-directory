from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from schedule.models import Event
from bio.items import models as item_models


@python_2_unicode_compatible
class ActionType(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("name"))
    description = models.TextField(null=True, blank=True, verbose_name=_("description"))

    class Meta:
        app_label = 'bio_scheduler'
        verbose_name = _("action type")
        verbose_name_plural = _("action types")

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Action(Event):
    type = models.ForeignKey(ActionType, verbose_name=_("type"))
    plants = models.ManyToManyField(item_models.PlantItem, blank=True, verbose_name=_("plants"))
    areas = models.ManyToManyField(item_models.Area, blank=True, verbose_name=_("areas"))

    class Meta:
        app_label = 'bio_scheduler'
        verbose_name = _("action")
        verbose_name_plural = _("action")

    def __str__(self):
        _str = self.type.name
        if self.plants.exists():
            _str = '%s %s' % (_str, self.plants.all()[0])
        if self.rule:
            _str = '%s %s' % (_str, self.rule.name)
        return _str

    def get_absolute_url(self):
        return reverse('action', args=(self.id,))

    def get_admin_url(self):
        return reverse('admin:bio_scheduler_action_change', args=(self.id,))
