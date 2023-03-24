from PIL import Image
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
VEHICAL_TYPE=(
    ('CAR','CAR'),
    ('BUS','BUS'),
    ('TRAVELS','TRAVELS'),
    ('OTHER','OTHER'),
)
STATUS=(
    ('Pending','Pending'),
    ('Droped','Droped'),
)


class DB_Tourse_and_Travels(models.Model):
        bill_no=models.IntegerField(null=True)
        driver_name=models.ForeignKey(User, related_name="Driver_Name", on_delete=models.CASCADE)
        vehical_no=models.CharField(max_length=50)
        vehical_type=models.CharField(max_length=50,choices=VEHICAL_TYPE)
        arivel_city = models.CharField(max_length=50)
        arivel_time=models.DateTimeField(auto_now=False, auto_now_add=True, editable=True)
        destination_city=models.CharField(max_length=50)
        destination_time=models.DateTimeField(auto_now=True, auto_now_add=False, editable=True)
        opning_km=models.IntegerField()
        closing_km=models.IntegerField(null=True)
        opning_km_photo=models.ImageField(default="static/default.jpg",upload_to="opning_km", height_field=None, width_field=None, max_length=None)
        closing_km_photo=models.ImageField(default="static/default.jpg",upload_to="closing_km", height_field=None, width_field=None, max_length=None,null=True)
        total_km=models.IntegerField(null=True)
        cust_name=models.CharField(max_length=50)
        cust_photo=models.ImageField(upload_to="customer_photo",default="static/default.jpg", height_field=None, width_field=None, max_length=None,null=True,blank=True)
        order_by=models.CharField(max_length=100,null=True,blank=True)
        order_by_photo=models.ImageField(upload_to='order_by',default="static/default.jpg", height_field=None, width_field=None, max_length=None,null=True,blank=True)
        status=models.CharField(default='Pending', max_length=50,choices=STATUS)

        toll_name_1=models.CharField(max_length=50,null=True,blank=True)
        toll_name_2=models.CharField(max_length=50,null=True,blank=True)
        toll_name_3=models.CharField(max_length=50,null=True,blank=True)
        toll_name_4=models.CharField(max_length=50,null=True,blank=True)
        toll_name_5=models.CharField(max_length=50,null=True,blank=True)
        toll_name_6=models.CharField(max_length=50,null=True,blank=True)
        
        toll_amount_1=models.IntegerField(null=True,blank=True)
        toll_amount_2=models.IntegerField(null=True,blank=True)
        toll_amount_3=models.IntegerField(null=True,blank=True)
        toll_amount_4=models.IntegerField(null=True,blank=True)
        toll_amount_5=models.IntegerField(null=True,blank=True)
        toll_amount_6=models.IntegerField(null=True,blank=True)

        km_reading_1=models.IntegerField(null=True,blank=True)
        km_reading_2=models.IntegerField(null=True,blank=True)
        km_reading_3=models.IntegerField(null=True,blank=True)
        km_reading_4=models.IntegerField(null=True,blank=True)
        
        diesel_amount_1=models.IntegerField(null=True,blank=True)
        diesel_amount_2=models.IntegerField(null=True,blank=True)
        diesel_amount_3=models.IntegerField(null=True,blank=True)
        diesel_amount_4=models.IntegerField(null=True,blank=True)

        diesel_meter_photo_1=models.ImageField(upload_to='diesel 1',null=True,blank=True,)
        diesel_meter_photo_2=models.ImageField(upload_to='diesel 2',null=True,blank=True)
        diesel_meter_photo_3=models.ImageField(upload_to='diesel 3',null=True,blank=True)
        diesel_meter_photo_4=models.ImageField(upload_to='diesel 4',null=True,blank=True)




        def save(self,):
            if self.diesel_meter_photo_1:
                super().save()
                diesel_photo_1 = Image.open(self.diesel_meter_photo_1.path) 
                if diesel_photo_1.height > 1200 or diesel_photo_1.width > 1200:
                    output_size = (1200, 1200)
                    diesel_photo_1.thumbnail(output_size)
                    diesel_photo_1.save(self.diesel_meter_photo_1.path)
                    
            if self.diesel_meter_photo_2:
                super().save()
                diesel_photo_2 = Image.open(self.diesel_meter_photo_2.path) 
                if diesel_photo_2.height > 1200 or diesel_photo_2.width > 1200:
                    output_size = (1200, 1200)
                    diesel_photo_2.thumbnail(output_size)
                    diesel_photo_2.save(self.diesel_meter_photo_2.path)
                    
            if self.diesel_meter_photo_3:
                super().save()
                diesel_photo_3 = Image.open(self.diesel_meter_photo_3.path) 
                if diesel_photo_3.height > 1200 or diesel_photo_3.width > 1200:
                    output_size = (1200, 1200)
                    diesel_photo_3.thumbnail(output_size)
                    diesel_photo_3.save(self.diesel_meter_photo_3.path)
                    
            if self.diesel_meter_photo_4:
                super().save()
                diesel_photo_4 = Image.open(self.diesel_meter_photo_4.path) 
                if diesel_photo_4.height > 1200 or diesel_photo_4.width > 1200:
                    output_size = (1200, 1200)
                    diesel_photo_4.thumbnail(output_size)
                    diesel_photo_4.save(self.diesel_meter_photo_4.path)

                    
            if self.opning_km_photo:
                super().save()
                opning_km = Image.open(self.opning_km_photo.path)
                if opning_km.height > 1200 or opning_km.width > 1200:
                    output_size = (1200, 1200)
                    opning_km.thumbnail(output_size)
                    opning_km.save(self.opning_km_photo.path)

                    
            if self.closing_km_photo:
                super().save()
                closing_km = Image.open(self.closing_km_photo.path) 
                if closing_km.height > 1200 or closing_km.width > 1200:
                    output_size = (1200, 1200)
                    closing_km.thumbnail(output_size)
                    closing_km.save(self.closing_km_photo.path)

 
                    
            if self.cust_photo:
                super().save()
                customer_photo = Image.open(self.cust_photo.path) 
                if customer_photo.height > 1200 or customer_photo.width > 1200:
                    output_size = (1200, 1200)
                    customer_photo.thumbnail(output_size)
                    customer_photo.save(self.cust_photo.path) 


            if self.order_by_photo:
                super().save()    
                order_by_ph = Image.open(self.order_by_photo.path) 
                if order_by_ph.height > 1200 or order_by_ph.width > 1200:
                    output_size = (1200, 1200)
                    order_by_ph.thumbnail(output_size)
                    order_by_ph.save(self.order_by_photo.path)  

    # def save(self,):
    #     super().save()
    #     opning_km = Image.open(self.opning_km_photo.path) 
    #     closing_km = Image.open(self.closing_km_photo.path) 
    #     customer_photo = Image.open(self.cust_photo.path) 
    #     order_by_ph = Image.open(self.order_by_photo.path) 
    #     diesel_photo_1 = Image.open(self.diesel_meter_photo_1.path) 
    #     diesel_photo_2 = Image.open(self.diesel_meter_photo_2.path) 
    #     diesel_photo_3 = Image.open(self.diesel_meter_photo_3.path) 
    #     diesel_photo_4 = Image.open(self.diesel_meter_photo_4.path) 

    #     if opning_km.height > 1200 or opning_km.width > 1200:
    #         output_size = (1200, 1200)
    #         opning_km.thumbnail(output_size)
    #         opning_km.save(self.opning_km_photo.path)

    #     if closing_km.height > 1200 or closing_km.width > 1200:
    #         output_size = (1200, 1200)
    #         closing_km.thumbnail(output_size)
    #         closing_km.save(self.closing_km_photo.path)

    #     if customer_photo.height > 1200 or customer_photo.width > 1200:
    #         output_size = (1200, 1200)
    #         customer_photo.thumbnail(output_size)
    #         customer_photo.save(self.cust_photo.path)  

    #     if order_by_ph.height > 1200 or order_by_ph.width > 1200:
    #         output_size = (1200, 1200)
    #         order_by_ph.thumbnail(output_size)
    #         order_by_ph.save(self.order_by_photo.path)  

    #     if diesel_photo_1.height > 1200 or diesel_photo_1.width > 1200:
    #         output_size = (1200, 1200)
    #         diesel_photo_1.thumbnail(output_size)
    #         diesel_photo_1.save(self.diesel_meter_photo_1.path)  

    #     if diesel_photo_2.height > 1200 or diesel_photo_2.width > 1200:
    #         output_size = (1200, 1200)
    #         diesel_photo_2.thumbnail(output_size)
    #         diesel_photo_2.save(self.diesel_meter_photo_2.path)  

    #     if diesel_photo_3.height > 1200 or diesel_photo_3.width > 1200:
    #         output_size = (1200, 1200)
    #         diesel_photo_3.thumbnail(output_size)
    #         diesel_photo_3.save(self.diesel_meter_photo_3.path)  

    #     if diesel_photo_4.height > 1200 or diesel_photo_4.width > 1200:
    #         output_size = (1200, 1200)
    #         diesel_photo_4.thumbnail(output_size)
    #         diesel_photo_4.save(self.diesel_meter_photo_4.path)  
