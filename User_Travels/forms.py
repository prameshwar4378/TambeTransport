from django import forms
from django.db.models.fields import FilePathField
from django.forms.widgets import HiddenInput
from django.contrib.auth.forms import AuthenticationForm
from User_Travels.models import DB_Tourse_and_Travels
from PIL import Image


class Form_New_Entry(forms.ModelForm):
    class Meta:
        model = DB_Tourse_and_Travels
        fields = ('vehical_no','vehical_type','arivel_city','destination_city','opning_km','opning_km_photo','cust_name','cust_photo')
        widgets={}

class Form_Drop_Cust(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Form_Drop_Cust, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['opning_km'].widget.attrs['readonly'] = True
            self.fields['total_km'].widget.attrs['readonly'] = True
            self.fields['cust_name'].widget.attrs['readonly'] = True

    class Meta:
        model = DB_Tourse_and_Travels
        fields = ('cust_name','opning_km','closing_km','total_km','closing_km_photo','status')
        widgets={
            'opning_km':forms.TextInput(attrs={'class':'form-control','onkeyup':'calculate_total_km(this.value);'}),
            'closing_km':forms.TextInput(attrs={'class':'form-control','onkeyup':'calculate_total_km(this.value);'})
            }

class Form_Manage_Diesel(forms.ModelForm):
   
    class Meta:
        model = DB_Tourse_and_Travels
        fields = ('diesel_amount_1','diesel_amount_2','diesel_amount_3','diesel_amount_4',
        'diesel_meter_photo_1','diesel_meter_photo_2','diesel_meter_photo_3','diesel_meter_photo_4',
        'km_reading_1','km_reading_2','km_reading_3','km_reading_4')
        widgets={
            'km_reading_1':forms.TextInput(attrs={'class':'form-control'}),
        }

    
