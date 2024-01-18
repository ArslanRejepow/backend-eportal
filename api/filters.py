from django_filters import OrderingFilter, FilterSet, filters

from api.models import News


class NewsFilter(FilterSet):
    q = filters.CharFilter(field_name="title", lookup_expr='icontains')
    order = OrderingFilter(
        fields=(
            ('id', 'id',),
            ('view', 'view',),
            ('like', 'like',),
        )
    )

    class Meta:
        model = News
        fields = ['q', 'order']
