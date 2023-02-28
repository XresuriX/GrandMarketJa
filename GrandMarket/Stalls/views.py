from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.contrib import messages
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from .filters import StallFilter
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

Stall = get_model('Stalls', 'Stall')
StallsCreateUpdateForm = get_class(
    'Stalls.forms', 'StallCreateUpdateForm')
StallsSearchForm = get_class(
    'Stalls.forms', 'StallSearchForm')

StallStock = get_model('Stalls', 'StallStock')
StallStockCreateUpdateForm = get_class(
    'Stalls.forms', 'StallStockCreateUpdateForm')


class StallListView(ListView):
    model = Stall
    template_name = "Stall/stalls_list.html"
    filterform_class = StallsSearchForm

    def get_title(self):
        data = getattr(self.filterform, 'cleaned_data', {})

        name = data.get('name', None)
        city = data.get('primary_delivery_location', None)

        if name and not city:
            return gettext('Boutiques matching "%s"') % (name)
        elif name and city:
            return gettext('Boutiques matching "%s" near "%s"') % (name, city)
        elif city:
            return gettext('Boutiques near "%s"') % (city)
        else:
            return gettext('Boutiques')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['filterform'] = self.filterform
        data['queryset_description'] = self.get_title()
        return data

    def get_queryset(self):
        qs = self.model.objects.all()
        self.filterform = self.filterform_class(self.request.GET)
        if self.filterform.is_valid():
            qs = self.filterform.apply_filters(qs)
        return qs


class StallDetailView(DetailView):
    model = Stall
    template_name = 'Stall/stall_details.html'
    context_object_name = 'stall'


class StallCreateView(CreateView):
    model = Stall
    template_name = 'Stall/stall_update.html'
    form_class = StallsCreateUpdateForm
    success_url = reverse_lazy('Stalls:index')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = _('Create new Stalls')
        return ctx

    def form_invalid(self, form):
        messages.error(
            self.request,
            "Your submitted data was not valid - please correct the below errors")
        return super().form_invalid(form)

    def form_valid(self, form):
        form.instance.owner = self.request.user
        response = super().form_valid(form)
        msg = render_to_string('Stall/messages/stall_saved.html',
                               {'Stall': self.object})
        messages.success(self.request, msg, extra_tags='safe')
        
        self.object.save()
        return response


class StallUpdateView(UserPassesTestMixin, UpdateView, LoginRequiredMixin):
    model = Stall
    template_name = "Stall/stall_update.html"
    form_class = StallsCreateUpdateForm
    context_object_name = 'stall'

    def test_func(self):
        stall = self.get_object()
        return stall.owner == self.request.user

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = self.object.name
        return ctx

    def forms_invalid(self, form, inlines):
        messages.error(
            self.request,
            "Your submitted data was not valid - please correct the below errors")
        return super().forms_invalid(form, inlines)

    def forms_valid(self, form, inlines):
        msg = render_to_string('Stall/messages/stall_saved.html',
                               {'Stalls': self.object})
        messages.success(self.request, msg, extrforms_valida_tags='safe')
        return super().forms_valid(form, inlines)


class StallDeleteView(DeleteView):
    model = Stall
    template_name = "Stall/stall_delete.html"
    success_url = reverse_lazy('Stalls:index')


class StallDashboardView(DetailView):
    model = StallStock
    template_name = 'Stall/stall_dashboard.html'


class StallStockCreateView(CreateView):
    model = StallStock
    template_name = 'Stall/stallstock_update.html'
    form_class = StallStockCreateUpdateForm
    success_url = reverse_lazy('Stalls:index')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['name'] = _('Create new Stalls stock')
        return ctx

    def forms_invalid(self, form, inlines):
        messages.error(
            self.request,
            "Your submitted data was not valid - please correct the below errors")
        return super().forms_invalid(form, inlines)

    def forms_valid(self, form, inlines):
        form.instance.owner = self.request.user
        response = super().forms_valid(form, inlines)
        msg = render_to_string('Stall/messages/stall_saved.html',
                               {'Stalls': self.object})
        messages.success(self.request, msg, extra_tags='safe')
        return response


class StallStockUpdateView(UserPassesTestMixin, UpdateView, LoginRequiredMixin):
    model = StallStock
    template_name = "Stall/stallstock_update.html"
    form_class = StallStockCreateUpdateForm
    context_object_name = 'stallstock'

    def test_func(self):
        stall = self.get_object()
        return stall.owner == self.request.user

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = self.object.name
        return ctx

    def forms_invalid(self, form, inlines):
        messages.error(
            self.request,
            "Your submitted data was not valid - please correct the below errors")
        return super().forms_invalid(form, inlines)

    def forms_valid(self, form, inlines):
        msg = render_to_string('Stall/messages/stall_saved.html',
                               {'Stalls': self.object})
        messages.success(self.request, msg, extrforms_valida_tags='safe')
        return super().forms_valid(form, inlines)


