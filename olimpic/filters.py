import django_filters
from django.forms import TextInput
from django_filters import FilterSet
from .models import *

class NOCFilter(FilterSet):
    class Meta:
        model = Noc
        fields = '__all__'
    
    noc = django_filters.CharFilter(lookup_expr='icontains')
    region = django_filters.CharFilter(lookup_expr='icontains')
    notes = django_filters.CharFilter(lookup_expr='icontains')


class AthletesFilter(FilterSet):
    class Meta:
        model = Athlete_events
        fields = '__all__'
    
    name = django_filters.CharFilter(lookup_expr='icontains', widget=TextInput(attrs=
    {
        'class': 'datepicker form-control form-control-sm',
        'placeholder': 'Name',
        'size': 20,
    }))
    sex = django_filters.CharFilter(lookup_expr='icontains')
    age = django_filters.CharFilter(lookup_expr='icontains')
    height = django_filters.CharFilter(lookup_expr='icontains')
    weight = django_filters.CharFilter(lookup_expr='icontains')
    team = django_filters.CharFilter(lookup_expr='icontains')
    noc = django_filters.CharFilter(lookup_expr='icontains')
    games = django_filters.CharFilter(lookup_expr='icontains')
    year = django_filters.CharFilter(lookup_expr='icontains')
    season = django_filters.CharFilter(lookup_expr='icontains')
    city = django_filters.CharFilter(lookup_expr='icontains')
    sport = django_filters.CharFilter(lookup_expr='icontains')
    event = django_filters.CharFilter(lookup_expr='icontains')
    medal = django_filters.CharFilter(lookup_expr='icontains')

