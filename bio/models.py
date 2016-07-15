from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse


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


@python_2_unicode_compatible
class Image(models.Model):
    description = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=100)
    image = models.ImageField()

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
class Pest(models.Model):
    name = models.CharField(max_length=50)
    latin_name = models.CharField(max_length=100, blank=True, null=True)

    description = models.TextField(max_length=2000, blank=True, null=True)

    illustration = models.ForeignKey(Image, blank=True, null=True, related_name='pest_illustrations')
    images = models.ManyToManyField(Image, blank=True)

    symptom = models.TextField(max_length=300, blank=True, null=True)
    treatment = models.TextField(max_length=5000, blank=True)

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
# 
# 
# @python_2_unicode_compatible
# class Order(models.Model):
#     name = models.CharField(max_length=50, primary_key=True)
#     description = models.TextField()
# 
#     class Meta:
#         app_label = 'bio'
#         verbose_name = _('order')
#         verbose_name_plural = _('orders')
# 
#     def __str__(self):
#         return self.name
# 
# 
# @python_2_unicode_compatible
# class Family(models.Model):
#     name = models.CharField(max_length=50, primary_key=True)
#     order = models.ForeignKey(Order)
#     description = models.TextField()
# 
#     class Meta:
#         app_label = 'bio'
#         verbose_name = _('family')
#         verbose_name_plural = _('families')
# 
#     def __str__(self):
#         return self.name
# 
# 
# @python_2_unicode_compatible
# class Genus(models.Model):
#     name = models.CharField(max_length=50, primary_key=True)
#     family = models.ForeignKey(Family)
#     description = models.TextField()
# 
#     class Meta:
#         app_label = 'bio'
#         verbose_name = _('genus')
#         verbose_name_plural = _('genus')
# 
#     def __str__(self):
#         return self.name


