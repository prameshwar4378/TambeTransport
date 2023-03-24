from django.db.models import Max
from urllib import response
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from AdminPanel.models import DBUser,DB_Company_List
from User.forms import Form_Contact_Us, Form_Deliver_Stock
from User.models import DB_Contact_Us, DB_Load_Unload_Vehical
from AdminPanel.forms import UserRegistration,Form_Manage_Vehical_Records,login_form,From_Generate_LR
from django.contrib import messages
import xlwt
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import UserRegistration,Form_Company_list
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render,get_object_or_404
from AdminPanel.filters import All_Record_Data_Filter   
from django.core.paginator import Paginator



def index(request):
    fm=Form_Contact_Us()
    if request.method=="POST":
        fm=Form_Contact_Us(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Thank You...! We will contact you soon')
            fm=Form_Contact_Us()
    return render(request,'LoadingReport/index.html',{'form':fm})





@login_required(login_url='/admin_login')
def admin_choose_dashboard(request):
    return render(request,'LoadingReport/choose_dashboard.html')


# Create your views here.
@login_required(login_url='/admin_login')
def AdminHome(request):
    var_rec_all=DB_Load_Unload_Vehical.objects.all()
    count_all=var_rec_all.count()

    var_rec_pending=DB_Load_Unload_Vehical.objects.filter(Status="Pending")
    count_pending=var_rec_pending.count()

    var_rec_delivered=DB_Load_Unload_Vehical.objects.filter(Status="Delivered")
    count_delivered=var_rec_delivered.count()

    var_user_all=User.objects.all()
    count_user_all=var_user_all.count()

    data={'count_all':count_all,'count_pending':count_pending,'count_delivered':count_delivered,'count_user_all':count_user_all}
    return render(request,'LoadingReport/AdminHome.html',data)

@login_required(login_url='/admin_login')
def Manageuser(request):
    # if request.method=='POST':
    #      fm=UserRegistration(request.POST)
    #      if fm.is_valid():
    #         nm=fm.cleaned_data['emp_name']
    #         id=fm.cleaned_data['emp_id_no']
    #         li=fm.cleaned_data['emp_license_no']
    #         ad=fm.cleaned_data['emp_adress']
    #         uid=fm.cleaned_data['emp_user_id']
    #         ps=fm.cleaned_data['emp_pass']
    #         cps=fm.cleaned_data['emp_co_pass']
    #         reg=DBUser(emp_name=nm,emp_id_no=id,emp_license_no=li,emp_adress=ad,emp_user_id=uid,emp_pass=ps,emp_co_pass=cps)
    #         reg.save()
    #         messages.success(request,'Account Created Successfully!!!')
            
    #      else:
    #         fm=UserRegistration()

    # fm=UserRegistration()
    # dt=DBUser.objects.all()
    # data={'form':fm,'data':dt}
    fm=UserRegistration()
    if request.method=='POST':
         fm=UserRegistration(request.POST)
         if fm.is_valid():
             fm.save()
             fm=UserRegistration()
             messages.success(request,'Account Created Successfully!!!')
    dt=User.objects.all()
    data={'form':fm,'dt':dt}
    return render(request,'LoadingReport/ManageUser.html',data)


@login_required(login_url='/admin_login')
def Manage_Company(request):
    fm=Form_Company_list()
    if request.method=='POST':
         fm=Form_Company_list(request.POST)
         if fm.is_valid():
             fm.save()
             fm=Form_Company_list()
             messages.success(request,'New Company Added Successfully!!!')
    dt=DB_Company_List.objects.order_by('-id')
    data={'form':fm,'dt':dt}
    return render(request,'LoadingReport/company_list.html',data)

@login_required(login_url='/admin_login')
def Delete_Company_Name_List(request,id):
      if request.method=='POST':
        rm=Form_Company_list(request.POST)
        pi=DB_Company_List.objects.get(pk=id)
        pi.delete()
        messages.success(request,'Account Deleted Successfully!!!')
        return HttpResponseRedirect('/Admin_Home/manage_company/')


@login_required(login_url='/admin_login')
def Update_Company_Name_List(request,id):
    if request.method=="POST":
        rm=Form_Company_list(request.POST)
        pi=DB_Company_List.objects.get(pk=id)
        fm=Form_Company_list(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Record Updated Successfully')
            return redirect('/Admin_Home/manage_company/')
        else:
            pi=DB_Company_List.objects.get(pk=id)
            fm=Form_Company_list(request.POST, instance=pi)
    else:
        pi=DB_Company_List.objects.get(pk=id)
        fm=Form_Company_list(instance=pi)
    return render(request,'LoadingReport/update_company_list.html',{'form':fm})


@login_required(login_url='/admin_login')
def admin_pending_records(request):
    rec=DB_Load_Unload_Vehical.objects.filter(Status="Pending").order_by('-id')
    data={'rec':rec}            
    return render(request,'LoadingReport/admin_pending_records.html',data)


@login_required(login_url='/admin_login')
def AdminVehicalRecords(request):
    rec=DB_Load_Unload_Vehical.objects.order_by('-id')
    Filter=All_Record_Data_Filter(request.GET, queryset=rec)
    rec2=Filter.qs    
    count=rec2.count()
    paginator=Paginator(rec2,100)
    page_number=request.GET.get('page')
    page_record_finel=paginator.get_page(page_number)
    totalpage=page_record_finel.paginator.num_pages
    data={'rec':page_record_finel,'filter':Filter,'count':count,'pagenumbers':[n+1 for n in range(totalpage)]}
    return render(request,'LoadingReport/Admin_Records.html',data)



def delete_data(request,id):
    if request.method=='POST':
        rm=UserRegistration(request.POST)
        pi=User.objects.get(pk=id)
        pi.delete()
        messages.success(request,'Account Deleted Successfully!!!')
        return HttpResponseRedirect('/Admin_Home/manage_user/')


def delete_vehical_record(request,id):
    if request.method=='POST':
        rm=Form_Deliver_Stock(request.POST)
        pi=DB_Load_Unload_Vehical.objects.get(pk=id)
        pi.delete()
        messages.success(request,'Record Deleted Successfully')
    return redirect('/Admin_Home/admin_vehical_records/',{'pi':pi})

import os
def update_vehical_records(request,id):
    if request.method=="POST":
        pi=DB_Load_Unload_Vehical.objects.get(pk=id)
        fm=Form_Manage_Vehical_Records(request.POST,request.FILES, instance=pi)
        
        if fm.is_valid():
            fm.save()
        fm=Form_Manage_Vehical_Records()
        messages.success(request,'Record Updated Successfully')

        return redirect('/Admin_Home/admin_vehical_records/')
    else:
        pi=DB_Load_Unload_Vehical.objects.get(pk=id)
        fm=Form_Manage_Vehical_Records(instance=pi)
    return render(request,'LoadingReport/updateUser.html',{'fm':fm})


def update_user_data(request,id):
    if request.method=="POST":
        rm=UserRegistration(request.POST)
        pi=User.objects.get(pk=id)
        fm=UserRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Record Updated Successfully')
            return redirect('/Admin_Home/manage_user/')
        else:
            pi=User.objects.get(pk=id)
            fm=UserRegistration(request.POST, instance=pi)
    else:
        pi=User.objects.get(pk=id)
        fm=UserRegistration(instance=pi)
    return render(request,'LoadingReport/updateUser.html',{'fm':fm})


# def update_vehical_records(request):

def admin_login(request):
    form=login_form()
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            if user.is_superuser:
             login(request,user)
             return redirect('/admin_choose_dashboard',{'user',user})
            else:
             messages.error(request,'Opps...! You are not admin. Please try user login.! ')
             return redirect('/admin_login',{'user',user}) 
        else:
            form=login_form()
            messages.error(request,'Opps...! User does not exist... Please Try Again.!')

    return render(request,"LoadingReport/admin_login.html",{'form':form})


def admin_logout(request):
    logout(request)
    return redirect('/')

from .resources import DB_Load_Unload_Vehical_Resource,User_Resource
def export_data(request):
    record_resource = DB_Load_Unload_Vehical_Resource()
    dataset = record_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Vehical_Records.xls"'
    return response

def export_users(request):
    user_rec = User_Resource()
    dataset = user_rec.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'
    return response

# def print(request,id):
#       dt=get_object_or_404(DB_Load_Unload_Vehical,id=id)
#       return render(request,"LoadingReport/print_lr.html",{'data':dt})

# def generate_lr(request,id):
#     if request.method=="POST":
#         pi=DB_Load_Unload_Vehical.objects.get(pk=id)
#         fm=From_Generate_LR(request.POST,request.FILES,instance=pi)
#         if fm.is_valid():
#             fm.save()
#         return redirect('/Admin_Home/')
#     else:
#            pi=DB_Load_Unload_Vehical.objects.get(pk=id)
#            fm=From_Generate_LR(request.POST,request.FILES,instance=pi)

#     return render(request,"LoadingReport/generate_lr.html",{'fm':fm})


@login_required(login_url='/admin_login')
def enquiry(request):
    data=DB_Contact_Us.objects.order_by('-id')
    return render(request,"LoadingReport/Enquiry.html",{'data':data})


def generate_lr(request,id):
    Auto_LR_No=1 if DB_Load_Unload_Vehical.objects.filter(Auto_LR_No="1").count() == 0 else DB_Load_Unload_Vehical.objects.aggregate(max=Max('Auto_LR_No'))["max"] + int(1) 
    initialize_LR_NO={
        'Auto_LR_No':Auto_LR_No
    }

    if request.method=="POST":
        pi=DB_Load_Unload_Vehical.objects.get(pk=id)
        fm=From_Generate_LR(request.POST,request.FILES,instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,"LR Generated Successfully...!")
            return redirect('/Admin_Home/admin_pending_records/')
        else:
            pi=DB_Load_Unload_Vehical.objects.get(pk=id)
            fm=From_Generate_LR(request.POST,request.FILES,instance=pi)
    else:
        pi=DB_Load_Unload_Vehical.objects.get(pk=id)
        fm=From_Generate_LR(instance=pi,initial=initialize_LR_NO)
        # dt=DB_Load_Unload_Vehical.objects.all().aggregate(Max('Auto_LR_No'))
    return render(request,"LoadingReport/generate_lr.html",{'fm':fm,'dt':Auto_LR_No})

def update_lr(request,id):
    if request.method=="POST":
        pi=DB_Load_Unload_Vehical.objects.get(pk=id)
        fm=From_Generate_LR(request.POST,request.FILES,instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,"LR Updated Successfully...!")
            return redirect('/Admin_Home/admin_pending_records/')
        else:
            pi=DB_Load_Unload_Vehical.objects.get(pk=id)
            fm=From_Generate_LR(request.POST,request.FILES,instance=pi)
    else:
        pi=DB_Load_Unload_Vehical.objects.get(pk=id)
        fm=From_Generate_LR(instance=pi)
        dt=DB_Load_Unload_Vehical.objects.all().aggregate(Max('Auto_LR_No'))
    return render(request,"LoadingReport/generate_lr.html",{'fm':fm})


def print_lr(request,id):
      dt=get_object_or_404(DB_Load_Unload_Vehical,id=id)
      return render(request,"LoadingReport/Print_LR.html",{'data':dt})

