from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.contrib import messages
from django.template.loader import render_to_string
from django.urls import reverse_lazy

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


class StallListView(ListView):
    model = Stall
    template_name = "Stall/stalls_list.html"
    context_object_name = "stalls_list"

    def __init__(self):
        super().__init__()
        self.object_list = self.get_queryset()

    def stalls_list(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)


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

    def forms_invalid(self, form, inlines):
        messages.error(
            self.request,
            "Your submitted data was not valid - please correct the below errors")
        return super().forms_invalid(form, inlines)

    def forms_valid(self, form, inlines):
        response = super().forms_valid(form, inlines)

        msg = render_to_string('Stall/messages/stall_saved.html',
                               {'Stalls': self.object})
        messages.success(self.request, msg, extra_tags='safe')
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
