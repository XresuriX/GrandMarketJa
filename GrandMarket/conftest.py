import pytest
from pytest_factoryboy import register
from Tests.factories import UserFactory

register(UserFactory)

@pytest.mark.django_db
@pytest.fixture(scope='class')
def new_user_1(db, user_factory):
    user = user_factory.create()
    return user
