from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def validate_ph(value):
    if value < 0 or value > 14:
        raise ValidationError(
            _('%(value)s is not a pH number'),
            params={'value': value},
        )
