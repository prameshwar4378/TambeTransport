from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import redirect, render,get_object_or_404
from .forms import *
from .models import DB_Load_Unload_Vehical
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.core.paginator import Paginator



# Create your views here.
@login_required(login_url='/user/user_login')
def home(request):
    var_rec_all=DB_Load_Unload_Vehical.objects.filter(Driver_Name_id=request.user.id)
    count_all=var_rec_all.count()

    var_rec_pending=DB_Load_Unload_Vehical.objects.filter(Status="Pending",Driver_Name_id=request.user.id)
    count_pending=var_rec_pending.count()

    var_rec_delivered=DB_Load_Unload_Vehical.objects.filter(Status="Delivered",Driver_Name_id=request.user.id)
    count_delivered=var_rec_delivered.count()

    data={'count_all':count_all,'count_pending':count_pending,'count_delivered':count_delivered}
    return render(request,'UserApp/user_home.html',data)

from django.contrib.auth.models import User

@login_required(login_url='/user/user_login')
def user_choose_dashboard(request):
    return render(request,'UserApp/choose_dashboard.html')



@login_required(login_url='/user/user_login')
def new_entry(request):
    initial_data={
        'Status':'Pending'
    }

    fm=Form_New_Entry(initial=initial_data)
    if request.method=="POST":
        fm=Form_New_Entry(request.POST,request.FILES)
        if fm.is_valid():
            dt=fm.save(commit=False)
            log_user=User.objects.get(username=request.user.username)
            dt.Driver_Name=log_user
            dt.save()
            messages.success(request,'Record Created Successfully')
            fm=Form_New_Entry()
    return render(request,'UserApp/new_entry.html',{'entry_form':fm})

    # Create your views here.
@login_required(login_url='/user/user_login')
def pending_records(request):
    rec=DB_Load_Unload_Vehical.objects.filter(Status="Pending",Driver_Name_id=request.user.id).order_by('-id')
    data={'rec':rec}
    return render(request,'UserApp/pending_records.html',data)

    # Create your views here.
@login_required(login_url='/user/user_login')
def delivered_records(request):
    rec=DB_Load_Unload_Vehical.objects.filter(Status="Delivered",Driver_Name_id=request.user.id).order_by('-id')
    paginator=Paginator(rec,100)
    page_number=request.GET.get('page')
    page_record_finel=paginator.get_page(page_number)
    totalpage=page_record_finel.paginator.num_pages
    data={'rec':page_record_finel,'pagenumbers':[n+1 for n in range(totalpage)]}
    return render(request,'UserApp/delivered_records.html',data)

def deliver_form(request,id):
    initial_data={
        'Status':'Delivered'
    }
    if request.method=="POST":
        pi=DB_Load_Unload_Vehical.objects.get(pk=id)
        fm=Form_Deliver_Stock(request.POST,request.FILES,instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Delivered Successfully..!")
            return redirect('/user/delivered_records/')
        else:
            pi=DB_Load_Unload_Vehical.objects.get(pk=id)
            fm=Form_Deliver_Stock(request.POST,request.FILES,instance=pi)
    else:
        pi=DB_Load_Unload_Vehical.objects.get(pk=id)
        fm=Form_Deliver_Stock(instance=pi, initial=initial_data)
    return render(request,"UserApp/deliver_form.html",{'fm':fm})


# def generate_lr(request,id):
#       dt=get_object_or_404(DB_Load_Unload_Vehical,id=id)
#       return render(request,"UserApp/generate_Lr_New.html",{'data':dt})



# def user_login(request):
#     fm=Form_user_login()
#     if request.method=='POST':
#         try:
#             login=DBUser.objects.get(emp_user_id=request.POST['emp_user_id'],emp_pass=request.POST['emp_pass'])
#             print('username = ',login)
#             request.session['emp_user_id']=login.emp_user_id
#             return render(request,"UserApp/user_base.html")
#         except DBUser.DoesNotExist as e:
#             messages.success(request,"username and password is invalid")
#     return render(request,"UserApp/user_login.html",{'fm':fm})


# def logout(request):
#     try:
#         del request.session['emp_user_id']
#     except:
#         return redirect('/user_login/')
#     return render(request,("UserApp/user_login.html"))

    
def contact_us(request):
    fm=Form_Contact_Us()
    if request.method=="POST":
        fm=Form_Contact_Us(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Thank You...! We will contact you soon')
            return redirect('/user/contact_us/')
    return render(request,'UserApp/contact_us.html',{'fm':fm})


def user_login(request):

    form=user_login_form()
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/user_choose_dashboard',{'user',user})
        else:
            form=user_login_form()
            messages.error(request,'Opps...! User does not exist... Please try again..!')

    return render(request,"UserApp/user_login.html",{'form':form})


def user_logout(request):
    logout(request)
    return redirect('/')

