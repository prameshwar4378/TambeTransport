from http.client import HTTPResponse
from django.db.models import Max
from urllib import response
import xlwt
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from Admin_Travels.forms import Form_Update_Travel_Record
from User_Travels.models import DB_Tourse_and_Travels
from django.core.paginator import Paginator
from django.shortcuts import redirect, render,get_object_or_404
from Admin_Travels.filters import Travel_Record_Data_Filter

# Create your views here.
@login_required(login_url='/admin_login')
def admin_home(request):
    var_rec_all=DB_Tourse_and_Travels.objects.all()
    count_all=var_rec_all.count()

    var_rec_pending=DB_Tourse_and_Travels.objects.filter(status="Pending")
    count_pending=var_rec_pending.count()

    var_rec_droped=DB_Tourse_and_Travels.objects.filter(status="Droped")
    count_droped=var_rec_droped.count()

    var_user_all=User.objects.all()
    count_user_all=var_user_all.count()

    data={'count_all':count_all,'count_pending':count_pending,'count_droped':count_droped,'count_user_all':count_user_all}
    
    return render(request,'admin_tourse_travels/admin_home.html',data)

def admin_travel_all_records(request):
    rec=DB_Tourse_and_Travels.objects.order_by('-id')
    Filter=Travel_Record_Data_Filter(request.GET, queryset=rec)
    rec2=Filter.qs    
    count=rec2.count()
    paginator=Paginator(rec,100)
    page_number=request.GET.get('page')
    page_record_finel=paginator.get_page(page_number)
    totalpage=page_record_finel.paginator.num_pages
    data={'rec':page_record_finel,'filter':Filter,'rec2':rec2,'count':count,'pagenumbers':[n+1 for n in range(totalpage)]}
    return render(request,'admin_tourse_travels/All_Records.html',data)


def print_travel_receipt(request,id):
      dt=get_object_or_404(DB_Tourse_and_Travels,id=id)
      return render(request,"admin_tourse_travels/Print_Receipt.html",{'data':dt})


def update_travel_record(request,id):
    if request.method=="POST":
        pi=DB_Tourse_and_Travels.objects.get(pk=id)
        fm=Form_Update_Travel_Record(request.POST,request.FILES,instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Record Updated Successfully..!")
            return redirect('/admin_travels/admin_travel_all_records')
        else:
            pi=DB_Tourse_and_Travels.objects.get(pk=id)
            fm=Form_Update_Travel_Record(request.POST,request.FILES,instance=pi)
    else:
        pi=DB_Tourse_and_Travels.objects.get(pk=id)
        fm=Form_Update_Travel_Record(instance=pi)
    return render(request,"admin_tourse_travels/update_travel_record.html",{'fm':fm})

def delete_travel_record(request,id):
    if request.method=='POST':
        rm=Form_Update_Travel_Record(request.POST)
        pi=DB_Tourse_and_Travels.objects.get(pk=id)
        pi.delete()
        messages.success(request,'Record Deleted Successfully')
    return redirect('/admin_travels/admin_travel_all_records',{'pi':pi})


from Admin_Travels.resources import DB_Tourse_Travels_Resource
def travel_export_excel(request):
    record_resource = DB_Tourse_Travels_Resource()
    dataset = record_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Database.xls"'
    return response
