from http.client import HTTPResponse
from django.db.models import Max
from urllib import response
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from User_Travels.forms import Form_New_Entry,Form_Drop_Cust,Form_Manage_Diesel
from django.contrib.auth.models import User
from django.core.paginator import Paginator

from User_Travels.models import DB_Tourse_and_Travels


# Create your views here.
@login_required(login_url='/user/user_login')
def user_home(request):
    var_rec_all=DB_Tourse_and_Travels.objects.filter(driver_name_id=request.user.id)
    count_all=var_rec_all.count()

    var_rec_pending=DB_Tourse_and_Travels.objects.filter(status="Pending",driver_name_id=request.user.id)
    count_pending=var_rec_pending.count()

    var_rec_drop=DB_Tourse_and_Travels.objects.filter(status="Droped",driver_name_id=request.user.id)
    count_drop=var_rec_drop.count()

    data={'count_all':count_all,'count_pending':count_pending,'count_drop':count_drop}
    return render(request,'user_tourse_travels/user_home.html',data)

def new_entry(request):
    fm=Form_New_Entry()
    if request.method=="POST":
        fm=Form_New_Entry(request.POST,request.FILES)
        if fm.is_valid():
            dt=fm.save(commit=False)
            log_user=User.objects.get(username=request.user.username)
            dt.driver_name=log_user
            dt.save()
            messages.success(request,'Record Created Successfully')
            fm=Form_New_Entry()
    data={'fm':fm}
    return render(request,'user_tourse_travels/new_entry.html',data)

def pending_records(request):
    rec=DB_Tourse_and_Travels.objects.filter(status='Pending',driver_name_id=request.user.id).order_by('-id')
    data={'rec':rec}
    return render(request,'user_tourse_travels/pending_records.html',data)

def droped_records(request):
    rec=DB_Tourse_and_Travels.objects.filter(status='Droped',driver_name_id=request.user.id).order_by('-id')
    paginator=Paginator(rec,100)
    page_number=request.GET.get('page')
    page_record_finel=paginator.get_page(page_number)
    totalpage=page_record_finel.paginator.num_pages
    data={'rec':page_record_finel,'pagenumbers':[n+1 for n in range(totalpage)]}
    return render(request,'user_tourse_travels/Droped_records.html',data)

def drop_cust(request,id):
    initial_data={
        'status':'Droped'
    }
    if request.method=="POST":
        pi=DB_Tourse_and_Travels.objects.get(pk=id)
        fm=Form_Drop_Cust(request.POST,request.FILES,instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Droped Successfully..!")
            return redirect('/user_travels/droped_records/')
        else:
            pi=DB_Tourse_and_Travels.objects.get(pk=id)
            fm=Form_Drop_Cust(request.POST,request.FILES,instance=pi)
    else:
        pi=DB_Tourse_and_Travels.objects.get(pk=id)
        fm=Form_Drop_Cust(instance=pi,initial=initial_data)
    return render(request,"user_tourse_travels/drop_cust.html",{'fm':fm})



def manage_diesel(request,id):
        if request.method=="POST":
            pi=DB_Tourse_and_Travels.objects.get(pk=id)
            fm=Form_Manage_Diesel(request.POST,request.FILES,instance=pi)
            if fm.is_valid():
                fm.save()
                messages.success(request,"Updated Successfully..!")
                return redirect('/user_travels/pending_records/')
            else:
                pi=DB_Tourse_and_Travels.objects.get(pk=id)
                fm=Form_Manage_Diesel(request.POST,request.FILES,instance=pi)
        else:
            pi=DB_Tourse_and_Travels.objects.get(pk=id)
            fm=Form_Manage_Diesel(instance=pi)
        return render(request,"user_tourse_travels/manage_diesel.html",{'fm':fm})
