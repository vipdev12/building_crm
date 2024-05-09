from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_positive(value):
    if value < 0:
        raise ValidationError(
            _("%(value)s is not an positive number"),
            params={"value": value},
        )
