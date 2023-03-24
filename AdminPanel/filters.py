import django_filters
from User.models import DB_Load_Unload_Vehical
from django_filters import DateFilter


class All_Record_Data_Filter(django_filters.FilterSet):
    start_date=DateFilter(field_name='From_Date',lookup_expr='gte')
    end_date=DateFilter(field_name='From_Date',lookup_expr='lte')

    def __init__(self, *args, **kwargs):
        super(All_Record_Data_Filter, self).__init__(*args, **kwargs)
        self.filters['Auto_LR_No'].label="Tambe LR No"
        self.filters['start_date'].label="Start Date - MM/DD/YYYY"
        self.filters['end_date'].label="End Date - MM/DD/YYYY"

    class Meta:
        model = DB_Load_Unload_Vehical
        fields = ['Auto_LR_No','Driver_Name','From_company','To_company','From_Date','Status']
    