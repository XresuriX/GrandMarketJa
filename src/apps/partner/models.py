from django.db import models
from oscar.apps.partner.abstract_models import AbstractPartner

class Partner(AbstractPartner):
    primary_delivery_location = models.CharField(max_length=150, blank=False, null=False, default='kingston')
    secondary_delivery_location = models.CharField(max_length=150, blank=True, null=True)
    contact_number = models.CharField(max_length=20, null=True, blank=True)



from oscar.apps.partner.models import *  # noqa isort:skip
