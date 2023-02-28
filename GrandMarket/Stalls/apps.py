from django.apps import AppConfig
from oscar.core.application import OscarConfig
from django.urls import path, re_path
from oscar.core.loading import get_class


class StallsConfig(OscarConfig):
    name = 'Stalls'
    namespace = 'Stalls'

    def ready(self):
        super().ready()
        self.Stall_list_view = get_class(
            'Stalls.views', 'StallListView')
        self.Stall_detail_view = get_class(
            'Stalls.views', 'StallDetailView')
        self.Stall_dashboard_view = get_class(
            'Stalls.views', 'StallDashboardView')
        self.stalls_create_view = get_class(
            'Stalls.views', 'StallCreateView')
        self.stalls_update_view = get_class(
            'Stalls.views', 'StallUpdateView')
        self.stalls_delete_view = get_class(
            'Stalls.views', 'StallDeleteView')

        self.stallstock_create_view = get_class(
            'Stalls.views', 'StallStockCreateView')
        self.stallstock_update_view = get_class(
            'Stalls.views', 'StallStockUpdateView')

    def get_urls(self):
        urls = super().get_urls()
        urls += [
            path('', self.Stall_list_view.as_view(), name='index'),
            path('details/<int:pk>/', self.Stall_detail_view.as_view(), name='details'),
            path('dashboard/<int:pk>/', self.Stall_dashboard_view.as_view(), name='dashboard'),
            path('create/', self.stalls_create_view.as_view(), name='stall-create'),
            path('update/<int:pk>/', self.stalls_update_view.as_view(), name='stall-update'),
            path('delete/<int:pk>/', self.stalls_delete_view.as_view(), name='stall-delete'),
            path('create/stock/<int:pk>', self.stallstock_create_view.as_view(), name='stall-stock-create'),
            path('update/stock/<int:pk>', self.stallstock_update_view.as_view(), name='stall-stock-update'),



        ]
        return self.post_process_urls(urls)


""""""