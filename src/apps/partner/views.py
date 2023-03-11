from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse, reverse_lazy

from apps.partner.models import Partner
from apps.partner.forms import NewPartner

from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _
from oscar.core.loading import get_model, get_class
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView
)



class StoresListView(ListView):
    model = Partner
    template_name = "oscar/store/stores_list.html"
    context_object_name = "stores_list"

    def __init__(self):
        super().__init__()
        self.object_list = self.get_queryset()

    def stores_list(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)


class StoreDetailView(DetailView):
    model = Partner
    template_name = 'oscar/store/store_details.html'
    context_object_name = 'store'


class StoreCreateView(CreateView):
    model = Partner
    template_name = 'oscar/store/store_update.html'
    form_class = NewPartner
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = _('Create new partner')
        return ctx

    def get_success_url(self):
        """messages.success(self.request,
                         _("Partner '%s' was created successfully.") %
                         self.object.name)"""
        return reverse('partner:index')