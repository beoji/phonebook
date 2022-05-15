from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_first_name(value):
    if not value == 'Janusz':
        raise ValidationError(
            _('%(value)s is not an Janusz'),
            params={'value': value},
        )