@python_2_unicode_compatible
class Plant(models.Model):
    name = models.CharField(max_length=50, help_text=_("Common name, example: tomato."), verbose_name=_("name"))
    latin_name = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('latin name'))
    variety = models.CharField(max_length=50, blank=True, null=True, verbose_name=_('variety'))
    # genus = models.ForeignKey(Genus, null=True)
    description = models.TextField(blank=True, help_text=_("How is the plant."), verbose_name=_("description"))
    illustration = models.ForeignKey(Image, blank=True, null=True, related_name='plant_illustrations', help_text=_("Image showed for illustrate the plant."), verbose_name=_("illustration"))
    images = models.ManyToManyField(Image, blank=True, help_text=_("Gallery of images representing the plant."), verbose_name=_("images"))

    pathologies = models.ManyToManyField('Pathology', blank=True, help_text=_("Disease affecting the plant."), verbose_name=_("pathologies"))
    pests = models.ManyToManyField('Pest', blank=True, help_text=_("Organisms that cause nuisance and epidemic disease."), verbose_name=_("pests"))

    lifecycle = models.CharField(choices=LIFECYCLES, max_length=20, blank=True, null=True, verbose_name=_("lifecycle"))

    seedling_description = models.TextField(blank=True, null=True, help_text=_("How to seed."), verbose_name=_("seedling description"))
    seedling_start = models.PositiveSmallIntegerField(choices=MONTHS, blank=True, null=True, help_text=_("When start to seed."), verbose_name=_("seedling start month"))
    seedling_end = models.PositiveSmallIntegerField(choices=MONTHS, blank=True, null=True, help_text=_("When end to seed."), verbose_name=("seedling end month"))
    germination_period = models.PositiveSmallIntegerField(blank=True, null=True, help_text=_("In days."), verbose_name=_("germination time"))

    planting_description = models.TextField(blank=True, null=True, help_text=_("How to plant."), verbose_name=_("planting description"))
    planting_start = models.PositiveSmallIntegerField(choices=MONTHS, blank=True, null=True, help_text=_("When start to plant."), verbose_name=_("planting start month"))
    planting_end = models.PositiveSmallIntegerField(choices=MONTHS, blank=True, null=True, help_text=_("When end to plant."), verbose_name=_("planting end month"))

    growth_period = models.PositiveSmallIntegerField(blank=True, null=True, help_text=_("In days."), verbose_name=_("growth time"))
    growth_description = models.TextField(blank=True, null=True, help_text=_("How plant growths."), verbose_name=_("growth description"))
    growth_maintenance = models.TextField(blank=True, null=True, help_text=_("How to take care."), verbose_name=_("growth maintenance"))

    blossom_period = models.PositiveSmallIntegerField(blank=True, null=True, help_text=_("In days."), verbose_name=_("blossom time"))
    blossom_description = models.TextField(blank=True, null=True, help_text=_("How plant flower."), verbose_name=_("blossom description"))
    blossom_maintenance = models.TextField(blank=True, null=True, help_text=_("How take care of blossom."), verbose_name=_("blossom maintenance"))

    harvest_description = models.TextField(blank=True, null=True, help_text=_("How to harvest."), verbose_name=_("harvest description"))
    harvest_start = models.PositiveSmallIntegerField(choices=MONTHS, blank=True, null=True, help_text=_("When start harvest."), verbose_name=_("harvest start month"))
    harvest_end = models.PositiveSmallIntegerField(choices=MONTHS, blank=True, null=True, help_text=_("When end harvest."), verbose_name=_("harvest end month"))

    like = models.ManyToManyField('self', blank=True, help_text=_("Plants with beneficial association"), verbose_name=_("good with"))
    dislike = models.ManyToManyField('self', blank=True, help_text=_("Plants with bad association"), verbose_name=_("bad with"))

    environment_description = models.TextField(blank=True, null=True, help_text=_("What is the best environment."), verbose_name=_("environment description"))
    temp_min = models.SmallIntegerField(blank=True, null=True, help_text=_("In \xb0C."), verbose_name=_("minimum temperature"))
    temp_optimal_day = models.SmallIntegerField(blank=True, null=True, help_text=_("In \xb0C."), verbose_name=_("optimal day temperature"))
    temp_optimal_night = models.SmallIntegerField(blank=True, null=True, help_text=_("In \xb0C."), verbose_name=_("optimal ngiht temperature"))
    temp_max = models.SmallIntegerField(blank=True, null=True, help_text=_("In \xb0C."), verbose_name=_("maximum temperature"))
    humidity_min = models.PositiveSmallIntegerField(blank=True, null=True, help_text=_("In %."), verbose_name=_("minimum humidity"))
    humidity_max = models.PositiveSmallIntegerField(blank=True, null=True, help_text=_("In %."), verbose_name=_("maximum humidity"))
    density = models.PositiveSmallIntegerField(blank=True, null=True, help_text=_("In unit by m2."), verbose_name=_("optimal density"))

    exposition = models.CharField(choices=EXPOSITIONS, max_length=15, blank=True, null=True, verbose_name=_("exposition"))
    exposition_time = models.PositiveSmallIntegerField(blank=True, null=True, help_text=_("In hours"), verbose_name=_("exposition time"))

    ph_min = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=_("minimum PH"))
    ph_max = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=_("maximum PH"))

    nitrogen = models.PositiveSmallIntegerField(blank=True, null=True)
    phosphorus = models.PositiveSmallIntegerField(blank=True, null=True)
    potassium = models.PositiveSmallIntegerField(blank=True, null=True)

    before = models.ManyToManyField('self', blank=True, help_text=_("What to plant before this plant."), verbose_name=_("plant before"))
    after = models.ManyToManyField('self', blank=True, help_text=_("What to plant after this plant"), verbose_name=_("plant after"))

    food = models.BooleanField(default=True, verbose_name=_("is food"))
    toxic = models.BooleanField(verbose_name=_("is toxic"))
    green_manure = models.BooleanField(default=False, verbose_name=_("is green manure"))

    class Meta:
        app_label = 'bio'
        verbose_name = _('plant')
        verbose_name_plural = _('plants')
        unique_together = ('name', 'variety')

    def __str__(self):
        if self.latin_name and self.variety:
            return "%s (%s) %s" % (self.name, self.latin_name, self.variety)
        elif self.latin_name:
            return "%s (%s)" % (self.name, self.latin_name)
        return self.name

    def get_absolute_url(self):
        return reverse('plant', args=(self.id,))

    def get_admin_url(self):
        return reverse('admin:bio_plant_change', args=(self.id,))

    def get_illustration_url(self):
        return self.illustration.image.url
