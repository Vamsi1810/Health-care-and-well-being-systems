from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls.conf import path
from .forms import AppointmentForm, ConsultationForm
from .models import Appointment, Hospital, MedicineCart
from authentication.forms import FeedbackForm
from pharmacy.models import MedicineOrder, Medicine
from pharmacy.forms import MedicineForm
from doctor.models import HealthTips,Slot,Doctor, Consult
from django.core.mail import send_mail
from django.core.files.storage import FileSystemStorage
from datetime import date
import datetime
import re

def CheckProfession(request):
    try:
        a=request.session['username']
        if a is None:
            return None
        else:
            pro=request.session['profession']
            return pro
    except:
        return None

def ContactPage(request):
    pro=CheckProfession(request)
    if pro=='doctor':
        return redirect('dochome')
    elif pro=='pharmacy':
        return redirect('pharmacyhome')
    conform=FeedbackForm()
    if request.method=="POST":
        conform=FeedbackForm(request.POST)
        print(conform.data)
        if conform.is_valid():
            conform.save()
            return render(request,"cuscontact.html",{'feed':'Feedback Was Sent Successfully'})
    return render(request,"cuscontact.html",{'form':conform})

def AboutPage(request):
    pro=CheckProfession(request)
    if pro=='doctor':
        return redirect('dochome')
    elif pro=='pharmacy':
        return redirect('pharmacyhome')
    return render(request,'cusabout.html')

def CustomerHome(request):
    pro=CheckProfession(request)
    if pro=='doctor':
        return redirect('dochome')
    elif pro=='pharmacy':
        return redirect('pharmacyhome')
    medor=MedicineOrder.objects.filter(useremail=request.session['email'])
    data1=[0,0,0,0,0,0,0,0,0,0,0,0]
    for i in medor:
        my_mon = i.date.strftime("%m")
        p=int(my_mon)
        data1[p-1]+=1
    data2=[0,0,0,0,0,0,0,0,0,0,0,0]
    con=Consult.objects.filter(useremail=request.session['email'])
    for i in con:
        my_mon = i.date.strftime("%m")
        p=int(my_mon)
        data2[p-1]+=1
    return render(request,'cusHome.html',{'data1':data1,'data2':data2})

def CusOrders(request):
    pro=CheckProfession(request)
    if pro=='doctor':
        return redirect('dochome')
    elif pro=='pharmacy':
        return redirect('pharmacyhome')
    orders=MedicineOrder.objects.filter(useremail=request.session['email'])
    print(orders)
    if request.method=="POST":
        rem=request.POST.get("remove")
        remove=rem.split(",")
        ors=MedicineOrder.objects.get(medicinename=remove[0],email=remove[1],useremail=request.session['email'])
        ors.delete()
        orders=MedicineOrder.objects.filter(useremail=request.session['email'])
        price=0
        for c in orders:
            price=price+c.endprice
        print(price)
        if(price!=0):
            return render(request,'cusOrders.html',{'orders':orders,'success':'Successfully deleted the order!','price':price})
        return render(request,'cusOrders.html',{'orders':orders,'success':'Successfully deleted the order!'})
    price=0
    for c in orders:
        price=price+c.endprice
    print(price)
    return render(request,'cusOrders.html',{'orders':orders,'price':price})

