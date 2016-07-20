from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from bio.models import EXPOSITIONS, Image

AREA_TYPES = (
    ('outside', _('outside')),
    ('inside', _('inside')),
    ('greenhouse', _('greenhouse'))
)
SOIL_TYPES = (
    ('potting', _('potting soil')),
    ('clay', _('clay')),
    ('sand', _('sand')),
    ('silt', _('silt'))
)
PLANT_STAGES = (
    ('sow', _('sow')),
    ('germination', _('germination')),
    ('juvenile', _('juvenile')),
    ('adult', _('adult')),
    ('blossom', _('blossom')),
    ('fruit', _('fruit')),
    ('dormant', _('dormant'))
)
GUIDE_STAGES = PLANT_STAGES[1:]


@python_2_unicode_compatible
class Guide(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("name"))
    stage = models.CharField(max_length=15, choices=GUIDE_STAGES, blank=True, null=True, verbose_name=_('stage'))
    description = models.TextField(blank=True, verbose_name=_("description"))

    illustration = models.ForeignKey(Image, blank=True, null=True, related_name='guide_illustrations')
    images = models.ManyToManyField(Image, blank=True)


    area_type = models.CharField(max_length=30, choices=AREA_TYPES, blank=True, null=True, verbose_name=_('type'))
    soil_type = models.CharField(max_length=30, choices=SOIL_TYPES, blank=True, null=True, verbose_name=_('soil type'))

    exposition = models.CharField(choices=EXPOSITIONS, max_length=15, blank=True, null=True, verbose_name=_("exposition"))
    exposition_time = models.PositiveSmallIntegerField(blank=True, null=True, help_text=_("In hours"), verbose_name=_("exposition time"))

    humidity_min = models.PositiveSmallIntegerField(blank=True, null=True, help_text=_("In %."), verbose_name=_("minimum humidity"))
    humidity_max = models.PositiveSmallIntegerField(blank=True, null=True, help_text=_("In %."), verbose_name=_("maximum humidity"))

    temperature_min = models.SmallIntegerField(blank=True, null=True, help_text=_('In \xb0C.'), verbose_name=_('minimum temperature'))
    temperature_max = models.SmallIntegerField(blank=True, null=True, help_text=_('In \xb0C.'), verbose_name=_('maximum temperature'))

    class Meta:
        app_label = 'bio_guide'
        verbose_name = _('guide')
        verbose_name_plural = _('guides')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('guide', args=(self.id,))

    def get_admin_url(self):
        return reverse('admin:bio_guide_guide_change', args=(self.id,))

    def get_illustration_url(self):
        return self.illustration.image.url
