import django_filters
from rest_framework import filters

from api.models import Order, Product


class IsOnStuckFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(stock__gt=0)
class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = {
            "name":["iexact" , "icontains"],
            "price":["exact","lt","gt"],
            "stock":["lt","gt"]
        }

class OrderFilter(django_filters.FilterSet):
    created_at = django_filters.DateFilter(field_name='created_at__date')
    class Meta:
        model = Order
        fields = {
            "status":["exact"],
            "created_at": ["exact", "lt", "gt"]
        }