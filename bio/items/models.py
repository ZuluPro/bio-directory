from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from bio.models import Plant, EXPOSITIONS

AREA_TYPES = (
    (u'outside', _(u'outside')),
    (u'inside', _(u'inside')),
    (u'greenhouse', _(u'inside'))
)
SOIL_TYPES = (
    (u'potting', _(u'potting soil')),
    (u'clay', _(u'clay')),
    (u'sand', _(u'sand')),
    (u'silt', _(u'silt'))
)
PLANT_STAGES = (
    (u'sow', _(u'sow')),
    (u'germination', _(u'germination')),
    (u'seedling', _(u'adult')),
    (u'flowering', _(u'fruit')),
    (u'dormant', _(u'dormant'))
)


@python_2_unicode_compatible
class Area(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=30, choices=AREA_TYPES, verbose_name=_(u'type'))
    soil_type = models.CharField(max_length=30, choices=SOIL_TYPES, blank=True, null=True, verbose_name=_(u'soil type'))
    ph = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=_(u'PH'))
    surface = models.PositiveSmallIntegerField(blank=True, null=True, help_text=_(u'In m2.'), verbose_name=_(u'surface'))

    morning_temp = models.PositiveSmallIntegerField(blank=True, null=True, help_text=_(u'In \xb0C.'), verbose_name=_(u'morning temperature'))
    day_temp = models.PositiveSmallIntegerField(blank=True, null=True, help_text=_(u'In \xb0C.'), verbose_name=_(u'day temperature'))
    night_temp = models.PositiveSmallIntegerField(blank=True, null=True, help_text=_(u'In \xb0C.'), verbose_name=_(u'night temperature'))

    morning_humidity = models.PositiveSmallIntegerField(blank=True, null=True, help_text=_(u'In %.'), verbose_name=_(u'day humidity'))
    day_humidity = models.PositiveSmallIntegerField(blank=True, null=True, help_text=_(u'In %.'), verbose_name=_(u'day humidity'))
    night_humidity = models.PositiveSmallIntegerField(blank=True, null=True, help_text=_(u'In %.'), verbose_name=_(u'night humidity'))

    morning_exposition = models.CharField(choices=EXPOSITIONS, max_length=15, blank=True, null=True, verbose_name=_(u'morning exposition'))
    afternoon_exposition = models.CharField(choices=EXPOSITIONS, max_length=15, blank=True, null=True, verbose_name=_(u'afternoon exposition'))
    exposition_time = models.PositiveSmallIntegerField(blank=True, null=True, help_text=_(u'In hours'), verbose_name=_(u'exposition time'))

    class Meta:
        app_label = u'bio_items'
        verbose_name = _(u'area')
        verbose_name_plural = _(u'areas')

    def __str__(self):
        return self.area


@python_2_unicode_compatible
class PlantItem(models.Model):
    type = models.ForeignKey(Plant)
    stage = models.CharField(max_length=15, choices=PLANT_STAGES, blank=True, null=True, verbose_name=_(u'stage'))

    seedling_area = models.ForeignKey(Area, blank=True, null=True, related_name=u'sown', help_text=_(u'Where it has been sown'), verbose_name=_(u'seedling area'))
    seedling_date = models.DateField(blank=True, null=True, help_text=_(u'When the seed has been planted'), verbose_name=_(u'seedling date'))

    planting_area = models.ForeignKey(Area, blank=True, null=True, related_name=u'planted', help_text=_(u'Where it has been planted'), verbose_name=_(u'planting area'))
    planting_date = models.DateField(blank=True, null=True, help_text=_(u'When it has been planted to growth'), verbose_name=_(u'planting date'))

    blossom_start_date = models.DateField(blank=True, null=True, help_text=_(u'When it has its first flower'), verbose_name=_(u'blossom date'))
    harvest_start_date = models.DateField(blank=True, null=True, help_text=_(u'When it has its usable element'), verbose_name=_(u'harvest date'))
    death_date = models.DateField(blank=True, null=True, help_text=_(u'When it is considered as dead'), verbose_name=_(u'death date'))

    class Meta:
        app_label = u'bio_items'
        verbose_name = _(u'plant')
        verbose_name_plural = _(u'plants')

    def __str__(self):
        return u'%s' % self.type

    def get_absolute_url(self):
        return reverse('plantitem', args=(self.id,))

    def get_admin_url(self):
        return reverse('admin:bio_plantitem_change', args=(self.id,))

    def get_illustration_url(self):
        return self.type.illustration.image.url
