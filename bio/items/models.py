from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.utils.timezone import now
from bio.models import Plant, EXPOSITIONS
from bio.guide.models import Guide, PLANT_STAGES, AREA_TYPES, SOIL_TYPES


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
        count = self.plantitem_set.count()
        if count:
            sample = self.plantitem_set.first()
            return '%i %s' % (self.plantitem_set.count(), sample.type)
        return str(_('Empty set'))


@python_2_unicode_compatible
class PlantItem(models.Model):
    type = models.ForeignKey(Plant)
    stage = models.CharField(max_length=15, choices=PLANT_STAGES, blank=True, null=True, verbose_name=_('stage'))
    set = models.ForeignKey(PlantSet, null=True, blank=True, help_text=_("Which is the set of this plant"), verbose_name=_("set"))

    germination_guide = models.ForeignKey(Guide, blank=True, null=True, related_name='germinated_plant', help_text=_('How to germinate'), verbose_name=_('germination guide'))
    seedling_area = models.ForeignKey(Area, blank=True, null=True, related_name='seedling', help_text=_('Where it has been sown'), verbose_name=_('seedling area'))
    seedling_date = models.DateField(blank=True, null=True, help_text=_('When the seed has been planted'), verbose_name=_('seedling date'))

    real_leaf_date = models.DateField(blank=True, null=True, help_text=_('When the has its first real leaves'), verbose_name=_('first real leaves date'))

    transplanting_guide = models.ForeignKey(Guide, blank=True, null=True, related_name='transplanted_plant', help_text=_('How do you plant'), verbose_name=_('transplanting guide'))
    transplanting_area = models.ForeignKey(Area, blank=True, null=True, related_name='planted', help_text=_('Where it has been transplanted'), verbose_name=_('transplanting area'))
    transplanting_date = models.DateField(blank=True, null=True, help_text=_('When it has been transplanted for real growth'), verbose_name=_('transplanting date'))

    blossom_guide = models.ForeignKey(Guide, blank=True, null=True, related_name='plant_blossom', help_text=_('How take care of blossom'), verbose_name=_('blossom guide'))
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
        if self.transplanting_date:
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

    def get_current_guide(self):
        if self.blossom_start_date:
            return self.blossom_guide
        if self.transplanting_date:
            return self.transplanting_guide
        if self.seedling_date:
            return self.germination_guide
        return None

    guide = property(get_current_guide)
