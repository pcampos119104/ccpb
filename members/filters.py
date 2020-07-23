import  django_filters 
from django import forms
from .models import Member


class MemberFilter(django_filters.FilterSet):
    name_member = django_filters.CharFilter(
            widget=forms.TextInput(attrs={'class': 'form-control bg-light border-0 small'}),
            lookup_expr='icontains')

