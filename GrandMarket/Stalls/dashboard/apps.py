from django.urls import path
from oscar.core.application import OscarDashboardConfig
from oscar.core.loading import get_class


class DashboardConfig(OscarDashboardConfig):
    name = 'Stalls.dashboard'
    label = 'Stalls_dashboard'
    namespace = 'Stalls-dashboard'

    default_permissions = ['is_staff']

    def ready(self):
        self.stalls_list_view = get_class(
            'Stalls.dashboard.views', 'DashboardStallsListView')
        self.stalls_create_view = get_class(
            'Stalls.dashboard.views', 'DashboardStallCreateView')
        self.stalls_update_view = get_class(
            'Stalls.dashboard.views', 'DashboardStallUpdateView')
        self.stalls_delete_view = get_class(
            'Stalls.dashboard.views', 'DashboardStallDeleteView')

    def get_urls(self):
        urls = [
            path('', self.stalls_list_view.as_view(), name='stalls-list'),
            path('create/', self.stalls_create_view.as_view(),
                 name='stall-create'),
            path('update/<int:pk>/', self.stalls_update_view.as_view(),
                 name='stall-update'),
            path('delete/<int:pk>/', self.stalls_delete_view.as_view(),
                 name='stall-delete'),
        ]
        return self.post_process_urls(urls)