def Cuscart(request):
    pro=CheckProfession(request)
    if pro=='doctor':
        return redirect('dochome')
    elif pro=='pharmacy':
        return redirect('pharmacyhome')
    carts=MedicineCart.objects.filter(useremail=request.session['email'])
    if request.method=="POST":
        if 'remove' in request.POST:
            rem=request.POST.get("remove")
            cartremove=rem.split(",")
            print(cartremove)
            carem=MedicineCart.objects.get(medicinename=cartremove[0],email=cartremove[1],useremail=request.session['email'])
            print(carem)
            carem.delete()
            carts=MedicineCart.objects.filter(useremail=request.session['email'])
            price=0
            for c in carts:
                price=price+c.endprice
            print(price)
            if(price!=0):
                return render(request,'cusCart.html',{'carts':carts,'success':'successfully removed from cart','price':price})
            return render(request,'cusCart.html',{'carts':carts,'success':'successfully removed from cart'})
        else:
            ordata=request.POST.get("order")
            detlist=ordata.split(",")
            details=MedicineCart.objects.get(medicinename=detlist[0],email=detlist[1])
            try:
                modi=MedicineOrder.objects.get(username=request.session['username'],medicinename=details.medicinename,email=detlist[1])
                print(modi)
                return render(request,'cusmedicines.html',{'medicines':carts,'error':'Order was already placed'})
            except:
                mo=MedicineOrder(username=request.session['username'],useremail=request.session['email'],usermobile=request.session['mobile'],
                userlocation=request.session['location'],medicinename=details.medicinename,email=details.email,location=details.location,
                startprice=details.startprice,endprice=details.endprice,image=details.image)
                mo.save()
                cc=MedicineCart.objects.get(useremail=request.session['email'],medicinename=detlist[0],email=detlist[1])
                cc.delete()
                carts=MedicineCart.objects.filter(useremail=request.session['email'])
                price=0
                for c in carts:
                    price=price+c.endprice
                print(price)
                return render(request,'cusmedicines.html',{'medicines':carts,'success':'order has been placed successfully','price':price})
    price=0
    for c in carts:
        price=price+c.endprice
    print(price)
    return render(request,'cusCart.html',{'carts':carts,'price':price})

def Placeorder(request):
    carts=MedicineCart.objects.filter(useremail=request.session['email'])
    for c in carts:
        mo=MedicineOrder(username=c.username,useremail=c.useremail,usermobile=c.usermobile,userlocation=c.userlocation,medicinename=c.medicinename,email=c.email,location=c.location,startprice=c.startprice,endprice=c.endprice,image=c.image)
        mo.save()
        c.delete()
    return redirect('cusorders')

def HospitalsList(request):
    pro=CheckProfession(request)
    if pro=='doctor':
        return redirect('dochome')
    elif pro=='pharmacy':
        return redirect('pharmacyhome')
    try:
        hospitals=Hospital.objects.all()
        if request.method=="POST":
            results = []
            name = str(request.POST['search'])
            c=0
            for i in hospitals:
                if re.match(name, i.name, re.IGNORECASE):
                    results.append(i)
                    c=c+1
            print(c)
            if c!=0:
                return render(request,'hospitals.html',{'hospitals': results})
            return render(request,'hospitals.html',{'error': "no results found"})
        return render(request,'hospitals.html',{'hospitals':hospitals})
    except:
        return render(request,'hospitals.html')

def MedicalHistory(request):
    pro=CheckProfession(request)
    if pro=='doctor':
        return redirect('dochome')
    elif pro=='pharmacy':
        return redirect('pharmacyhome')
    return render(request,'medicalHistory.html')

def Payment(request):
    pro=CheckProfession(request)
    if pro=='doctor':
        return redirect('dochome')
    elif pro=='pharmacy':
        return redirect('pharmacyhome')
    return render(request,'cusPayment.html')

def ConsultsPage(request):
    pro=CheckProfession(request)
    if pro=='doctor':
        return redirect('dochome')
    elif pro=='pharmacy':
        return redirect('pharmacyhome')
    dt=date.today()
    s=Slot.objects.filter(date__gte=dt)
    return render(request,'ConsultDoctor.html',{'doctors':s})

def ConsultDoctor(request,email,date):
    pro=CheckProfession(request)
    if pro=='doctor':
        return redirect('dochome')
    elif pro=='pharmacy':
        return redirect('pharmacyhome')
    dcdetails=Doctor.objects.get(email=email)
    # c=Consult(username=request.session['username'],useremail=request.session['email'],doctoremail=email,date=date)
    slot=request.POST.get('con')
    doc=Doctor.objects.get(email=email)
    doctorname=doc.firstname+" "+doc.lastname
    print(doctorname)
    return render(request,'consultRequirements.html',{'form':ConsultationForm(initial={'slot':slot}),'username':request.session['username'],'doctorname':doctorname,'useremail':request.session['email'],'doctoremail':email,'date':date})

def UpdateProbleToConsultation(request):
    frm=ConsultationForm(request.POST,request.FILES)
    print(frm.is_valid())
    if frm.is_valid():
        fs=FileSystemStorage()
        report=request.FILES['report']
        fs.save(report.name,report)
        frm.save()
    return redirect('consult')

