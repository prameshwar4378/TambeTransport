from dataclasses import fields
import email
from email.policy import default
from pyexpat import model
from django import forms
from django.forms.widgets import PasswordInput
from .models import DBUser,DB_Company_List
from User.models import *

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms  import AuthenticationForm

class UserRegistration(forms.ModelForm):
    class Meta:
        model = DBUser
        fields = ('emp_name','emp_id_no','emp_license_no','emp_adress','emp_user_id','emp_pass','emp_co_pass')
        widgets={
            'emp_name':forms.TextInput(attrs={'class':'form-control'}),
            'emp_id_no':forms.TextInput(attrs={'class':'form-control'}),
            'emp_license_no':forms.TextInput(attrs={'class':'form-control'}),
            'emp_adress':forms.TextInput(attrs={'class':'form-control'}),
            'emp_user_id':forms.TextInput(attrs={'class':'form-control'}),
            'emp_pass':forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
            'emp_co_pass':forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
        }
        labels = {
            'emp_name':'Name',
            'emp_id_no':'ID_No',
            'emp_license_no':'License No',
            'emp_adress':'Adress',
            'emp_user_id':'User ID',
            'emp_pass':'password',
            'emp_co_pass':'Confirm_Password'
        }

class Form_Manage_Vehical_Records(forms.ModelForm):
    class Meta:
        model = DB_Load_Unload_Vehical
        fields = ('From_LR_No','Vehical_No','From_company','Bins','From_File','To_company','To_File', 'Receiver','Invoice','Status')
        widgets={
            # 'Driver_Name':forms.TextInput(attrs={'class':'form-control'}),
            'From_LR_No':forms.TextInput(attrs={'class':'form-control'}),
            'Vehical_No':forms.TextInput(attrs={'class':'form-control'}),
            'Bins':forms.TextInput(attrs={'class':'form-control'}),
            'From_File':forms.FileInput(attrs={'class':'form-control'}),
            # 'From_Date':forms.TextInput(attrs={'class':'form-control'}),    
            # 'To_Date':forms.TextInput(attrs={'class':'form-control'}),
            'To_File':forms.FileInput(attrs={'class':'form-control'}),
            'Receiver':forms.TextInput(attrs={'class':'form-control'}),
            'Invoice':forms.TextInput(attrs={'class':'form-control'}),
        }


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError  
from django.forms.fields import EmailField  
from django.forms.forms import Form  

class UserRegistration(UserCreationForm):
    password1=forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}))
    password2=forms.CharField(label='Co-Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Confirm Password'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'enter username'}),
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'enter Driver Full Name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'License ID Number'}),
            'email':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Email Address'}),
        }
        labels={
            'username':'Username',
            'first_name':'Driver Name',
            'last_name':'License No',
            'email':'Email Adress',
            'password2':'Confirm Password'
        }

# 'Vehical_No'
# 'Auto_LR_No'
# 'From_company'
# 'From_Adress'
# 'From_Mobile'
# 'To_company'
# 'To_Adress'
# 'To_Mobile'
# 'Bins'
# 'Receiver'
# 'Invoice'
# 'Freight_ToPay'
# 'ST_Charges_ToPay'
# 'Value_Subcharge_ToPay'
# 'AOC_ToPay'
# 'Hamali_Charges_ToPay'
# 'Other_Charges_ToPay'
# 'Door_Delivery_ToPay'
# 'SUB_TOTAL_ToPay''GST_ToPay'
# 'GRAND_TOTAL_ToPay'

# 'Freight_Paid'
# 'ST_Charges_Paid'
# 'Value_Subcharge_Paid'
# 'AOC_Paid'
# 'Hamali_Charges_Paid'
# 'Other_Charges_Paid'
# 'Door_Delivery_Paid'
# 'SUB_TOTAL_Paid'
# 'GST_Paid'
# 'GRAND_TOTAL_Paid'

