from django.contrib.auth.models import (
    AbstractUser, BaseUserManager, AbstractBaseUser)
from django.db import models
from django.utils.translation import gettext_lazy as _
from oscar.core.compat import AUTH_USER_MODEL
from oscar.apps.customer import abstract_models



# An extension of the core Oscar User model
class CustomUser(abstract_models.AbstractUser):
   
    def __str__(self):
        return self.email




from oscar.apps.customer.models import *  # noqa isort:skip
