from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.validators import validate_color


# Choices


class TypesOfClothing(models.TextChoices):
    JACKET = "JACKET", _("Jacket")
    COAT = "COAT", _("Coat")
    HOODY = "HOODY", _("Hoody")
    T_SHIRT = "T_SHIRT", _("T-shirt")
    SHIRT = "SHIRT", _("Shirt")

    PANTS = "PANTS", _("Pants")
    DENIM = "DENIM", _("Denim")

    SNEAKERS = "SNEAKERS", _("Sneakers")
    BOOTS = "BOOTS", _("Boots")

    UNDERWEAR = "UNDERWEAR", _("Underwear")
    ACCESSORIES = "ACCESSORIES", _("Accessories")

    DEFAULT = 'DEFAULT', _("Other")


class GenderChoices(models.IntegerChoices):
    MALE = 0, _("male")
    FEMALE = 1, _("female")
    UNISEX = 2, _("unisex")

    __empty__ = _('(Unknown)')


# MODELS

class Clothing(models.Model):
    image = models.ImageField(verbose_name=_("image"), width_field=525, height_field=700)
    name = models.CharField(max_length=100, verbose_name=_("name"))
    description = models.CharField(max_length=500, verbose_name=_("description"))
    color = models.CharField(max_length=6, null=True, verbose_name=_("color"),
                             validators=[validate_color])
    sex = models.IntegerField(
        choices=GenderChoices.choices,
        default=GenderChoices.UNISEX,
        verbose_name=_("sex"),
    )
    forChild = models.BooleanField(verbose_name=_("for child"), default=False)
    size = models.DecimalField(max_digits=70, decimal_places=2, verbose_name=_("size"))
    price = models.DecimalField(max_digits=100000, decimal_places=2, verbose_name=_("price"))
    moderated = models.BooleanField(verbose_name=_("moderated"), default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    _type = models.CharField(
        max_length=12,
        choices=TypesOfClothing.choices,
        default=TypesOfClothing.DEFAULT,
        verbose_name=_("type of clothes")
    )
