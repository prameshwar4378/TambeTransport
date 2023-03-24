from cProfile import label
from dataclasses import fields
from pyexpat import model
from random import choices
from django import forms
from django.db.models.fields import FilePathField
from django.forms.widgets import HiddenInput
from django.contrib.auth.forms import AuthenticationForm

from AdminPanel.models import DBUser
  
# import GeeksModel from models.py
from User.models import DB_Load_Unload_Vehical,DB_Contact_Us

STATUS=(
    ('Pending','Pending'),
    ('Delivered','Delivered')
)


COMPANY = (
    ('Bajaj','Bajaj'),
    ('Simence','Simens'),
    ('Induriance Pvt.Ltd.','Induriance Pvt.Ltd.'),
    ('Wakhard Pharma Ltd.','Wakhard Pharma Ltd.'),
    ('Sanjeev Auto Group','Sanjeev Auto Group'),
    ('Videocon Ltd.','Videocon Ltd.'),
    )

# create a ModelForm
class Form_New_Entry(forms.ModelForm):
    class Meta:
        model = DB_Load_Unload_Vehical
        fields = ('From_LR_No','Vehical_No','From_company','To_company','Bins','From_File','From_File2','Invoice','Status')
        widgets={
            # 'Driver_Name':forms.TextInput(attrs={'class':'form-control'}),
            'From_LR_No':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter LR Number'}),
            'Vehical_No':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Vehical Number'}),
            'Bins':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Number Of Boxes'}),
            # 'From_Date':forms.TextInput(attrs={'class':'form-control'}),    
            # 'To_Date':forms.TextInput(attrs={'class':'form-control'}),
            'Invoice':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Invoice Number'}),
            # 'Status':forms.TextInput(),
        }
        error_messages={
            # 'Driver_Name':{'required':'Enter Driver Name'},
            'Bins':{'required':'Enter Number Of Boxes'},
            'From_LR_No':{'required':'Enter Loading Report Number'},
            'Vehical_No':{'required':'Enter Vehical Number'},
            'From_company':{'required':'Select Company Name'},
            'From_File':{'required':'Upload Loading Report'},
            'Invoice':{'required':'Enter Invoice Name'},
            'Status':{'required':'Select Your Action'},
            }
        labels={
            'From_LR_No':'LR No',
            'Vehical_No':'Vehical No',
            'From_c ompany':'Company Name',
            'From_File':'Upload Photo 1',
            'From_File2':'Upload Photo 2',
            'Bins':'Bin or Boxes',
            'Status':'Status',
            'Invoice':'Invoice'
        }


    def clean(self):
        super (Form_New_Entry, self).clean()
        Status=self.cleaned_data.get('Status')
        From_LR_No=self.cleaned_data.get('From_LR_No')
        From_company=self.cleaned_data.get('From_company')
        To_company=self.cleaned_data.get('To_company')
        if Status=='Delivered':
            self._errors['Status']=self.error_class(['Sorry You Not Able to Delivered Stock Before Loading...!'])
        for inst in DB_Load_Unload_Vehical.objects.all():
            if inst.From_LR_No==From_LR_No:
                self._errors['From_LR_No']=self.error_class(['LR No is Alredy Exist...!'])
        if From_company==To_company:
            self._errors['To_company']=self.error_class(['UnLoading Company should not be same as Loading Company...!'])
        return self.cleaned_data
    
        

class Form_Deliver_Stock(forms.ModelForm):
    class Meta:
        model = DB_Load_Unload_Vehical
        fields = ('From_LR_No','From_company','To_company','To_File','To_File2','To_File3','To_File4','To_File5', 'Receiver','Invoice','Status')
        widgets={
            'From_LR_No':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter LR Number'}),
            # 'Bins':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Number Of Boxes'}),
            'To_File':forms.FileInput(attrs={'class':'form-control'}),
            'To_File2':forms.FileInput(attrs={'class':'form-control'}),
            'To_File3':forms.FileInput(attrs={'class':'form-control'}),
            'To_File4':forms.FileInput(attrs={'class':'form-control'}),
            'To_File5':forms.FileInput(attrs={'class':'form-control'}),
            'Receiver':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Receiver Name'}),
            'Invoice':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Invoice Number'}),
            # 'Status':forms.TextInput(attrs={'class':'form-control'}),
        }
        error_messages={
            'From_LR_No':{'required':'Enter Loading Report Number'},
            # 'Bins':{'required':'Enter Number Of Boxes'},
            'To_company':{'required':'Select Company Name'},
            'Receiver':{'required':'Upload Loading Report'},
            'Invoice':{'required':'Enter Invoice Name'},
            'Status':{'required':'Select Your Action'},
            }
        labels={
            'From_LR_No':'LR No',
            'To_File':'Upload Photo',
            'To_File2':'Upload Photo 2',
            'To_File3':'Upload Photo 3',
            'To_File4':'Upload Photo 4',
            'To_File5':'Upload Photo 5',
            'Receiver':'Receiver Name',
            'Invoice':'Invoice No',
            'To_company':'Company Name'
        }
            

    def clean(self):
        super (Form_Deliver_Stock, self).clean()
        Status=self.cleaned_data.get('Status')

        From_company=self.cleaned_data.get('From_company')
        To_company=self.cleaned_data.get('To_company')
        if From_company==To_company:
            self._errors['To_company']=self.error_class(['Loading Company should not be same as UnLoading company...!'])

        if Status=='Pending' or Status=="":
            self._errors['Status']=self.error_class(['You Need To Delivered Stock...!'])

        return self.cleaned_data
        



class user_login_form(AuthenticationForm):
    username=forms.CharField(label='username',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}))
    password=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}))



# class Form_contact_us(forms.ModelForm):
#     class Meta:
#         model = DB_contact_us
#         fields = ('name','mobile','msg')
        # widgets={
        #     'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Name'}),
        #     'mobile':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Mobile Numebr'}),
        #     'msg':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter message here'}),
        # }
        # labels={
        #     'name':'Full Name',
        #     'mobile':'Mobile',
        #     'msg':'Message',
        # }

class Form_Contact_Us(forms.ModelForm):
    class Meta:
        model=DB_Contact_Us
        fields=('cust_name','cust_mobile','cust_message')
        labels={
            'cust_name':"Name",
            'cust_mobile':"Mobile",
            'cust_message':"Message"
        }