import django_filters
from .models import Mobile


class MobileFilter(django_filters.FilterSet):
    class Meta:
        model = Mobile
        fields = ['os', 'price', 'data_transfer', 'processor_speed']