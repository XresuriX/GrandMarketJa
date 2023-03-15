import pytest
from django.db import IntegrityError
#from pytest_django.asserts import assertQuerysetEqual
from django.test import TestCase
from Tests.factories import PartnersFactory
from oscar.core.compat import AUTH_USER_MODEL
from apps.partner.models import Partner

"""@pytest.mark.django_db
class TestPartnerModel():
    def test_new_user(new_user_1):
        #print(new_user_1)
        assert True

    def test_new_partner(new_partner_1):
        print(new_partner_1)
        assert True

    def test_partner_1(db, partners_factory):
        partner = partners_factory.create()
        #print(partner.users)
        assert True


@pytest.mark.parametrize(
    "title, id, validity",
    [
        ("clean cc2", 1, True),
        ("dump alfalfa", 2, True),
    ],
)
def test_tasks_instance(
    db, tasks_factory, title, id, validity
):

    test = tasks_factory(
        title=title,
        id=id,
    )

    item = Tasks.objects.all().count()
    print(item)
    assert item == validity


@pytest.mark.django_db
def test_create_partner_with_user(db, user_factory, partners_factory):
    # Create a new partner with a user
    partner = partners_factory.create(users=["new_user_2"])

    # Check if the partner was saved to the database
    print(partner.name)
    assert Partner.objects.filter(id=partner.id).exists()

    # Check if the user was added to the partner's users field
    #assert partner.users.filter(id=new_user_2.id).exists()
"""

@pytest.mark.django_db
@pytest.mark.parametrize(
    "name, code, users, primary_delivery_location, secondary_delivery_location, contact_number, validity",
    [
        ("", "", "", "", "", "", True),
        ("name", "name", "test@user.com", "kingston", "secondary_delivery_location", "38465465", True),
        ("GrandMarket", "Grand-Market", "test@GMJA.com", "kingston", "spanish town", "38465465", True),
        ("", "name", "", "kingston", "secondary_delivery_location", "38465465", True),
    ],
)
def test_partner_instance(
    db, partners_factory, user_factory, name, code, users, primary_delivery_location, secondary_delivery_location, contact_number, validity
):
    test = partners_factory(
        name=name, 
        code=code, 
        users=user_factory(email="test@user.com"), 
        primary_delivery_location=primary_delivery_location, 
        secondary_delivery_location=secondary_delivery_location, 
        contact_number=contact_number,
    )

    item = Partner.objects.all().count()
    print(item)
    assert item == validity
    


