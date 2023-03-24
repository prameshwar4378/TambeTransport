import django_filters
from User_Travels.models import DB_Tourse_and_Travels
from django_filters import DateFilter


class Travel_Record_Data_Filter(django_filters.FilterSet):
    start_date=DateFilter(field_name='arivel_time',lookup_expr='gte')
    end_date=DateFilter(field_name='arivel_time',lookup_expr='lte')
    
    def __init__(self, *args, **kwargs):
        super(Travel_Record_Data_Filter, self).__init__(*args, **kwargs)
        self.filters['driver_name'].label="Driver Name"
        self.filters['status'].label="Status"
        self.filters['start_date'].label="Start Date - MM/DD/YYYY"
        self.filters['end_date'].label="End Date - MM/DD/YYYY"
    
    class Meta:
        model = DB_Tourse_and_Travels
        fields = ['driver_name','arivel_time','status']
    

