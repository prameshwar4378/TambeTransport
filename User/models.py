from email.mime import image
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from AdminPanel.models import DB_Company_List

class DB_Contact_Us(models.Model):
    cust_name=models.CharField(max_length=50)
    cust_mobile=models.BigIntegerField()
    cust_message=models.TextField(max_length=1000)
    enquiry_date=models.DateTimeField(auto_now=True, auto_now_add=False, editable=True)





# declare a new model with a name "GeeksModel"
COMPANY = (
    ('Bajaj','Bajaj'),
    ('Simence','Simens'),
    ('Induriance Pvt.Ltd.','Induriance Pvt.Ltd.'),
    ('Wakhard Pharma Ltd.','Wakhard Pharma Ltd.'),
    ('Sanjeev Auto Group','Sanjeev Auto Group'),
    )

STATUS=(
    ('Pending','Pending'),
    ('Delivered','Delivered')
)


class DB_Load_Unload_Vehical(models.Model):
           # fields of the model
    Auto_LR_No=models.BigIntegerField(null=True)
    From_LR_No = models.BigIntegerField()
    Driver_Name = models.ForeignKey(User, related_name="Admin", on_delete=models.CASCADE)
    E_Way_Bill = models.CharField(max_length=100,blank=True, null=True)

    # first_name=models.ForeignKey(User, on_delete=models.CASCADE)
    Vehical_No = models.CharField(max_length=50)
    Bins=models.IntegerField(null=True)
    From_company=models.ForeignKey(DB_Company_List, related_name="Bajaj", on_delete=models.CASCADE)
    From_Adress=models.CharField(max_length=500,null=True,default="")
    From_Mobile=models.BigIntegerField(blank=True, null=True)
    From_Branch_Code=models.CharField(max_length=100,blank=True, null=True)
    # From_File=models.FileField(upload_to='From_Company/',max_length=250,default=None)
    From_File=models.ImageField(upload_to='From_company/', height_field=None, width_field=None, max_length=None,null=True)
    From_File2=models.ImageField(upload_to='From_company2/', default="static/default.png", height_field=None, width_field=None, max_length=None,null=True, blank=True)
    From_Date=models.DateTimeField(auto_now=False, auto_now_add=True, editable=True)
    To_company=models.ForeignKey(DB_Company_List, related_name="Bajaj1", null=True, on_delete=models.CASCADE)
    To_Adress=models.CharField(max_length=500,null=True,default="")
    To_Mobile=models.BigIntegerField(blank=True, null=True)
    To_Date=models.DateTimeField(auto_now=True, auto_now_add=False)
    To_Branch_Code=models.CharField(max_length=100,blank=True, null=True)
    To_File=models.ImageField(upload_to='To_company/', default="static/default.png", height_field=None, width_field=None, max_length=None, null=True)
    To_File2=models.ImageField(upload_to='To_company2/',default="static/default.png", height_field=None, width_field=None, max_length=None, null=True, blank=True)
    To_File3=models.ImageField(upload_to='To_company3/',default="static/default.png", height_field=None, width_field=None, max_length=None, null=True, blank=True)
    To_File4=models.ImageField(upload_to='To_company4/',default="static/default.png", height_field=None, width_field=None, max_length=None, null=True, blank=True)
    To_File5=models.ImageField(upload_to='To_company5/',default="static/default.png", height_field=None, width_field=None, max_length=None, null=True, blank=True)
    # To_File=models.FileField(upload_to='To_Company/',max_length=250,default=None,editable=True)
    Receiver=models.CharField(max_length=50)
    Invoice=models.CharField(max_length=50,blank=True, null=True)
    Status=models.CharField(max_length=50,choices=STATUS)

    Freight_ToPay=models.IntegerField(blank=True, null=True,default="0")
    ST_Charges_ToPay=models.IntegerField(blank=True, null=True,default="0")
    Value_Subcharge_ToPay=models.IntegerField(blank=True, null=True,default="0")
    AOC_ToPay=models.IntegerField(blank=True, null=True,default="0")
    Hamali_Charges_ToPay=models.IntegerField(blank=True, null=True,default="0")
    Other_Charges_ToPay=models.IntegerField(blank=True, null=True,default="0")
    Door_Delivery_ToPay=models.IntegerField(blank=True, null=True,default="0")
    SUB_TOTAL_ToPay=models.IntegerField(blank=True, null=True,default="0")
    GST_ToPay_Per=models.FloatField(blank=True, null=True,default="0")
    GST_ToPay=models.FloatField(blank=True, null=True,default="0")
    GRAND_TOTAL_ToPay=models.FloatField(blank=True, null=True,default="0")

    Freight_Paid=models.IntegerField(blank=True, null=True,default="0")
    ST_Charges_Paid=models.IntegerField(blank=True, null=True,default="0")
    Value_Subcharge_Paid=models.IntegerField(blank=True, null=True,default="0")
    AOC_Paid=models.IntegerField(blank=True, null=True,default="0")
    Hamali_Charges_Paid=models.IntegerField(blank=True, null=True,default="0")
    Other_Charges_Paid=models.IntegerField(blank=True, null=True,default="0")
    Door_Delivery_Paid=models.IntegerField(blank=True, null=True,default="0")
    SUB_TOTAL_Paid=models.IntegerField(blank=True, null=True,default="0")
    GST_Paid_Per=models.FloatField(blank=True, null=True,default="0")
    GST_Paid=models.FloatField(blank=True, null=True,default="0")
    GRAND_TOTAL_Paid=models.FloatField(blank=True, null=True,default="0")

    Description=models.CharField(max_length=200,blank=True, null=True)
    Actual_Weight=models.IntegerField(blank=True, null=True)
    Charged_Weight=models.IntegerField(blank=True, null=True)
    Item_Type=models.CharField(max_length=50,blank=True, null=True)
    Delivery_At=models.CharField(max_length=50,null=True,default="")



    # def save(self,*args, **kwargs):
    #  super().save(*args,**kwargs)
    #  img=Image.open(self,From_File.path)
    #  if img.height > 300 or img.width > 300:
    #         output_size =(300*300)
    #         img.thumbnail(output_size)
    #         img.save(self.From_File.path)


    from PIL import Image
    def save(self,):
        super().save()
        img_From1 = Image.open(self.From_File.path)
        img_From2 = Image.open(self.From_File2.path)
        img_To = Image.open(self.To_File.path)
        img_To2 = Image.open(self.To_File2.path)
        img_To3 = Image.open(self.To_File3.path)
        img_To4 = Image.open(self.To_File4.path)
        img_To5 = Image.open(self.To_File5.path)
        

        if img_From1.height > 1500 or img_From1.width > 1500:
            output_size = (1500, 1500)
            img_From1.thumbnail(output_size)
            img_From1.save(self.From_File.path) 
        
        if img_From2.height > 1500 or img_From2.width > 1500:
            output_size = (1500, 1500)
            img_From2.thumbnail(output_size)
            img_From2.save(self.From_File2.path) 
        
        if img_To.height > 1500 or img_To.width > 1500:
            output_size = (1500, 1500)
            img_To.thumbnail(output_size)
            img_To.save(self.To_File.path)
        
        if img_To2.height > 1500 or img_To2.width > 1500:
            output_size = (1500, 1500)
            img_To2.thumbnail(output_size)
            img_To2.save(self.To_File2.path)
        
        if img_To3.height > 1500 or img_To3.width > 1500:
            output_size = (1500, 1500)
            img_To3.thumbnail(output_size)
            img_To3.save(self.To_File3.path)
        
        if img_To4.height > 1500 or img_To4.width > 1500:
            output_size = (1500, 1500)
            img_To4.thumbnail(output_size)
            img_To4.save(self.To_File4.path)
        
        if img_To5.height > 1500 or img_To5.width > 1500:
            output_size = (1500, 1500)
            img_To5.thumbnail(output_size)
            img_To5.save(self.To_File5.path)

    # def save(self,):
    #     super().save()
    #     img = Image.open(self.To_File.path)
    #     if img.height > 1000 or img.width > 1000:
    #         output_size = (1000, 1000)
    #         img.thumbnail(output_size)
    #         img.save(self.To_File.path)
        

def __str__(self):
        return self.From_company
    











