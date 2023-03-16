import pytest
from django import urls
from django.contrib.auth.models import User
from apps.partner.models import Partner
from apps.partner.views import StoreUserUpdateView
from oscar.apps.dashboard.partners.forms import PartnerCreateForm, ROLE_CHOICES, ExistingUserForm
from Tests.factories import PartnersFactory
from oscar.core.compat import AUTH_USER_MODEL
from apps.partner.models import Partner

"""
@pytest.mark.django_db
def test_form_pass(client, pass_data):
    form_url = urls.reverse_lazy('user-update')
    resp = client.post(form_url, data=pass_data)
    assert resp.status_code == 200
    #assert b'' in resp.content


@pytest.mark.django_db
def test_form_fail(client, fail_data):
    form_url = urls.reverse('store-details')
    resp = client.post(form_url, data=fail_data)
    assert resp.status_code == 404
    #assert b'' in resp.content
"""