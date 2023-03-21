import oscar.apps.partner.apps as apps
from django.apps import AppConfig
from oscar.core.application import OscarConfig
from django.urls import path, re_path
from oscar.core.loading import get_class


class PartnerConfig(apps.PartnerConfig):
    name = 'apps.partner'
    namespace = 'partner'

    def ready(self):
            super().ready()
            self.Stores_list_view = get_class(
                'partner.views', 'StoresListView')
            self.Store_detail_view = get_class(
                'partner.views', 'StoreDetailView')
            self.stores_create_view = get_class(
                'partner.views', 'StoreCreateView')
            self.store_user_update_view = get_class(
                'partner.views', 'StoreUserUpdateView')
            self.stores_update_view = get_class(
                'partner.views', 'StoreUpdateView')
            """
            self.stores_delete_view = get_class(
                'partner.views', 'StoreDeleteView')"""

    def get_urls(self):
        urls = super().get_urls()
        urls += [
            path('search/', self.Stores_list_view.as_view(), name='index'),
            path('store/details/<int:pk>/', self.Store_detail_view.as_view(), name='details'),
            path('store/create/', self.stores_create_view.as_view(), name='store-create'),
            path('store/update-user/<int:user_pk>/', self.store_user_update_view.as_view(), name='user-update'),
            path('store/update/<int:pk>/', self.stores_update_view.as_view(), name='update'),
        ]
        return self.post_process_urls(urls)
    
    
    
"""path('update/<int:pk>/', self.stores_update_view.as_view(), name='store-update'),
path('delete/<int:pk>/', self.stores_delete_view.as_view(), name='store-delete'),"""