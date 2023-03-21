from django.db import models
from src import settings
from oscar.apps.partner.abstract_models import AbstractPartner
from oscar.core.utils import slugify
from django.utils.translation import gettext as _
import os
from django.conf import settings
from django.utils.translation import pgettext_lazy



class Partner(AbstractPartner):
    name = models.CharField(
        pgettext_lazy("Partner's name", "Name"), max_length=128, blank=True, db_index=True, unique=True)
    primary_delivery_location = models.CharField(max_length=150, blank=False, null=False, default='kingston')
    secondary_delivery_location = models.CharField(max_length=150, blank=True, null=True)
    contact_number = models.CharField(max_length=20, null=True, blank=True)
    image = models.ImageField(
        _("Image"),
        upload_to="images/partner-images",
        blank=True, null=True)
    group = models.ForeignKey(
        'PartnerGroup',
        models.PROTECT,
        related_name='partners',
        verbose_name=_("Group"),
        null=True,
        blank=True
    )

    is_pickup_store = models.BooleanField(_("Is pickup store"), default=True)
    is_active = models.BooleanField(_("Is active"), default=True)

    """def get_media_path(self, filename):
        
        Returns the full path to a media file, including a subfolder based on the partner's code.
        
        # Create a subfolder using the partner's code
        subfolder = os.path.join('partners', self.code)

        # Join the subfolder and filename to create the full path
        return os.path.join(settings.MEDIA_ROOT, subfolder, filename)"""


class PartnerGroup(models.Model):
    name = models.CharField(_('Name'), max_length=100, unique=True)
    slug = models.SlugField(_('Slug'), max_length=100, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name




from oscar.apps.partner.models import *  # noqa isort:skip
