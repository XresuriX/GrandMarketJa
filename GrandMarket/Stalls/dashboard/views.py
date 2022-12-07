from django.contrib import messages
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _
from django.views import generic
from oscar.core.loading import get_class, get_model

Stalls = get_model('Stalls', 'Stall')
StallsCreateUpdateForm = get_class(
    'Stalls.dashboard.forms', 'DashboardStallCreateUpdateForm')
DashboardStallsSearchForm = get_class(
    'Stalls.dashboard.forms', 'DashboardStallSearchForm')


class DashboardStallsListView(generic.ListView):
    model = Stalls
    template_name = "dashboard/Stall/stalls_list.html"
    context_object_name = "Stalls_list"
    filterform_class = DashboardStallsSearchForm

    def get_title(self):
        data = getattr(self.filterform, 'cleaned_data', {})

        name = data.get('name', None)
        city = data.get('primary_delivery_location', None)

        if name and not city:
            return gettext('Stalls matching "%s"') % name
        elif name and city:
            return gettext('Stalls matching "%s" near "%s"') % (name, city)
        elif city:
            return gettext('Stalls near "%s"') % city
        else:
            return gettext('Stalls')

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


class DashboardStallCreateView(generic.CreateView):
    model = Stalls
    template_name = 'dashboard/Stall/stall_update.html'
    form_class = StallsCreateUpdateForm
    success_url = reverse_lazy('Stalls-dashboard:stalls-list')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = _('Create new Stalls')
        return ctx

    def forms_invalid(self, form, inlines):
        messages.error(
            self.request,
            "Your submitted data was not valid - please correct the below errors")
        return super().forms_invalid(form, inlines)

    def forms_valid(self, form, inlines):
        response = super().forms_valid(form, inlines)

        msg = render_to_string('dashboard/Stall/messages/stall_saved.html',
                               {'Stalls': self.object})
        messages.success(self.request, msg, extra_tags='safe')
        return response


class DashboardStallUpdateView(generic.UpdateView):
    model = Stalls
    template_name = "dashboard/Stall/stall_update.html"
    form_class = StallsCreateUpdateForm
    success_url = reverse_lazy('Stalls-dashboard:stalls-list')

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
        msg = render_to_string('dashboard/Stall/messages/stall_saved.html',
                               {'Stalls': self.object})
        messages.success(self.request, msg, extrforms_valida_tags='safe')
        return super().forms_valid(form, inlines)


class DashboardStallDeleteView(generic.DeleteView):
    model = Stalls
    template_name = "dashboard/Stall/stall_delete.html"
    success_url = reverse_lazy('Stalls-dashboard:stalls-list')
