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
        self.stalls_create_view = get_class(
            'Stalls.views', 'StallCreateView')
        self.stalls_update_view = get_class(
            'Stalls.views', 'StallUpdateView')
        self.stalls_delete_view = get_class(
            'Stalls.views', 'StallDeleteView')

    def get_urls(self):
        urls = super().get_urls()
        urls += [
            path('', self.Stall_list_view.as_view(), name='index'),
            path('details/<int:pk>/', self.Stall_detail_view.as_view(), name='details'),
            path('create/', self.stalls_create_view.as_view(), name='stall-create'),
            path('update/<int:pk>/', self.stalls_update_view.as_view(), name='stall-update'),
            path('delete/<int:pk>/', self.stalls_delete_view.as_view(), name='stall-delete'),
        ]
        return self.post_process_urls(urls)
