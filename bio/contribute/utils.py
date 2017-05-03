import random
from django.db.models import Q
from . import models
from . import forms
from . import permissions


class NoQuestionError(Exception):
    pass


def get_plant_unknown_fields(plant, user=None):
    fieldnames = [f.attname for f in plant._meta.get_fields()
                  if hasattr(f, 'attname') and
                  f.attname not in forms.PlantQuestionForm._meta.exclude and
                  (getattr(plant, f.attname) is None or getattr(plant, f.attname) == '') and
                  not models.PlantQuestion.objects.filter(plant=plant, fieldname=f.attname, user=user).exists()]
    return fieldnames


def get_plant_unknown_field(plant, user=None):
    fieldnames = get_plant_unknown_fields(plant, user)
    if not fieldnames:
        raise NoQuestionError()
    fieldname = random.choice(fieldnames)
    return fieldname


def get_plant_validation_questions(plant, user):
    fieldnames = [f.attname for f in plant._meta.get_fields()
                  if hasattr(f, 'attname') and
                  f.attname not in forms.PlantQuestionForm._meta.exclude]
    return models.PlantQuestion.objects\
        .filter(plant=plant, fieldname__in=fieldnames)\
        .exclude(Q(validated_by=user) | Q(declined_by=user))\
        .exclude(user=user)\
        .order_by('?')


def get_plant_validation_question(user, plant=None):
    if plant is None:
        questions = models.PlantQuestion.objects\
                      .exclude(Q(validated_by=user) | Q(declined_by=user))\
                      .exclude(user=user)\
                      .order_by('?')
        if permissions.user_can_validate(user):
            questions = questions.filter(validated=False)

        question = questions.first()
        if question is None:
            return None
        plant = question.plant
    return get_plant_validation_questions(plant, user).first()


def get_new_plant_validation_questions(user):
    qs = models.NewPlant.objects.filter(validated=False)
    if not permissions.user_can_validate(user):
        qs = qs.exclude(Q(declined_by=user) | Q(user=user))
    return qs


def get_new_plant_validation_question(user):
    return get_new_plant_validation_questions(user)\
            .exclude(user=user)\
            .order_by('?')\
            .first()


def get_plant_image_validation_questions(user):
    qs = models.PlantImage.objects\
        .filter(validated=False)\
        .exclude(Q(validated_by=user) | Q(declined_by=user))
    if permissions.user_can_validate(user):
        qs = qs.filter(validated=False)
    return qs


def get_plant_image_validation_question(user):
    return get_plant_image_validation_questions(user)\
            .order_by('?')\
            .first()
