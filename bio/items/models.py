from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.utils.timezone import now
from bio.models import Plant, EXPOSITIONS

AREA_TYPES = (
    ('outside', _('outside')),
    ('inside', _('inside')),
    ('greenhouse', _('inside'))
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
    ('seedling', _('adult')),
    ('flowering', _('fruit')),
    ('dormant', _('dormant'))
)


@python_2_unicode_compatible
class Area(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=30, choices=AREA_TYPES, verbose_name=_('type'))
    soil_type = models.CharField(max_length=30, choices=SOIL_TYPES, blank=True, null=True, verbose_name=_('soil type'))
    ph = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=_('PH'))
    surface = models.PositiveSmallIntegerField(blank=True, null=True, help_text=_('In m2.'), verbose_name=_('surface'))

    morning_temp = models.PositiveSmallIntegerField(blank=True, null=True, help_text=_('In \xb0C.'), verbose_name=_('morning temperature'))
    day_temp = models.PositiveSmallIntegerField(blank=True, null=True, help_text=_('In \xb0C.'), verbose_name=_('day temperature'))
    night_temp = models.PositiveSmallIntegerField(blank=True, null=True, help_text=_('In \xb0C.'), verbose_name=_('night temperature'))

    morning_humidity = models.PositiveSmallIntegerField(blank=True, null=True, help_text=_('In %.'), verbose_name=_('morning humidity'))
    day_humidity = models.PositiveSmallIntegerField(blank=True, null=True, help_text=_('In %.'), verbose_name=_('day humidity'))
    night_humidity = models.PositiveSmallIntegerField(blank=True, null=True, help_text=_('In %.'), verbose_name=_('night humidity'))

    morning_exposition = models.CharField(choices=EXPOSITIONS, max_length=15, blank=True, null=True, verbose_name=_('morning exposition'))
    afternoon_exposition = models.CharField(choices=EXPOSITIONS, max_length=15, blank=True, null=True, verbose_name=_('afternoon exposition'))
    exposition_time = models.PositiveSmallIntegerField(blank=True, null=True, help_text=_('In hours'), verbose_name=_('exposition time'))

    class Meta:
        app_label = 'bio_items'
        verbose_name = _('area')
        verbose_name_plural = _('areas')

    def __str__(self):
        return self.area


@python_2_unicode_compatible
class PlantSet(models.Model):
    comment = models.TextField(null=True, blank=True, help_text=_("Comment about this set"), verbose_name=_("comment"))
    active = models.BooleanField(default=True, verbose_name=_('active'))

    class Meta:
        app_label = 'bio_items'
        verbose_name = _('plant set')
        verbose_name_plural = _('plant set')

    def __str__(self):
        sample = self.plantitem_set.first()
        return '%i %s' % (self.plantitem_set.count(), sample.type)


@python_2_unicode_compatible
class PlantItem(models.Model):
    type = models.ForeignKey(Plant)
    stage = models.CharField(max_length=15, choices=PLANT_STAGES, blank=True, null=True, verbose_name=_('stage'))
    set = models.ForeignKey(PlantSet, null=True, blank=True, help_text=_("Which is the set of this plant"), verbose_name=_("set"))

    seedling_area = models.ForeignKey(Area, blank=True, null=True, related_name='sown', help_text=_('Where it has been sown'), verbose_name=_('seedling area'))
    seedling_date = models.DateField(blank=True, null=True, help_text=_('When the seed has been planted'), verbose_name=_('seedling date'))

    planting_area = models.ForeignKey(Area, blank=True, null=True, related_name='planted', help_text=_('Where it has been planted'), verbose_name=_('planting area'))
    planting_date = models.DateField(blank=True, null=True, help_text=_('When it has been planted to growth'), verbose_name=_('planting date'))

    blossom_start_date = models.DateField(blank=True, null=True, help_text=_('When it has its first flower'), verbose_name=_('blossom date'))
    harvest_start_date = models.DateField(blank=True, null=True, help_text=_('When it has its usable element'), verbose_name=_('harvest date'))
    death_date = models.DateField(blank=True, null=True, help_text=_('When it is considered as dead'), verbose_name=_('death date'))

    class Meta:
        app_label = 'bio_items'
        verbose_name = _('plant')
        verbose_name_plural = _('plants')

    def __str__(self):
        if self.blossom_start_date:
            return '%s %s' % (self.type, self.get_blossom_age())
        if self.planting_date:
            return '%s %s' % (self.type, self.get_growth_age())
        if self.seedling_date:
            return '%s %s' % (self.type, self.get_seedling_age())
        return '%s' % self.type

    def get_absolute_url(self):
        return reverse('plantitem', args=(self.id,))

    def get_admin_url(self):
        return reverse('admin:bio_items_plantitem_change', args=(self.id,))

    def get_illustration_url(self):
        return self.type.illustration.image.url

    def _get_day_delta(self, date):
        if isinstance(date, datetime):
            date = date.date()
        last_date = self.death_date if self.death_date else now().date()
        return (last_date - date).days

    def get_seedling_age(self):
        return _('S+%(days)i' % {'days': self._get_day_delta(self.seedling_date)})

    def get_growth_age(self):
        return _('G+%(days)i' % {'days': self._get_day_delta(self.planting_date)})

    def get_blossom_age(self):
        return _('B+%(days)i' % {'days': self._get_day_delta(self.blossom_start_date)})
