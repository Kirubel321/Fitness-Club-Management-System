import django_filters
from django_filters import DateFilter


from .models import *

class MemberListFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='dateCreated', lookup_expr='gte')
    end_date = DateFilter(field_name='dateCreated', lookup_expr='lte')
    class Meta:
        model = MemberList        
        fields = '__all__'
        exclude = ['memberImage','lastName','email','phoneNumber','address','status','package','plan','trainer','id']