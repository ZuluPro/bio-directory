from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.utils import six
from bio.models import validators

LIFECYCLES = (
    ('perennial', _('Perennial')),
    ('annual', _('Annual')),
    ('biennials', _('Biennials')),
)

EXPOSITIONS = (
    ('full_sunlight', _('full sunlight')),
    ('partial shade', _('partial shade')),
    ('shade', _('shade')),
)
MORPHOLOGIES = (
    ('herbaceous', _("Herbaceous")),
    ('bush', _("Bush")),
    ('tree', _("Tree")),
)
LEVELS = [(i, ('%d/5' % i)) for i in range(6)]
PH = [(i, i) for i in range(15)]
PERCENTAGES = [(i, ('%d%%' % i)) for i in range(0, 101, 1)]
ROOT_DEPTHS = [(i, ('%d cm' % i)) for i in range(0, 10010, 10)]
ROOT_AREAS = [(i, ('%d m2' % i)) for i in range(0, 11)]
TEMPERATURES = [(i, ("%d \xb0C" % i)) for i in range(-30, 51)]
PLANT_AGES = [(i, i) for i in range(1, 1001)]
SEED_AGES = [(i, ('%d month' % i)) for i in range(1, 241)]
GERMINATION_TIMES = [(i, ('%d days' % i)) for i in range(1, 121)]


