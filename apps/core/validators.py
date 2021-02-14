from re import compile

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

COLOR_RE = compile(r'^#(([0-9a-f]{3})|([0-9a-f]{6}))$')


def validate_color(value: str):
    if COLOR_RE.fullmatch(value):
        raise ValidationError(
            _('%(value)s is not a color'),
            params={'value': value},
        )


__all__ = (
    "validate_color"
)