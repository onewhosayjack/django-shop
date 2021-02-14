from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Clothing(models.Model):
    image = models.ImageField(verbose_name=_("image"), width_field=525, height_field=700)

    name = models.CharField(max_length=100, verbose_name=_("name"))
    description = models.CharField(max_length=500, verbose_name=_("description"))
    
    color = models.CharField(max_length=6, null=True, verbose_name=_("color"))

    gender = models.ValueRange(0, 2)
    isChild = models.BooleanField(verbose_name=_("is child"))

    size = models.DecimalField(max_digits=70, decimal_places=2, verbose_name=_("size"))

    # code = models.CharField(max_length=50, verbose_name=_("code"))

    price = models.DecimalField(max_digits=100000, decimal_places=2, verbose_name=_("price"))

    moderated = models.BooleanField(verbose_name=_("moderated"), default=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE)


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



    _type = models.CharField(max_length=12, choices=TypesOfClothing.choices, default=TypesOfClothing.DEFAULT)
