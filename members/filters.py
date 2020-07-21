from django_filters import FilterSet
from .models import Member


class MemberFilter(FilterSet):
    class Meta:
        model = Member
        fields = {
                'name_member': ['icontains'],
                }
