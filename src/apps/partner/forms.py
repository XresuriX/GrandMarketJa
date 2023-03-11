from oscar.apps.dashboard.partners.forms import PartnerCreateForm
from apps.partner.models import Partner
from django.contrib.auth.models import Permission
from django import forms
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from oscar.core.loading import get_model


ROLE_CHOICES = (
    ('staff', ('Full dashboard access')),
    ('limited', ('Limited dashboard access')),
)

class PartnerSearchForm(forms.Form):
    name = forms.CharField(label=_('Stall name'), required=False)
    primary_delivery_location = forms.CharField(label=_('Primary delivery location'), required=False)

    def is_empty(self):
        d = getattr(self, 'cleaned_data', {})
        def empty(key): return not d.get(key, None)
        return empty('name') and empty('primary_delivery_location')

    def apply_primary_delivery_location_filter(self, qs, value):
        words = value.replace(',', ' ').split()
        q = [Q(primary_delivery_location__icontains=word) for word in words]
        return qs.filter(*q)

    def apply_name_filter(self, qs, value):
        return qs.filter(name__icontains=value)

    def apply_filters(self, qs):
        for key, value in self.cleaned_data.items():
            if value:
                qs = getattr(self, 'apply_%s_filter' % key)(qs, value)
        return qs


class NewPartner(PartnerCreateForm):
    """def __init__(self, *args, **kwargs):
        user = kwargs['instance']
        role = user = 'limited'
        kwargs.setdefault('initial', {})['role'] = role
        super().__init__(*args, **kwargs)
        # Partner.name is optional and that is okay. But if creating through
        # the dashboard, it seems sensible to enforce as it's the only field
        # in the form.
        self.fields['name'].required = True
        self.fields['users'].initial = user

    def save(self):
        role = self.cleaned_data.get('role', 'none')
        user = super().save(commit=False)
        user.is_staff = role == 'staff'
        if self.cleaned_data['password1']:
            user.set_password(self.cleaned_data['password1'])
        user.save()

        dashboard_perm = Permission.objects.get(
            codename='dashboard_access', content_type__app_label='partner')
        user_has_perm = user.user_permissions.filter(
            pk=dashboard_perm.pk).exists()
        if role == 'limited' and not user_has_perm:
            user.user_permissions.add(dashboard_perm)
        elif role == 'staff' and user_has_perm:
            user.user_permissions.remove(dashboard_perm)
        return user
"""
    class Meta:
        model = Partner
        fields = ('name', 'image', 'primary_delivery_location', 'secondary_delivery_location', 'contact_number',)