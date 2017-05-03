from django import template
from bio.contribute import permissions

register = template.Library()


@register.filter(name='can_add_plant')
def can_add_plant(user):
    return permissions.user_can_add_plant(user)


@register.filter(name='can_validate')
def can_validate(user):
    return permissions.user_can_validate(user)