@python_2_unicode_compatible
class Plant(models.Model):
    name = models.CharField(max_length=50, help_text=_("Common name, example: tomato."), verbose_name=_("name"))
    latin_name = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('latin name'))
    # genus = models.ForeignKey(Genus, null=True)
    description = models.TextField(blank=True, null=True, help_text=_("How is the plant."), verbose_name=_("description"))

    illustration = models.ForeignKey('bio.Image', blank=True, null=True, related_name='plant_illustrations', help_text=_("Image showed for illustrate the plant."), verbose_name=_("illustration"))
    images = models.ManyToManyField('bio.Image', blank=True, help_text=_("Gallery of images representing the plant."), verbose_name=_("images"))

    # Lyfecycle
    lifecycle = models.CharField(choices=LIFECYCLES, max_length=20, blank=True, null=True, verbose_name=_("lifecycle"))
    max_age = models.PositiveSmallIntegerField(blank=True, null=True, choices=PLANT_AGES, help_text=_("in year"), verbose_name=_("maximum age"))


    # Morphology
    ## Roots
    dense_roots = models.NullBooleanField(null=True, blank=True, verbose_name=_("have dense roots"))
    pivot_roots = models.NullBooleanField(null=True, blank=True, verbose_name=_("have pivot roots"))
    plunging_roots = models.NullBooleanField(null=True, blank=True, verbose_name=_("have plunging roots"))
    oblique_pivot_roots = models.NullBooleanField(null=True, blank=True, verbose_name=_("have oblique pivot roots"))
    creeping_roots = models.NullBooleanField(null=True, blank=True, verbose_name=_("have creeping roots"))
    root_depth = models.PositiveSmallIntegerField(blank=True, null=True, choices=ROOT_DEPTHS, help_text=_("in centimeter"), verbose_name=_("root maximum depth"))
    root_area = models.PositiveSmallIntegerField(blank=True, null=True, choices=ROOT_AREAS, help_text=_("in m2"), verbose_name=_("root maximum area"))
    # Aerial
    woody = models.NullBooleanField(null=True, blank=True, verbose_name=_("is woody"))
    herbaceous = models.NullBooleanField(null=True, blank=True, verbose_name=_("is herbaceous"))
    deciduous_leaf = models.NullBooleanField(null=True, blank=True, verbose_name=_("have deciduous leaf"))
    morphology = models.CharField(choices=MORPHOLOGIES, max_length=20, blank=True, null=True, verbose_name=_("morphology"))

    transplantable = models.NullBooleanField(null=True, blank=True, verbose_name=_("is transplantable"))

    # Reproduction
    stoloniferous = models.NullBooleanField(null=True, blank=True, verbose_name=_("is stoloniferous"))
    cutting = models.NullBooleanField(null=True, blank=True, verbose_name=_("support cutting"))
    
    angiospermae = models.NullBooleanField(null=True, blank=True, verbose_name=_("is angiosperma"))
    monoecious = models.NullBooleanField(null=True, blank=True, verbose_name=_("is monoecious"))
    dioecy = models.NullBooleanField(null=True, blank=True, verbose_name=_("is dioecious"))
    hermaphrodite = models.NullBooleanField(null=True, blank=True, verbose_name=_("is hermaphrodite"))
    autogamous = models.NullBooleanField(null=True, blank=True, verbose_name=_("is autogamous"))
    allogamous = models.NullBooleanField(null=True, blank=True, verbose_name=_("is allogamous"))

    entomogamous = models.NullBooleanField(null=True, blank=True, verbose_name=_("is entomogamous"))
    anemogamous = models.NullBooleanField(null=True, blank=True, verbose_name=_("is anemogamous"))

    # Seed
    seed_need_stratification = models.NullBooleanField(null=True, blank=True, verbose_name=_("seed needs stratification"))
    seed_conservation_time = models.PositiveSmallIntegerField(blank=True, null=True, choices=SEED_AGES, help_text=_("In month"), verbose_name=_("seed conservation time"))
    germination_min_time = models.PositiveSmallIntegerField(blank=True, null=True, choices=GERMINATION_TIMES, help_text=_("In days"), verbose_name=_("germination minimum time"))
    germination_rate = models.PositiveSmallIntegerField(blank=True, null=True, choices=PERCENTAGES, help_text=_("In %."), verbose_name=_("Germination rate"))
    germination_min_temp = models.PositiveSmallIntegerField(blank=True, null=True, choices=TEMPERATURES, help_text=_("In \xb0C."), verbose_name=_("germination minimum temperature"))
    germination_max_temp = models.PositiveSmallIntegerField(blank=True, null=True, choices=TEMPERATURES, help_text=_("In \xb0C."), verbose_name=_("germination maximum temperature"))
    germination_humidity_min = models.PositiveSmallIntegerField(blank=True, null=True, choices=PERCENTAGES, help_text=_("In %."), verbose_name=_("germination minimum humidity"))
    germination_humidity_max = models.PositiveSmallIntegerField(blank=True, null=True, choices=PERCENTAGES, help_text=_("In %."), verbose_name=_("germination maximum humidity"))
    # Planting
    # planting_start = models.PositiveSmallIntegerField(choices=MONTHS, blank=True, null=True, help_text=_("When start to plant."), verbose_name=_("planting start month"))
    # planting_end = models.PositiveSmallIntegerField(choices=MONTHS, blank=True, null=True, help_text=_("When end to plant."), verbose_name=_("planting end month"))
    determinate_growth = models.NullBooleanField(verbose_name=_("have determinate growth"))
    indeterminate_growth = models.NullBooleanField(verbose_name=_("have indeterminate growth"))

    # seedling_start = models.PositiveSmallIntegerField(choices=MONTHS, blank=True, null=True, help_text=_("When start to seed."), verbose_name=_("seedling start month"))
    # seedling_end = models.PositiveSmallIntegerField(choices=MONTHS, blank=True, null=True, help_text=_("When end to seed."), verbose_name=("seedling end month"))
    # first_harvest = models.PositiveSmallIntegerField(blank=True, null=True, help_text=_("In month"), verbose_name=_("First harvest after"))
    # harvest_start = models.PositiveSmallIntegerField(choices=MONTHS, blank=True, null=True, help_text=_("When start harvest."), verbose_name=_("harvest start month"))
    # harvest_end = models.PositiveSmallIntegerField(choices=MONTHS, blank=True, null=True, help_text=_("When end harvest."), verbose_name=_("harvest end month"))

    food = models.NullBooleanField(verbose_name=_("is food"))
    toxic = models.NullBooleanField(verbose_name=_("is toxic"))

    # Environement
    environment_description = models.TextField(blank=True, null=True, help_text=_("What is the best environment."), verbose_name=_("environment description"))
    bio_indication = models.TextField(blank=True, null=True, help_text=_("What this plant indicate"), verbose_name=_("bio indication"))

    temp_min = models.SmallIntegerField(blank=True, null=True, choices=TEMPERATURES, help_text=_("In \xb0C."), verbose_name=_("minimum temperature"))
    temp_max = models.SmallIntegerField(blank=True, null=True, choices=TEMPERATURES, help_text=_("In \xb0C."), verbose_name=_("maximum temperature"))
    humidity_min = models.PositiveSmallIntegerField(blank=True, null=True, choices=PERCENTAGES, help_text=_("In %."), verbose_name=_("minimum humidity"))
    humidity_max = models.PositiveSmallIntegerField(blank=True, null=True, choices=PERCENTAGES, help_text=_("In %."), verbose_name=_("maximum humidity"))

    ph_min = models.PositiveSmallIntegerField(blank=True, null=True, choices=PH, validators=[validators.validate_ph], verbose_name=_("minimum pH"))
    ph_max = models.PositiveSmallIntegerField(blank=True, null=True, choices=PH, validators=[validators.validate_ph], verbose_name=_("maximum pH"))

    water_requirement = models.PositiveSmallIntegerField(blank=True, null=True, choices=LEVELS, verbose_name=_("water requirement"))
    nitrogen = models.PositiveSmallIntegerField(blank=True, null=True, choices=LEVELS, verbose_name=_("nitrogen requirements"))
    phosphorus = models.PositiveSmallIntegerField(blank=True, null=True, choices=LEVELS, verbose_name=_("phosphorus requirements"))
    potassium = models.PositiveSmallIntegerField(blank=True, null=True, choices=LEVELS, verbose_name=_("potassium requirements"))

    exposition_full = models.NullBooleanField(blank=True, verbose_name=_("support full sunlight"))
    exposition_partial = models.NullBooleanField(blank=True, verbose_name=_("support partial shade"))
    exposition_shade = models.NullBooleanField(blank=True, verbose_name=_("support shade"))

    green_manure = models.NullBooleanField(verbose_name=_("is green manure"))
    nitrogen_fixing = models.NullBooleanField(verbose_name=_("capture nitrogen"))

    class Meta:
        app_label = 'bio'
        verbose_name = _('plant')
        verbose_name_plural = _('plants')

    def __str__(self):
        if self.latin_name:
            return "%s (%s)" % (self.name, self.latin_name)
        return self.name

    def get_absolute_url(self):
        return reverse('plant', args=(self.id,))

    def get_admin_url(self):
        return reverse('admin:bio_plant_change', args=(self.id,))

    def get_illustration_url(self):
        if self.illustration:
            return self.illustration.image.url

    def get_slug(self):
        slug = self.name.lower().replace(' ', '-').strip()
        return slug

    def get_tag(self):
        from bio.models import Tag
        slug = self.get_slug()
        return Tag.objects.filter(name=slug).first()

    def get_root_types(self):
        root_types = []
        if self.dense_roots:
            root_types.append(_("dense"))
        if self.pivot_roots:
            root_types.append(_("pivot"))
        if self.plunging_roots:
            root_types.append(_("plunging"))
        if self.oblique_pivot_roots:
            root_types.append(_("oblique pivot"))
        if self.creeping_roots:
            root_types.append(_("creeping"))
        return root_types

    def get_root_types_display(self):
        root_types = [six.text_type(s).capitalize() for s in self.get_root_types()]
        display = ' / '.join(root_types)
        return display

    def get_tissue_types(self):
        tissue_type = []
        if self.herbaceous:
            tissue_type.append(_('herbaceous'))
        if self.woody:
            tissue_type.append(_('woody'))
        return tissue_type

    def get_tissue_types_display(self):
        tissue_types = [six.text_type(s).capitalize() for s in self.get_tissue_types()]
        display = ' / '.join(tissue_types)
        return display

    def get_transplantable_display(self):
        if self.transplantable is None:
            return None
        return _("transplatable") if self.transplantable else _("not transplatable")

    def get_reproduction_types(self):
        repr_type = []
        if self.angiospermae:
            repr_type.append(_('flower'))
        if self.stoloniferous:
            repr_type.append(_("stoloniferous"))
        if self.cutting:
            repr_type.append(_('cutting'))
        return repr_type

    def get_reproduction_types_display(self):
        repr_type = [six.text_type(s).capitalize() for s in self.get_reproduction_types()]
        display = ' / '.join(repr_type)
        return display

    def get_sexual_repartitions(self):
        sex_repar = []
        if self.monoecious:
            sex_repar.append(_("monoecious"))
        if self.dioecy:
            sex_repar.append(_("dioecious"))
        if self.hermaphrodite:
            if self.autogamous:
                sex_repar.append(_("hermaphrodite autogamous"))
            else:
                sex_repar.append(_("hermaphrodite"))
        return sex_repar

    def get_sexual_repartition_display(self):
        sex_repar = [six.text_type(s).capitalize() for s in self.get_sexual_repartitions()]
        dis = ' / '.join(sex_repar)
        return dis

    def _get_range_display(self, min_, max_, unit):
        values = {'min': min_, 'max': max_, 'unit': unit}
        if min_ is not None and max_ is not None:
            return _("From %(min)d to %(max)d %(unit)s") % values
        elif min_ is not None:
            return _("Minimum %(min)d %(unit)s") % values
        elif max_ is not None:
            return _("Maximum %(max)d %(unit)s") % values

    def get_germination_temp_display(self):
        return self._get_range_display(self.germination_min_temp,
                                       self.germination_max_temp,
                                       '\xb0C')

    def get_germination_humidity_display(self):
        return self._get_range_display(self.germination_humidity_min,
                                       self.germination_humidity_max,
                                       '%')

    def get_growth_types(self):
        growth_types = []
        if self.determinate_growth:
            growth_types.append('determinate')
        if self.indeterminate_growth:
            growth_types.append('indeterminate')
        return growth_types

    def get_growth_types_display(self):
        growth_types = [six.text_type(s).capitalize() for s in self.get_growth_types()]
        display = ' / '.join(growth_types)
        return display

    def get_temp_display(self):
        return self._get_range_display(self.temp_min, self.temp_max, '\xb0C')

    def get_humidity_display(self):
        return self._get_range_display(self.humidity_min, self.humidity_max, '%')

    def get_ph_display(self):
        return self._get_range_display(self.ph_min, self.ph_max, 'pH')

    def get_exposition_types(self):
        exp_types = []
        if self.exposition_shade:
            exp_types.append(_('shade'))
        if self.exposition_partial:
            exp_types.append(_('partial'))
        if self.exposition_full:
            exp_types.append(_('full sunlight'))
        return exp_types

    def get_exposition_types_display(self):
        exp_types = [six.text_type(s).capitalize() for s in self.get_exposition_types()]
        display = ' / '.join(exp_types)
        return display

    def get_stoloniferous_display(self):
        if self.stoloniferous is None:
            return
        return _("is stoloniferous") if self.stoloniferous else _("isn't stoloniferous")
