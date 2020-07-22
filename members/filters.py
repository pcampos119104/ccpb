import  django_filters 
from .models import Member


class MemberFilter(django_filters.FilterSet):
    # name_member = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Member
        fields = {
                'name_member': ['icontains'],
                }
