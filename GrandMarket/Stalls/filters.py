import django_filters


from .models import Stall


class StallFilter(django_filters.FilterSet):

    class Meta:
        model = Stall
        fields = ['category', 'primary_delivery_location']
