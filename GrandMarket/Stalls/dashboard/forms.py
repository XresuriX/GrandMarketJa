from django import forms
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from oscar.core.loading import get_model

Stall = get_model('Stalls', 'Stall')


class DashboardStallSearchForm(forms.Form):
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

    """def apply_name_filter(self, qs, value):
        return qs.filter(name__icontains=value)"""

    def apply_filters(self, qs):
        for key, value in self.cleaned_data.items():
            if value:
                qs = getattr(self, 'apply_%s_filter' % key)(qs, value)
        return qs


class DashboardStallCreateUpdateForm(forms.ModelForm):
    class Meta:
        model = Stall
        fields = ('name', 'image', 'primary_delivery_location', 'secondary_delivery_location')
