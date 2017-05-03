from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse


class CompanionShip(models.Model):
    plant = models.ForeignKey('bio.Plant')
    with_ = models.ManyToManyField('bio.Plant')
    impact = models.BooleanField(verbose_name=_("impact"))
    description = models.TextField(verbose_name=_("description"))


class RotationAfter(models.Model):
    plant = models.ForeignKey('bio.Plant')
    after = models.ManyToManyField('bio.Plant')
    description = models.TextField(verbose_name=_("description"))


class RotationBefore(models.Model):
    plant = models.ForeignKey('bio.Plant')
    before = models.ManyToManyField('bio.Plant')
    description = models.TextField(verbose_name=_("description"))
