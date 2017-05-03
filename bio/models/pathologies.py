from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse


@python_2_unicode_compatible
class Pathology(models.Model):
    name = models.CharField(max_length=50)
    latin_name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=2000, blank=True, null=True)

    illustration = models.ForeignKey('bio.Image', blank=True, null=True, related_name='pathology_illustrations')
    images = models.ManyToManyField('bio.Image', blank=True)

    symptom = models.TextField(max_length=300, blank=True, null=True)

    class Meta:
        app_label = 'bio'
        verbose_name = _('pathology')
        verbose_name_plural = _('pathologies')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('pathology', args=(self.id,))

    def get_admin_url(self):
        return reverse('admin:bio_pathology_change', args=(self.id,))

    def get_illustration_url(self):
        return self.illustration.image.url


@python_2_unicode_compatible
class PathologyTreatment(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=2000, blank=True, null=True)
    pathologies = models.ManyToManyField(Pathology)
