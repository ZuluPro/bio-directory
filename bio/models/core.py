from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.utils.text import slugify
from bio import utils


MONTHS = (
    (1, _('January')),
    (2, _('Febuary')),
    (3, _('March')),
    (4, _('April')),
    (5, _('May')),
    (6, _('June')),
    (7, _('July')),
    (8, _('August')),
    (9, _('September')),
    (10, _('October')),
    (11, _('November')),
    (12, _('December')),
)


def image_upload_to(instance, filename):
    filetype = filename.split('.')[-1]
    slug_name = slugify(instance.title)
    full_path = 'bio/images/%s.%s' % (slug_name, filetype)
    import ipdb; ipdb.set_trace()
    return full_path


@python_2_unicode_compatible
class Image(models.Model):
    description = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=100)
    image = models.ImageField(storage=utils.get_media_storage(), upload_to=image_upload_to)

    class Meta:
        app_label = 'bio'
        verbose_name = _('image')
        verbose_name_plural = _('images')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return self.image.url


@python_2_unicode_compatible
class Pathology(models.Model):
    name = models.CharField(max_length=50)
    latin_name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=2000, blank=True, null=True)

    illustration = models.ForeignKey(Image, blank=True, null=True, related_name='pathology_illustrations')
    images = models.ManyToManyField(Image, blank=True)

    symptom = models.TextField(max_length=300, blank=True, null=True)
    treatment = models.TextField(max_length=5000, blank=True)

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
class Insect(models.Model):
    name = models.CharField(max_length=50)
    latin_name = models.CharField(max_length=100, blank=True, null=True)

    description = models.TextField(max_length=2000, blank=True, null=True)

    illustration = models.ForeignKey(Image, blank=True, null=True, related_name='pest_illustrations')
    images = models.ManyToManyField(Image, blank=True)

    class Meta:
        app_label = 'bio'
        verbose_name = _('pest')
        verbose_name_plural = _('pests')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('pest', args=(self.id,))

    def get_admin_url(self):
        return reverse('admin:bio_pest_change', args=(self.id,))

    def get_illustration_url(self):
        return self.illustration.image.url
