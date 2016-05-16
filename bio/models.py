from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse


@python_2_unicode_compatible
class Image(models.Model):
    description = models.TextField()
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

    symptom = models.TextField(max_length=300, blank=True, null=True)
    illustrations = models.ManyToManyField(Image, blank=True)

    treatment = models.TextField(max_length=5000, blank=True)

    class Meta:
        app_label = 'bio'
        verbose_name = _('pathology')
        verbose_name_plural = _('pathologies')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('pathology', args=(self.id,))


@python_2_unicode_compatible
class Pest(models.Model):
    name = models.CharField(max_length=50)
    latin_name = models.CharField(max_length=100, blank=True, null=True)

    description = models.TextField(max_length=2000, blank=True, null=True)
    symptom = models.TextField(max_length=300, blank=True, null=True)
    illustrations = models.ManyToManyField(Image, blank=True)

    treatment = models.TextField(max_length=5000, blank=True)

    class Meta:
        app_label = 'bio'
        verbose_name = _('pest')
        verbose_name_plural = _('pests')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('pest', args=(self.id,))
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
    name = models.CharField(max_length=50)
    latin_name = models.CharField(max_length=100, blank=True, null=True)
    # genus = models.ForeignKey(Genus, null=True)
    description = models.TextField(blank=True)
    images = models.ManyToManyField(Image, blank=True)

    pathologies = models.ManyToManyField('Pathology', blank=True)
    pests = models.ManyToManyField('Pest', blank=True)

    planting_description = models.TextField(blank=True, null=True)
    planting_start = models.DateField(blank=True, null=True)
    planting_end = models.DateField(blank=True, null=True)

    harvest_description = models.TextField(blank=True, null=True)
    harvest_start = models.DateField(blank=True, null=True)
    harvest_end = models.DateField(blank=True, null=True)

    like = models.ManyToManyField('self', blank=True)
    dislike = models.ManyToManyField('self', blank=True)
    temp_min = models.SmallIntegerField(blank=True, null=True)
    temp_max = models.SmallIntegerField(blank=True, null=True)
    humidity_min = models.SmallIntegerField(blank=True, null=True)
    humidity_max = models.SmallIntegerField(blank=True, null=True)
    heliophilous = models.NullBooleanField()

    food = models.BooleanField()
    toxic = models.BooleanField()

    class Meta:
        app_label = 'bio'
        verbose_name = _('plant')
        verbose_name_plural = _('plants')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plant', args=(self.id,))

    def get_admin_url(self):
        return reverse('admin:bio_plant_change', args=(self.id,))
