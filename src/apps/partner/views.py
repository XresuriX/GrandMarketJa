from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse, reverse_lazy

from apps.partner.models import Partner
from apps.partner.forms import NewPartner, ExistingUserForm

from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _
from oscar.core.loading import get_model, get_class
from oscar.core.compat import get_user_model
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView
)

User = get_user_model()

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
    success_url = reverse_lazy('partner:index')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = _('Create new partner')
        return ctx

    def get_success_url(self):
        messages.success(self.request,
                         _("Store '%s' was created successfully.") %
                         self.object.name)
        return reverse('partner:index')
    
    def form_invalid(self, form):
        messages.error(
            self.request,
            "Your submitted data was not valid - please correct the below errors")
        return super().form_invalid(form)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    

class StoreUserUpdateView(UpdateView):
    template_name = 'oscar/store/store_user_update_form.html'
    form_class = ExistingUserForm

    def get_object(self, queryset=None):
        self.partner = get_object_or_404(Partner, pk=self.kwargs['partner_pk'])
        return get_object_or_404(User,
                                 pk=self.kwargs['user_pk'],
                                 partners__pk=self.kwargs['partner_pk'])

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        name = self.object.get_full_name() or self.object.email
        ctx['partner'] = self.partner
        ctx['title'] = _("Edit user '%s'") % name
        return ctx

    def get_success_url(self):
        name = self.object.get_full_name() or self.object.email
        messages.success(self.request,
                         _("User '%s' was updated successfully.") % name)
        return reverse('partner:index')