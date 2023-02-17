import pytest
from django.db import IntegrityError
from pytest_django.asserts import assertQuerysetEqual
from Stalls.models import Stall, StallStock


from oscar.core.compat import AUTH_USER_MODEL

@pytest.mark.django_db
class TestStallModel():
    def test_new_user(new_user_1):
        print(new_user_1)
        assert True

    
    def test_create_new_stall(new_user_1, stall_factory):
        stall = stall_factory.build()
        count = stall.objects.all().count
        print(count)