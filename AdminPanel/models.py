from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class DBUser(models.Model):
    emp_name=models.CharField(max_length=100)
    emp_id_no=models.CharField(max_length=100)
    emp_license_no=models.CharField(max_length=100)
    emp_adress=models.CharField(max_length=100)
    emp_user_id=models.CharField(max_length=50,)
    emp_pass=models.CharField(max_length=50)
    emp_co_pass=models.CharField(max_length=50)

# class DBuser_AddFields(models.Model):
#     user=models.OneToOneField(User,on_delete=models.CASCADE)
#     mobile=models.IntegerField()

class DB_Company_List(models.Model):
    Company_Name=models.CharField(max_length=100)

    def __str__(self):
        return self.Company_Name