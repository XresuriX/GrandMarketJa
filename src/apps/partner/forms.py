from oscar.apps.dashboard.partners.forms import PartnerCreateForm
from apps.partner.models import Partner
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django import forms
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from oscar.core.loading import get_model
from oscar.core.compat import existing_user_fields, AUTH_USER_MODEL


ROLE_CHOICES = (
    ('limited', ('Limited dashboard access')),
)

class NewPartner(PartnerCreateForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['users'].queryset = get_user_model().objects.filter(pk=user.pk)
            self.fields['users'].initial = user.pk
            self.fields['users'].widget.attrs['hidden'] = True
            self.fields['role'].widget.attrs['hidden'] = True

        self.fields['name'].required = True

    class Meta:
        model = Partner
        fields = ('name', 'image', 'users', 'primary_delivery_location', 'secondary_delivery_location', 'contact_number',)


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



class ExistingUserForm(forms.ModelForm):
    """
    this form was designed by the original oscar devs i just repurposed it to change users role permissions 
    """
    role = forms.ChoiceField(choices=ROLE_CHOICES, widget=forms.RadioSelect,
                             label=_('User role'))
    

    def __init__(self, *args, **kwargs):
        user = kwargs['instance']
        role = 'staff' if user.is_staff else 'limited'
        kwargs.get('initial', {}).setdefault('role', role)
        super().__init__(*args, **kwargs)

    def save(self):
        role = self.cleaned_data.get('role', 'none')
        user = super().save(commit=False)
        user.is_staff = role == 'staff'
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

    class Meta:
        model = AUTH_USER_MODEL
        fields = existing_user_fields(
            ['first_name', 'last_name'])
        
""" + ['age']"""













