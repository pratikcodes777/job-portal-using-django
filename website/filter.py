import django_filters 
from work.models import Work 


class JobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Work 
        fields = ['title' , 'province', 'job_type', 'industry' ]