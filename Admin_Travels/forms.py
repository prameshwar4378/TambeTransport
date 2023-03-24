from django import forms
from django.db.models.fields import FilePathField
from django.forms.widgets import HiddenInput
from django.contrib.auth.forms import AuthenticationForm
from User_Travels.models import DB_Tourse_and_Travels

class Form_Update_Travel_Record(forms.ModelForm):
    class Meta:
        model = DB_Tourse_and_Travels
        fields = ('vehical_no','vehical_type','arivel_city','destination_city','opning_km','closing_km','total_km','cust_name','order_by','order_by_photo','status',
         'toll_name_1','toll_name_2','toll_name_3','toll_name_4','toll_name_5','toll_name_6',
         'toll_amount_1','toll_amount_2','toll_amount_3','toll_amount_4','toll_amount_5','toll_amount_6',
         )
        widgets={
            'opning_km':forms.TextInput(attrs={'class':'form-control','onkeyup':'calculate_total_km(this.value);'}),
            'closing_km':forms.TextInput(attrs={'class':'form-control','onkeyup':'calculate_total_km(this.value);'})
            }