from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib import auth

from bio import models as bio_models
from bio import utils
from bio.contribute import signals


class BaseQuestion(models.Model):
    reference = models.TextField(blank=True, max_length=1000, verbose_name=("reference"))

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    date = models.DateTimeField(auto_now_add=True, db_index=True)

    validated_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="+")
    declined_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="+")
    validated = models.BooleanField(default=False)

    class Meta:
        app_label = 'contribute'
        abstract = True

    def get_user_vote(self, user):
        if self.validated_by.filter(id=user.id).exists():
            return True
        elif self.declined_by.filter(id=user.id).exists():
            return False
        return None

    def get_user_vote_score(self, user):
        vote = self.get_user_vote(user)
        if vote is not None:
            return 1 if vote else -1
        return 0

    def has_voted(self, user):
        return self.get_user_vote(user) is not None

    @property
    def voters(self):
        plus = self.validated_by.values_list('id', flat=True)
        minus = self.declined_by.values_list('id', flat=True)
        User = auth.get_user_model()
        return User.objects.filter(id__in=set(plus) | set(minus))

    def vote_plus(self, user):
        self.unvote(user)
        self.validated_by.add(user)
        signals.vote_plus_answer.send(sender=None, instance=self, user=self.user)

    def vote_minus(self, user):
        self.unvote(user)
        self.declined_by.add(user)
        signals.vote_minus_answer.send(sender=None, instance=self, user=self.user)

    def unvote(self, user):
        if self.validated_by.filter(id=user.id).exists():
            self.validated_by.remove(user)
            signals.unvote_plus_answer.send(sender=None, instance=self, user=self.user)
        elif self.declined_by.filter(id=user.id).exists():
            self.declined_by.remove(user)
            signals.unvote_minus_answer.send(sender=None, instance=self, user=self.user)

    def accept_response(self, user):
        raise NotImplementedError()

    def unaccept_response(self, user):
        raise NotImplementedError()

    @property
    def minus_score(self):
        return self.declined_by.count()

    @property
    def plus_score(self):
        return self.validated_by.count()

    @property
    def score(self):
        plus = self.validated_by.count()
        minus = self.declined_by.count()
        return plus - minus


class NewPlant(BaseQuestion):
    name = models.CharField(max_length=100)

    class Meta:
        app_label = 'contribute'
        verbose_name = _("new plant")
        verbose_name_plural = _("new plants")

    def get_absolute_url(self):
        return reverse('contribute-new-plant-question-validate', args=(self.id,))

    @property
    def question(self):
        return _("Do you know a plant we don't know ?")

    @property
    def validation_question(self):
        return _("Does %s is a plant ?") % (self.name)

    def accept_response(self, user):
        self.validated = True
        if not bio_models.Plant.objects.filter(name=self.name).exists():
            bio_models.Plant.objects.create(name=self.name)
        signals.accepted_answer.send(None, instance=self, user=self.user)
        self.save()

    def unaccept_response(self, user):
        self.validated = False
        # bio_models.Plant.objects.filter(name=self.name).delete()
        signals.unaccepted_answer.send(None, instance=self, user=self.user)
        self.save()


class PlantQuestion(BaseQuestion):
    plant = models.ForeignKey('bio.Plant')
    fieldname = models.CharField(max_length=50)

    response = models.CharField(max_length=255)

    class Meta:
        app_label = 'contribute'
        verbose_name = _("plant question")
        verbose_name_plural = _("plant questions")

    def get_absolute_url(self):
        return reverse('contribute-plant-question-validate', args=(self.id,))

    @property
    def question(self):
        field = self.plant._meta.get_field(self.fieldname)
        if isinstance(field, models.TextField):
            q = _("Can you give the %(field)s of a %(plant_name)s") % {
                'field': field.verbose_name,
                'plant_name': self.plant.name,
            }
        elif isinstance(field, (models.BooleanField, models.NullBooleanField)):
            q = _("Does the %(plant_name)s %(field)s ?") % {
                'field': field.verbose_name,
                'plant_name': self.plant.name,
            }
        else:
            q = _("What is the %(field)s of a %(plant_name)s ?") % {
                'field': field.verbose_name,
                'plant_name': self.plant.name,
            }
        return q

    @property
    def validation_question(self):
        field = self.plant._meta.get_field(self.fieldname)
        attr_display = self.get_response_display()
        if isinstance(field, (models.BooleanField, models.NullBooleanField)):
            q = _("Do you agree that %(plant_name)s %(attr_display)s") % {
                'plant_name': self.plant.name,
                'attr_display': attr_display
            }
        else:
            q = _("Do you agree that the %(field)s of a %(plant_name)s is %(attr_display)s ?") % {
                'verbose': field.verbose_name,
                'plant_name': self.plant.name,
                'attr_display': self.get_response_display()
            }
        return q

    def get_field_verbose(self):
        return self.plant._meta.get_field(self.fieldname).verbose_name

    def get_response_display(self):
        attr_name = 'get_%s_display' % self.fieldname
        if hasattr(self.plant, attr_name):
            for val, display in self.plant._meta.get_field(self.fieldname).choices:
                if str(val) == str(self.response):
                    return display
        return self.response

    def accept_response(self, user):
        self.validated = True
        field = self.plant._meta.get_field(self.fieldname)
        if isinstance(field, (models.BooleanField, models.NullBooleanField)):
            value = True if self.response == 'yes' else False
        else:
            value = self.response
        setattr(self.plant, self.fieldname, value)
        self.plant.save()
        signals.accepted_answer.send(None, instance=self, user=self.user)
        self.save()

    def unaccept_response(self, user):
        self.validated = False
        setattr(self.plant, self.fieldname, None)
        self.plant.save()
        signals.unaccepted_answer.send(None, instance=self, user=self.user)
        self.save()


class PlantImage(BaseQuestion):
    plant = models.ForeignKey('bio.Plant')
    title = models.CharField(max_length=100)
    image = models.ImageField(storage=utils.get_media_storage(), upload_to=bio_models.core.image_upload_to)
    description = models.TextField(blank=True, null=True)

    class Meta:
        app_label = 'contribute'
        verbose_name = _("plant image")
        verbose_name_plural = _("plant images")

    def get_absolute_url(self):
        return reverse('contribute-plant-image-validate', args=(self.id,))

    @property
    def validation_question(self):
        return _("Is it a %(plant_name)s ?") % {'plant_name': str(self.plant)}

    def accept_response(self, user):
        self.validated = True
        image = bio_models.Image.objects.filter(image=self.image).first()
        if not image:
            image = bio_models.Image.objects.create(title=self.title,
                                                    image=self.image,
                                                    description=self.description)
        self.plant.images.add(image)
        if self.plant.illustration is None:
            self.plant.illustration = image
            self.plant.save()
        signals.accepted_answer.send(None, instance=self, user=self.user)
        self.save()

    def unaccept_response(self, user):
        self.validated = False
        image = bio_models.Image.objects.filter(image=self.image).first()
        if image:
            self.plant.images.remove(image)
            if self.plant.illustration == image:
                self.plant.illustration = None
                if self.plant.images.all().count():
                    self.plant.illustration = self.plant.images.first()
                self.plant.save()
        signals.unaccepted_answer.send(None, instance=self, user=self.user)
        self.save()