class From_Generate_LR(forms.ModelForm):

      class Meta:
        model = DB_Load_Unload_Vehical
        ordering=['From_company']
        fields = ('Auto_LR_No','E_Way_Bill','Vehical_No',
                  'From_company','From_Adress','From_Mobile','From_Branch_Code',
                  'To_company','To_Adress','To_Mobile','To_Branch_Code',
                  'Bins','Invoice',

                  'Freight_ToPay','ST_Charges_ToPay','Value_Subcharge_ToPay','AOC_ToPay','Hamali_Charges_ToPay',
                  'Other_Charges_ToPay','Door_Delivery_ToPay','SUB_TOTAL_ToPay','GST_ToPay_Per','GST_ToPay','GRAND_TOTAL_ToPay',

                  'Freight_Paid','ST_Charges_Paid','Value_Subcharge_Paid','AOC_Paid','Hamali_Charges_Paid',
                  'Other_Charges_Paid','Door_Delivery_Paid','SUB_TOTAL_Paid','GST_Paid_Per','GST_Paid','GRAND_TOTAL_Paid',

                  'Description','Actual_Weight','Charged_Weight','Item_Type','Delivery_At'
                  )
        widgets={
                'Auto_LR_No':forms.TextInput(attrs={'class':'form-control'}),
                'Vehical_No':forms.TextInput(attrs={'class':'form-control'}),
                'Bins':forms.TextInput(attrs={'class':'form-control'}),

                # 'From_company':forms.TextInput(attrs={'class':'form-control'}),
                'From_Adress':forms.TextInput(attrs={'class':'form-control'}),
                'From_Mobile':forms.TextInput(attrs={'class':'form-control'}),
                # 'To_company':forms.TextInput(attrs={'class':'cmb_company'}),
                'To_Adress':forms.TextInput(attrs={'class':'form-control'}),
                'To_Mobile':forms.TextInput(attrs={'class':'form-control'}),
                'Receiver':forms.TextInput(attrs={'class':'form-control'}),
                'Invoice':forms.TextInput(attrs={'class':'form-control'}),
               
                'Freight_ToPay':forms.TextInput(attrs={'class':'form-control','onkeyup':'additionToPay(this.value);'}),
                'ST_Charges_ToPay':forms.TextInput(attrs={'class':'form-control','onkeyup':'additionToPay(this.value);'}),
                'Value_Subcharge_ToPay':forms.TextInput(attrs={'class':'form-control','onkeyup':'additionToPay(this.value);'}),
                'AOC_ToPay':forms.TextInput(attrs={'class':'form-control','onkeyup':'additionToPay(this.value);'}),
                'Hamali_Charges_ToPay':forms.TextInput(attrs={'class':'form-control','onkeyup':'additionToPay(this.value);'}),
                'Other_Charges_ToPay':forms.TextInput(attrs={'class':'form-control','onkeyup':'additionToPay(this.value);'}),
                'Door_Delivery_ToPay':forms.TextInput(attrs={'class':'form-control','onkeyup':'additionToPay(this.value);'}),
                'SUB_TOTAL_ToPay':forms.TextInput(attrs={'class':'form-control'}),
                'GST_ToPay_Per':forms.TextInput(attrs={'class':'form-control','onkeyup':'additionToPay(this.value);'}),
                'GST_ToPay':forms.TextInput(attrs={'class':'form-control','onkeyup':'additionToPay(this.value);'}),
                'GRAND_TOTAL_ToPay':forms.TextInput(attrs={'class':'form-control'}),
               
                'Freight_Paid':forms.TextInput(attrs={'class':'form-control','onkeyup':'additionPaid(this.value);'}),
                'ST_Charges_Paid':forms.TextInput(attrs={'class':'form-control','onkeyup':'additionPaid(this.value);'}),
                'Value_Subcharge_Paid':forms.TextInput(attrs={'class':'form-control','onkeyup':'additionPaid(this.value);'}),
                'AOC_Paid':forms.TextInput(attrs={'class':'form-control','onkeyup':'additionPaid(this.value);'}),
                'Hamali_Charges_Paid':forms.TextInput(attrs={'class':'form-control','onkeyup':'additionPaid(this.value);'}),
                'Other_Charges_Paid':forms.TextInput(attrs={'class':'form-control','onkeyup':'additionPaid(this.value);'}),
                'Door_Delivery_Paid':forms.TextInput(attrs={'class':'form-control','onkeyup':'additionPaid(this.value);'}),
                'SUB_TOTAL_Paid':forms.TextInput(attrs={'class':'form-control'}),
                'GST_Paid_Per':forms.TextInput(attrs={'class':'form-control','onkeyup':'additionPaid(this.value);'}),
                'GST_Paid':forms.TextInput(attrs={'class':'form-control','onkeyup':'additionPaid(this.value);'}),
                'GRAND_TOTAL_Paid':forms.TextInput(attrs={'class':'form-control'}),
                
                'Decription':forms.TextInput(attrs={'class':'form-control'}),
                'Actual_Weight':forms.TextInput(attrs={'class':'form-control'}),
                'Charged_Weight':forms.TextInput(attrs={'class':'form-control'}),
                # 'Item_Type':forms.TextInput(attrs={'class':'form-control'}),
                'Delivery_At':forms.TextInput(attrs={'class':'form-control'}),
        }
        labels={
                 'Auto_LR_No':'Tambe LR No',
                 'Bins':'Bin or Boxes',
                 'From_company':'Company Name',
                 'From_Adress':'Company Adress',
                 'From_Mobile':'Mobile',
                 'E_Way_Bill':'E_Way_Bill_No',
                 'From_Branch_Code':'Branch_Code',
                 'To_company':'Company Name',
                 'To_Adress':'Company Adress',
                 'To_Mobile':'Mobile',
                 'To_Branch_Code':'Branch_Code',
                 'GST_ToPay_Per':'GST Percentage %',
                 'GST_Paid_Per':'GST Percentage %',
                 'GST_ToPay':'GST Amount',
                 'GST_Paid':'GST Amount',
            }
      error_messages={
            # 'Driver_Name':{'required':'Enter Driver Name'},
            'Bins':{'required':'Enter Number Of Boxes'
            }}
            



class Form_Company_list(forms.ModelForm):
    class Meta:
        model = DB_Company_List
        fields = ('Company_Name',)



class Form_Auto_Generate_Lr(forms.ModelForm):
    class Meta:
        model=DB_Load_Unload_Vehical
        fields=('Auto_LR_No',)

class login_form(AuthenticationForm):
    username=forms.CharField(label='username',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}))
    password=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}))


     
