from django.contrib.auth.models import User
from apps.partner.models import Partner
from oscar.apps.dashboard.partners.forms import PartnerCreateForm, ROLE_CHOICES
import pytest
from django.db import IntegrityError
from pytest_django.asserts import assertQuerysetEqual
from Tests.factories import PartnersFactory
from oscar.core.compat import AUTH_USER_MODEL
from apps.partner.models import Partner





"""def test_save_adds_dashboard_access_permission_to_limited_user(db):
    # Create a test user
    user = get_user_model().objects.create_user(
        username='testuser', password='testpass')

    # Set up the form data with the user's primary key
    partner_data = {'name': 'Test Partner', 'users': [user.pk], 'role': 'limited'}

    # Instantiate the NewPartner form with the test data
    form = NewPartner(data=partner_data)

    # Check if the form is valid
    assert form.is_valid()

    # Call form.save() with the test user as the user parameter
    form.save(user=user)

    # Reload the user from the database to get the updated user instance
    user = get_user_model().objects.get(pk=user.pk)

    # Get the ContentType and Permission objects for the partner app
    content_type = ContentType.objects.get(app_label='partner')
    dashboard_access_perm = Permission.objects.get(
        codename='dashboard_access', content_type=content_type)

    # Check if the user has the dashboard_access permission
    assert dashboard_access_perm in user.user_permissions.all()"""