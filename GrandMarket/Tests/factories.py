import pytest
import factory
from factory.django import DjangoModelFactory
from faker import Faker

from oscar.core.compat import AUTH_USER_MODEL

fake = Faker()

class UserFactory(DjangoModelFactory):
    class Meta:
        model = AUTH_USER_MODEL

    email = "a@a.com"
    first_name = "tester"
    password = "tester"
    is_active = "True"
    is_staff = "True"