def MedicinesPage(request):
    pro=CheckProfession(request)
    if pro=='doctor':
        return redirect('dochome')
    elif pro=='pharmacy':
        return redirect('pharmacyhome')
    try:
        medicines=Medicine.objects.all()
        if request.method=="POST":
            medform=MedicineForm(request.POST)
            ca=request.POST.get('cart')
            detlist=ca.split(",")
            details=Medicine.objects.get(medicinename=detlist[0],email=detlist[1])
            print(medform.data)
            try:
                mpl=MedicineCart.objects.get(username=request.session['username'],medicinename=details.medicinename,location=details.location)
                print(mpl)
                return render(request,'cusmedicines.html',{'medicines':medicines,'error':'medicine was already in the cart'})
            except:
                mc=MedicineCart(username=request.session['username'],useremail=request.session['email'],usermobile=request.session['mobile'],
                userlocation=request.session['location'],medicinename=details.medicinename,email=details.email,location=details.location,
                startprice=details.startprice,endprice=details.endprice,image=details.image)
                mc.save()
                return render(request,'cusmedicines.html',{'medicines':medicines,'success':'Medicine has been added to cart'})
            # if 'cart' in request.POST:
                
            # else:
            #     ca=request.POST.get('order')
            #     detlist=ca.split(",")
            #     details=Medicine.objects.get(medicinename=detlist[0],email=detlist[1])
            #     print(medform.data)
            #     try:
            #         mpl=MedicineOrder.objects.get(username=request.session['username'],medicinename=details.medicinename)
            #         print(mpl)
            #         return render(request,'cusmedicines.html',{'medicines':medicines,'error':'medicine was already in the Ordered'})
            #     except:
            #         mo=MedicineOrder(username=request.session['username'],useremail=request.session['email'],usermobile=request.session['mobile'],
            #         userlocation=request.session['location'],medicinename=details.medicinename,email=details.email,location=details.location,
            #         startprice=details.startprice,endprice=details.endprice,image=details.image)
            #         mo.save()
            #         return render(request,'cusmedicines.html',{'medicines':medicines,'success':'order has been placed successfully'})
        return render(request,'cusmedicines.html',{'medicines':medicines})
    except:
        return render(request,'cusmedicines.html')

def Appointmentpage(request,name):
    pro=CheckProfession(request)
    if pro=='doctor':
        return redirect('dochome')
    elif pro=='pharmacy':
        return redirect('pharmacyhome')
    aform=AppointmentForm()
    name=name.replace("%20"," ")
    if request.method=="POST":
        aform=AppointmentForm(request.POST,request.FILES)
        try:
            totalslot=Appointment.objects.filter(hospital=name,date=aform.data['date'], slot=aform.data['slot'])
            c=0
            for t in totalslot:
                c+=1
            if c>5:
                return render(request,'appointment.html',{'form':aform,'error':'Sorry slots are filled'})
            try:
                appoint=Appointment.objects.get(email=aform.data['email'],slot=aform.data['slot'],date=aform.data['date'])
                return render(request,'appointment.html',{'form':aform,'error':'Your slot is already booked'})
            except:
                aform.save()
            aform.save()
            return render(request,'appointment.html',{'form':aform,'success':'Your slot is booked successfully'})
        except:
            aform.save()
            return render(request,'appointment.html',{'form':aform,'success':'Your slot is booked successfully'})
    return render(request,'appointment.html',{'form':aform,'name':name,'username':request.session['username'],'email':request.session['email'],'mobile':request.session['mobile']})

def HealthTipsPage(request):
    pro=CheckProfession(request)
    if pro=='doctor':
        return redirect('dochome')
    elif pro=='pharmacy':
        return redirect('pharmacyhome')
    tips=HealthTips.objects.all()
    return render(request,'cushealthtips.html',{'tips':tips})

def LogoutDoctello(request):
    del request.session['username']
    del request.session['email']
    del request.session['mobile']
    del request.session['location']
    del request.session['profession']
    return redirect('home')

def ProfilePage(request):
    return render(request,'cusprofile.html')

def AllconsultationsPage(request):
    consults=Consult.objects.filter(useremail=request.session['email'])
    return render(request,'cusallconsultations.html',{'consults':consults})