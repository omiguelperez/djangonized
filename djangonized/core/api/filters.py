from django_filters import FilterSet, CharFilter
from core.models import Todo


class TodoFilter(FilterSet):
    username = CharFilter(name='owner__username', lookup_expr='contains')

    class Meta:
        model = Todo
        fields = ('username', 'done')
