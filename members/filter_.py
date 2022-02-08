import django_filters


from .models import Mumber

class Mumer_Filter(django_filters.FilterSet):

    name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Mumber
        fields = '__all__'
        exclude = ('owner', 'sex_type','published_at','gruop', 'money', 'image', 'data_sub', 'phone')