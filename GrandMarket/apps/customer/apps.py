from django.urls import path
from oscar.apps.customer.apps import CustomerConfig as CoreCustomerConfig
from .views import HomeView


class CustomerConfig(CoreCustomerConfig):
    name = 'apps.customer'

    def ready(self):
        super().ready()
        self.home_view = HomeView

    def get_urls(self):
        urls = super().get_urls()
        urls += [
            path('home/', self.home_view.as_view(), name='home'),
        ]
        return self.post_process_urls(urls)

